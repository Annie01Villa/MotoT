const DIACRITICOS = /\p{Diacritic}/gu;

/** Minúsculas y sin acentos: «María» → «maria». */
export function normalizar(texto: string): string {
  return texto.normalize("NFD").replace(DIACRITICOS, "").toLowerCase();
}

/** Quita guiones y espacios: «27-ABC-4» → «27ABC4». */
export function sinSeparadores(texto: string): string {
  return texto.replace(/[-\s]/g, "");
}
