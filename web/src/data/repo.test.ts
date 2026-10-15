import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { LIQUIDACIONES } from "./mock";
import { agruparPorDia, crearRepoMemoria, ordenar } from "./repo";
import type { DatosLiquidacion, Liquidacion } from "./types";

const datos: DatosLiquidacion = {
  fecha: "2026-10-13",
  motoId: "mot-3",
  choferId: "cho-3",
  montoCentavos: 30000,
  nombre: "12-MNO-5 · 13 oct 2026",
  nombrePersonalizado: false,
};

beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(new Date("2026-10-13T20:00:00Z"));
});
afterEach(() => vi.useRealTimers());

describe("identidad", () => {
  it("registrar devuelve la liquidación con un id único y creadaEn del reloj", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const a = repo.registrar(datos);
    const b = repo.registrar(datos);
    expect(a.id).not.toBe(b.id);
    expect(LIQUIDACIONES.some((l) => l.id === a.id)).toBe(false);
    expect(a.creadaEn).toBe("2026-10-13T20:00:00.000Z");
    expect(repo.obtener(a.id)).toEqual(a);
  });

  it("corregir cambia solo el registro de ese id y no toca id ni creadaEn", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const antes = repo.obtener("liq-002")!;
    const corregida = repo.corregir("liq-002", { ...datos, montoCentavos: 40000 });
    expect(corregida.id).toBe("liq-002");
    expect(corregida.creadaEn).toBe(antes.creadaEn);
    expect(corregida.montoCentavos).toBe(40000);
    for (const otra of LIQUIDACIONES.filter((l) => l.id !== "liq-002")) {
      expect(repo.obtener(otra.id)).toEqual(otra);
    }
  });

  it("corregir ignora id y creadaEn aunque vengan en los cambios", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const intento = { ...datos, id: "otro", creadaEn: "2000-01-01T00:00:00.000Z" } as DatosLiquidacion;
    const corregida = repo.corregir("liq-001", intento);
    expect(corregida.id).toBe("liq-001");
    expect(corregida.creadaEn).toBe("2026-10-13T18:00:00.000Z");
  });

  it("corregir un id que no existe falla", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    expect(() => repo.corregir("no-existe", datos)).toThrow();
  });
});

describe("orden y agrupado", () => {
  it("ordena por fecha ↓, luego creadaEn ↓ y luego id", () => {
    const base: Liquidacion = { ...datos, id: "x", creadaEn: "2026-10-13T10:00:00.000Z" };
    const lista = ordenar([
      { ...base, id: "a", fecha: "2026-10-12" },
      { ...base, id: "b", creadaEn: "2026-10-13T09:00:00.000Z" },
      { ...base, id: "c" },
      { ...base, id: "d" },
    ]);
    expect(lista.map((l) => l.id)).toEqual(["d", "c", "b", "a"]);
  });

  it("dos liquidaciones del mismo día: la registrada después va primero", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const nueva = repo.registrar(datos);
    expect(repo.listar()[0].id).toBe(nueva.id);
    expect(repo.listar().map((l) => l.id).slice(1)).toEqual(["liq-001", "liq-002", "liq-003", "liq-004"]);
  });

  it("corregir la fecha mueve la liquidación a su grupo y reordena", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const liq = repo.obtener("liq-001")!;
    repo.corregir("liq-001", { ...liq, fecha: "2026-10-12" });
    const grupos = agruparPorDia(repo.listar(), "2026-10-13");
    expect(grupos.map((g) => g.etiqueta)).toEqual(["Hoy · 13 oct 2026", "Ayer · 12 oct 2026"]);
    expect(grupos[0].items.map((l) => l.id)).toEqual(["liq-002"]);
    expect(grupos[1].items.map((l) => l.id)).toEqual(["liq-001", "liq-003", "liq-004"]);
  });

  it("avisa a quien está suscrito", () => {
    const repo = crearRepoMemoria(LIQUIDACIONES);
    const listener = vi.fn();
    const quitar = repo.subscribe(listener);
    repo.registrar(datos);
    expect(listener).toHaveBeenCalledTimes(1);
    quitar();
    repo.registrar(datos);
    expect(listener).toHaveBeenCalledTimes(1);
  });
});
