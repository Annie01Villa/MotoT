import { describe, expect, it } from "vitest";
import { formatMonto, leerMonto, MENSAJES_MONTO, montoParaCampo } from "./monto";

describe("leerMonto", () => {
  it.each([
    ["350", 35000],
    ["350.5", 35050],
    ["350.50", 35050],
    ["1,500.00", 150000],
    ["  350  ", 35000],
    ["0.01", 1],
  ])("acepta %j → %i centavos", (texto, centavos) => {
    expect(leerMonto(texto)).toEqual({ ok: true, centavos });
  });

  it.each([
    ["", "vacio"],
    ["   ", "vacio"],
    ["0", "cero"],
    ["0.00", "cero"],
    ["-5", "invalido"],
    ["350.505", "decimales"],
    ["abc", "invalido"],
    ["NaN", "invalido"],
    ["3 50", "invalido"],
    ["1234567890", "invalido"],
  ])("rechaza %j (%s)", (texto, error) => {
    expect(leerMonto(texto)).toEqual({ ok: false, error });
  });

  it("suma en centavos sin errores de punto flotante: 0.1 + 0.2 = 30", () => {
    const a = leerMonto("0.1");
    const b = leerMonto("0.2");
    if (!a.ok || !b.ok) throw new Error("debían ser válidos");
    expect(a.centavos + b.centavos).toBe(30);
    expect(formatMonto(a.centavos + b.centavos)).toBe("$0.30");
  });

  it("tiene un mensaje para cada error", () => {
    expect(MENSAJES_MONTO.vacio).toBe("Escribe el monto en pesos");
    expect(MENSAJES_MONTO.cero).toBe("El monto debe ser mayor que $0");
    expect(MENSAJES_MONTO.decimales).toBe("Escribe el monto con máximo 2 decimales");
    expect(MENSAJES_MONTO.invalido).toBe("Escribe solo números");
  });
});

describe("formato", () => {
  it("muestra dinero como $1,500.00", () => {
    expect(formatMonto(35000)).toBe("$350.00");
    expect(formatMonto(150000)).toBe("$1,500.00");
    expect(formatMonto(123456789)).toBe("$1,234,567.89");
    expect(formatMonto(5)).toBe("$0.05");
  });

  it("prepara el valor del campo al corregir", () => {
    expect(montoParaCampo(35000)).toBe("350.00");
    expect(montoParaCampo(35050)).toBe("350.50");
  });
});
