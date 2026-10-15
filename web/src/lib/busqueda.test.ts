import { describe, expect, it } from "vitest";
import { coincide, segmentar } from "./busqueda";

const hoy = "2026-10-13";
const juan = { placa: "27-ABC-4", chofer: "Juan Pérez López", fecha: "2026-10-13" };
const maria = { placa: "31-XKT-8", chofer: "María González Ruiz", fecha: "2026-10-12" };
const luis = { placa: "12-MNO-5", chofer: "Luis Hernández Soto", fecha: "2026-10-01" };

describe("búsqueda", () => {
  it("no distingue mayúsculas ni acentos", () => {
    expect(coincide(maria, "maria", hoy)).toBe(true);
    expect(coincide(maria, "MARÍA", hoy)).toBe(true);
    expect(coincide(juan, "perez", hoy)).toBe(true);
  });

  it("busca la placa con y sin guiones", () => {
    expect(coincide(juan, "27abc", hoy)).toBe(true);
    expect(coincide(juan, "27-ABC-4", hoy)).toBe(true);
    expect(coincide(juan, "abc4", hoy)).toBe(true);
    expect(coincide(maria, "27abc", hoy)).toBe(false);
  });

  it("busca cualquier parte del nombre del chofer", () => {
    expect(coincide(luis, "hernan", hoy)).toBe(true);
    expect(coincide(luis, "roberto", hoy)).toBe(false);
  });

  it("busca fechas en sus 3 formatos", () => {
    expect(coincide(juan, "13 oct 2026", hoy)).toBe(true);
    expect(coincide(juan, "13 oct", hoy)).toBe(true);
    expect(coincide(juan, "oct 2026", hoy)).toBe(true);
    expect(coincide(juan, "13/10/2026", hoy)).toBe(true);
    expect(coincide(luis, "1/10/2026", hoy)).toBe(true);
    expect(coincide(luis, "01/10/2026", hoy)).toBe(true);
    expect(coincide(maria, "13 oct", hoy)).toBe(false);
  });

  it("entiende «hoy» y «ayer»", () => {
    expect(coincide(juan, "hoy", hoy)).toBe(true);
    expect(coincide(maria, "Ayer", hoy)).toBe(true);
    expect(coincide(luis, "hoy", hoy)).toBe(false);
  });

  it("con varias palabras, todas tienen que aparecer", () => {
    expect(coincide(juan, "juan 27abc", hoy)).toBe(true);
    expect(coincide(juan, "juan hoy", hoy)).toBe(true);
    expect(coincide(juan, "juan ayer", hoy)).toBe(false);
  });

  it("ignora los espacios de los extremos; vacío coincide con todo", () => {
    expect(coincide(juan, "  juan  ", hoy)).toBe(true);
    expect(coincide(juan, "   ", hoy)).toBe(true);
  });
});

describe("resaltado", () => {
  it("marca la coincidencia conservando el texto original con acentos", () => {
    expect(segmentar("María González Ruiz", ["maria"])).toEqual([
      { texto: "María", resaltado: true },
      { texto: " González Ruiz", resaltado: false },
    ]);
  });

  it("en la placa ignora los guiones", () => {
    expect(segmentar("27-ABC-4", ["27abc"], true)).toEqual([
      { texto: "27-ABC", resaltado: true },
      { texto: "-4", resaltado: false },
    ]);
  });

  it("no interpreta HTML: devuelve el texto tal cual", () => {
    const segs = segmentar("<b>Juan</b>", ["<b>"]);
    expect(segs.map((s) => s.texto).join("")).toBe("<b>Juan</b>");
    expect(segs[0]).toEqual({ texto: "<b>", resaltado: true });
  });
});
