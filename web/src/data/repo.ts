import { now } from "@/lib/clock";
import { etiquetaDia } from "@/lib/fechas";
import type { DatosLiquidacion, Liquidacion, LiquidacionesRepo } from "./types";

/** fecha ↓, luego creadaEn ↓ y, si empatan, id: el orden es siempre el mismo. */
export function compararLiquidaciones(a: Liquidacion, b: Liquidacion): number {
  if (a.fecha !== b.fecha) return a.fecha < b.fecha ? 1 : -1;
  if (a.creadaEn !== b.creadaEn) return a.creadaEn < b.creadaEn ? 1 : -1;
  return a.id < b.id ? 1 : a.id > b.id ? -1 : 0;
}

export function ordenar(lista: Liquidacion[]): Liquidacion[] {
  return [...lista].sort(compararLiquidaciones);
}

export type GrupoDia<T extends Liquidacion = Liquidacion> = { fecha: string; etiqueta: string; items: T[] };

/** Agrupa una lista ya ordenada por día, conservando el orden. */
export function agruparPorDia<T extends Liquidacion>(lista: T[], hoy: string): GrupoDia<T>[] {
  const grupos: GrupoDia<T>[] = [];
  for (const liq of lista) {
    const ultimo = grupos[grupos.length - 1];
    if (ultimo && ultimo.fecha === liq.fecha) ultimo.items.push(liq);
    else grupos.push({ fecha: liq.fecha, etiqueta: etiquetaDia(liq.fecha, hoy), items: [liq] });
  }
  return grupos;
}

// Copia explícita de los campos editables: id y creadaEn nunca vienen del formulario.
function camposEditables(d: DatosLiquidacion): DatosLiquidacion {
  return {
    fecha: d.fecha,
    motoId: d.motoId,
    choferId: d.choferId,
    montoCentavos: d.montoCentavos,
    nombre: d.nombre,
    nombrePersonalizado: d.nombrePersonalizado,
  };
}

export type RepoMemoria = LiquidacionesRepo & {
  subscribe(listener: () => void): () => void;
};

type Dependencias = { generarId?: () => string };

/** Repositorio en memoria (estado del cliente): se reinicia al recargar. */
export function crearRepoMemoria(semilla: Liquidacion[], deps: Dependencias = {}): RepoMemoria {
  const generarId = deps.generarId ?? (() => crypto.randomUUID());
  let lista = ordenar(semilla);
  const listeners = new Set<() => void>();
  const avisar = () => listeners.forEach((l) => l());

  return {
    listar: () => lista,
    obtener: (id) => lista.find((l) => l.id === id),
    registrar(datos) {
      const liq: Liquidacion = {
        ...camposEditables(datos),
        id: generarId(),
        creadaEn: now().toISOString(),
      };
      lista = ordenar([...lista, liq]);
      avisar();
      return liq;
    },
    corregir(id, cambios) {
      const actual = lista.find((l) => l.id === id);
      if (!actual) throw new Error(`No existe la liquidación ${id}`);
      const corregida: Liquidacion = {
        ...camposEditables(cambios),
        id: actual.id,
        creadaEn: actual.creadaEn,
      };
      lista = ordenar(lista.map((l) => (l.id === id ? corregida : l)));
      avisar();
      return corregida;
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
