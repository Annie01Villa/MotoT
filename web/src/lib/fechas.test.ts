import { afterEach, describe, expect, it, vi } from "vitest";
import { now } from "./clock";
import {
  dateLocalDeFecha,
  diaRelativo,
  etiquetaDia,
  fechaDeDateLocal,
  fechaMx,
  formatFecha,
  formatFechaNumerica,
  sumarDias,
} from "./fechas";

afterEach(() => vi.useRealTimers());

describe("fechas de calendario en México", () => {
  it("prueba de medianoche: 2026-10-14T05:30Z es el 13 oct en México", () => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date("2026-10-14T05:30:00Z"));
    const hoy = fechaMx(now());
    expect(hoy).toBe("2026-10-13");
    expect(diaRelativo("2026-10-13", hoy)).toBe("Hoy");
    expect(diaRelativo("2026-10-12", hoy)).toBe("Ayer");
    expect(diaRelativo("2026-10-14", hoy)).toBeNull();
  });

  it("cambio de mes: el 1 nov, «Ayer» es el 31 oct", () => {
    vi.useFakeTimers();
    vi.setSystemTime(new Date("2026-11-01T18:00:00Z"));
    const hoy = fechaMx(now());
    expect(hoy).toBe("2026-11-01");
    expect(sumarDias(hoy, -1)).toBe("2026-10-31");
    expect(diaRelativo("2026-10-31", hoy)).toBe("Ayer");
  });

  it("cambio de año", () => {
    expect(sumarDias("2027-01-01", -1)).toBe("2026-12-31");
  });

  it("formatea «13 oct 2026» y «13/10/2026»", () => {
    expect(formatFecha("2026-10-13")).toBe("13 oct 2026");
    expect(formatFecha("2026-01-05")).toBe("5 ene 2026");
    expect(formatFechaNumerica("2026-01-05")).toBe("05/01/2026");
  });

  it("arma la etiqueta del grupo", () => {
    expect(etiquetaDia("2026-10-13", "2026-10-13")).toBe("Hoy · 13 oct 2026");
    expect(etiquetaDia("2026-10-12", "2026-10-13")).toBe("Ayer · 12 oct 2026");
    expect(etiquetaDia("2026-10-10", "2026-10-13")).toBe("10 oct 2026");
  });

  it("convierte la fecha del calendario por sus partes, sin pasar por UTC", () => {
    expect(fechaDeDateLocal(new Date(2026, 9, 13, 23, 59))).toBe("2026-10-13");
    expect(fechaDeDateLocal(dateLocalDeFecha("2026-03-01"))).toBe("2026-03-01");
  });
});
