import { describe, expect, it } from "vitest";
import { LIQUIDACIONES, MOTOS } from "@/data/mock";
import { crearRepoMemoria } from "@/data/repo";
import { crearReducer, estadoInicial, validar, type AccionForm, type EstadoForm } from "./formulario";

const reducer = crearReducer(MOTOS);
const hoy = "2026-10-13";
const aplicar = (e: EstadoForm, ...acciones: AccionForm[]) => acciones.reduce(reducer, e);

describe("chofer al elegir la moto", () => {
  it("se llena con el chofer de la moto", () => {
    const e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-1" });
    expect(e.choferId).toBe("cho-1");
  });

  it("al cambiar la moto, se reemplaza por el de la moto nueva", () => {
    const e = aplicar(
      estadoInicial(hoy),
      { tipo: "moto", motoId: "mot-1" },
      { tipo: "chofer", choferId: "cho-4" },
      { tipo: "moto", motoId: "mot-2" },
    );
    expect(e.choferId).toBe("cho-2");
  });

  it("si la moto nueva no tiene chofer, queda vacío y es obligatorio", () => {
    const e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-4" }, { tipo: "monto", texto: "350" });
    expect(e.choferId).toBeNull();
    expect(validar(e, MOTOS)).toEqual({ ok: false, errores: { chofer: "Elige el chofer" } });
  });

  it("un chofer cambiado a mano se conserva hasta que se cambie la moto", () => {
    const e = aplicar(
      estadoInicial(hoy),
      { tipo: "moto", motoId: "mot-1" },
      { tipo: "chofer", choferId: "cho-4" },
      { tipo: "fecha", fecha: "2026-10-12" },
      { tipo: "monto", texto: "300" },
    );
    expect(e.choferId).toBe("cho-4");
  });
});

describe("nombre personalizado", () => {
  it("sin editar: cambiar la moto o la fecha recalcula el nombre", () => {
    let e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-1" });
    expect(e.nombre).toBe("27-ABC-4 · 13 oct 2026");
    e = aplicar(e, { tipo: "moto", motoId: "mot-2" });
    expect(e.nombre).toBe("31-XKT-8 · 13 oct 2026");
    e = aplicar(e, { tipo: "fecha", fecha: "2026-10-12" });
    expect(e.nombre).toBe("31-XKT-8 · 12 oct 2026");
    expect(e.nombrePersonalizado).toBe(false);
  });

  it("editar el nombre, aunque quede el mismo texto, lo marca y ya no se recalcula", () => {
    let e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-1" });
    e = aplicar(e, { tipo: "nombre", texto: "27-ABC-4 · 13 oct 2026" });
    expect(e.nombrePersonalizado).toBe(true);
    e = aplicar(e, { tipo: "moto", motoId: "mot-2" }, { tipo: "fecha", fecha: "2026-10-12" });
    expect(e.nombre).toBe("27-ABC-4 · 13 oct 2026");
  });

  it("registrar con nombre editado → corregir → cambiar moto y fecha → el nombre sigue igual", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const registro = aplicar(
      estadoInicial(hoy),
      { tipo: "moto", motoId: "mot-1" },
      { tipo: "monto", texto: "350" },
      { tipo: "nombre", texto: "Pago de Juan" },
    );
    const v1 = validar(registro, MOTOS);
    if (!v1.ok) throw new Error("debía ser válido");
    const guardada = repo.registrar(v1.datos);
    expect(guardada.nombrePersonalizado).toBe(true);

    // Abrir Corregir: la bandera llega en true.
    const corregir = estadoInicial(hoy, repo.obtener(guardada.id));
    expect(corregir.nombrePersonalizado).toBe(true);
    const cambiado = aplicar(corregir, { tipo: "moto", motoId: "mot-3" }, { tipo: "fecha", fecha: "2026-10-10" });
    const v2 = validar(cambiado, MOTOS);
    if (!v2.ok) throw new Error("debía ser válido");
    const final = repo.corregir(guardada.id, v2.datos);
    expect(final.nombre).toBe("Pago de Juan");
    expect(final.motoId).toBe("mot-3");
    expect(final.fecha).toBe("2026-10-10");
  });

  it("corregir una liquidación de prueba (bandera en false) y cambiar la fecha recalcula el nombre", () => {
    const liq = LIQUIDACIONES.find((l) => l.id === "liq-001")!;
    const e = aplicar(estadoInicial(hoy, liq), { tipo: "fecha", fecha: "2026-10-11" });
    expect(e.nombre).toBe("27-ABC-4 · 11 oct 2026");
  });
});

describe("validaciones", () => {
  it("formulario vacío: pide moto y monto", () => {
    expect(validar(estadoInicial(hoy), MOTOS)).toEqual({
      ok: false,
      errores: { moto: "Elige la moto", monto: "Escribe el monto en pesos" },
    });
  });

  it("monto inválido muestra su mensaje", () => {
    const e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-1" }, { tipo: "monto", texto: "0" });
    expect(validar(e, MOTOS)).toEqual({ ok: false, errores: { monto: "El monto debe ser mayor que $0" } });
  });

  it("formulario completo: devuelve los datos con el monto en centavos", () => {
    const e = aplicar(estadoInicial(hoy), { tipo: "moto", motoId: "mot-1" }, { tipo: "monto", texto: "1,500.5" });
    expect(validar(e, MOTOS)).toEqual({
      ok: true,
      datos: {
        motoId: "mot-1",
        choferId: "cho-1",
        fecha: "2026-10-13",
        montoCentavos: 150050,
        nombre: "27-ABC-4 · 13 oct 2026",
        nombrePersonalizado: false,
      },
    });
  });

  it("si dejan el nombre vacío, se guarda el automático", () => {
    const e = aplicar(
      estadoInicial(hoy),
      { tipo: "moto", motoId: "mot-1" },
      { tipo: "monto", texto: "350" },
      { tipo: "nombre", texto: "  " },
    );
    const v = validar(e, MOTOS);
    expect(v.ok && v.datos.nombre).toBe("27-ABC-4 · 13 oct 2026");
  });
});
