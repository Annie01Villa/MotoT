// Los montos se guardan en centavos enteros. La conversión se hace con texto
// y enteros, nunca con parseFloat, para no arrastrar errores de punto flotante.

export type ErrorMonto = "vacio" | "cero" | "decimales" | "invalido";

export const MENSAJES_MONTO: Record<ErrorMonto, string> = {
  vacio: "Escribe el monto en pesos",
  cero: "El monto debe ser mayor que $0",
  decimales: "Escribe el monto con máximo 2 decimales",
  invalido: "Escribe solo números",
};

export type ResultadoMonto = { ok: true; centavos: number } | { ok: false; error: ErrorMonto };

// 9 dígitos enteros: límite técnico contra desbordes, no un tope de negocio.
const FORMATO = /^\d{1,9}(\.\d{1,2})?$/;
const DEMASIADOS_DECIMALES = /^\d{1,9}\.\d{3,}$/;

export function leerMonto(texto: string): ResultadoMonto {
  const limpio = texto.trim().replace(/,/g, "");
  if (limpio === "") return { ok: false, error: "vacio" };
  if (DEMASIADOS_DECIMALES.test(limpio)) return { ok: false, error: "decimales" };
  if (!FORMATO.test(limpio)) return { ok: false, error: "invalido" };

  const [pesos, decimales = ""] = limpio.split(".");
  const centavos = Number(pesos) * 100 + Number(decimales.padEnd(2, "0"));
  if (centavos === 0) return { ok: false, error: "cero" };
  return { ok: true, centavos };
}

function partes(centavos: number): { pesos: string; cent: string } {
  const pesos = Math.floor(centavos / 100);
  return { pesos: String(pesos), cent: String(centavos % 100).padStart(2, "0") };
}

/** "$1,500.00" */
export function formatMonto(centavos: number): string {
  const { pesos, cent } = partes(centavos);
  return `$${pesos.replace(/\B(?=(\d{3})+(?!\d))/g, ",")}.${cent}`;
}

/** "1500.00": valor del campo al abrir Corregir. */
export function montoParaCampo(centavos: number): string {
  const { pesos, cent } = partes(centavos);
  return `${pesos}.${cent}`;
}
