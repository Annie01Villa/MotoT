// Estado y reglas del formulario Registrar / Corregir liquidación.
import type { DatosLiquidacion, Liquidacion, Moto } from "@/data/types";
import { formatFecha } from "./fechas";
import { leerMonto, montoParaCampo, MENSAJES_MONTO } from "./monto";

export type EstadoForm = {
  motoId: string | null;
  choferId: string | null;
  fecha: string;
  montoTexto: string;
  nombre: string;
  nombrePersonalizado: boolean;
};

export type AccionForm =
  | { tipo: "moto"; motoId: string }
  | { tipo: "chofer"; choferId: string }
  | { tipo: "fecha"; fecha: string }
  | { tipo: "monto"; texto: string }
  | { tipo: "nombre"; texto: string };

export function nombreAutomatico(placa: string, fecha: string): string {
  return `${placa} · ${formatFecha(fecha)}`;
}

export function estadoInicial(hoy: string, liq?: Liquidacion): EstadoForm {
  if (!liq) {
    return { motoId: null, choferId: null, fecha: hoy, montoTexto: "", nombre: "", nombrePersonalizado: false };
  }
  return {
    motoId: liq.motoId,
    choferId: liq.choferId,
    fecha: liq.fecha,
    montoTexto: montoParaCampo(liq.montoCentavos),
    nombre: liq.nombre,
    nombrePersonalizado: liq.nombrePersonalizado,
  };
}

/** El reducer necesita las motos para saber su placa y su chofer. */
export function crearReducer(motos: Moto[]) {
  const placaDe = (motoId: string | null) => motos.find((m) => m.id === motoId)?.placa;

  // El nombre solo se recalcula mientras el usuario no lo haya escrito a mano.
  function conNombre(e: EstadoForm): EstadoForm {
    if (e.nombrePersonalizado) return e;
    const placa = placaDe(e.motoId);
    return placa ? { ...e, nombre: nombreAutomatico(placa, e.fecha) } : e;
  }

  return function reducer(e: EstadoForm, a: AccionForm): EstadoForm {
    switch (a.tipo) {
      case "moto": {
        // Al cambiar la moto, el chofer pasa a ser el de la moto nueva (o vacío si no tiene).
        const moto = motos.find((m) => m.id === a.motoId);
        return conNombre({ ...e, motoId: a.motoId, choferId: moto?.choferId ?? null });
      }
      case "chofer":
        return { ...e, choferId: a.choferId };
      case "fecha":
        return conNombre({ ...e, fecha: a.fecha });
      case "monto":
        return { ...e, montoTexto: a.texto };
      case "nombre":
        // Se marca aunque el texto quede igual: nunca se deduce comparando textos.
        return { ...e, nombre: a.texto, nombrePersonalizado: true };
    }
  };
}

export type ErroresForm = Partial<Record<"moto" | "chofer" | "monto", string>>;

export type ResultadoValidacion =
  | { ok: true; datos: DatosLiquidacion }
  | { ok: false; errores: ErroresForm };

export function validar(e: EstadoForm, motos: Moto[]): ResultadoValidacion {
  const errores: ErroresForm = {};
  if (!e.motoId) errores.moto = "Elige la moto";
  else if (!e.choferId) errores.chofer = "Elige el chofer";
  const monto = leerMonto(e.montoTexto);
  if (!monto.ok) errores.monto = MENSAJES_MONTO[monto.error];

  if (!e.motoId || !e.choferId || !monto.ok) return { ok: false, errores };
  const placa = motos.find((m) => m.id === e.motoId)?.placa ?? "";
  return {
    ok: true,
    datos: {
      motoId: e.motoId,
      choferId: e.choferId,
      fecha: e.fecha,
      montoCentavos: monto.centavos,
      // Si dejaron el nombre vacío, se guarda el automático.
      nombre: e.nombre.trim() || nombreAutomatico(placa, e.fecha),
      nombrePersonalizado: e.nombrePersonalizado,
    },
  };
}
