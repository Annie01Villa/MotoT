// Las fechas de negocio son días de calendario en México ("YYYY-MM-DD"),
// nunca instantes: no pasan por toISOString() ni por conversiones a UTC.

export const ZONA_NEGOCIO = "America/Mexico_City";

const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];

const partesMx = new Intl.DateTimeFormat("es-MX", {
  timeZone: ZONA_NEGOCIO,
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

function dosDigitos(n: number): string {
  return String(n).padStart(2, "0");
}

export function fechaDePartes(anio: number, mes: number, dia: number): string {
  return `${anio}-${dosDigitos(mes)}-${dosDigitos(dia)}`;
}

export function partesDeFecha(fecha: string): { anio: number; mes: number; dia: number } {
  const [anio, mes, dia] = fecha.split("-").map(Number);
  return { anio, mes, dia };
}

/** Día de calendario en México para un instante dado. */
export function fechaMx(instante: Date): string {
  const p = Object.fromEntries(partesMx.formatToParts(instante).map((x) => [x.type, x.value]));
  return fechaDePartes(Number(p.year), Number(p.month), Number(p.day));
}

/** Suma días a una fecha de calendario (aritmética de calendario, sin zona horaria). */
export function sumarDias(fecha: string, dias: number): string {
  const { anio, mes, dia } = partesDeFecha(fecha);
  const d = new Date(Date.UTC(anio, mes - 1, dia + dias));
  return fechaDePartes(d.getUTCFullYear(), d.getUTCMonth() + 1, d.getUTCDate());
}

/** "13 oct 2026" */
export function formatFecha(fecha: string): string {
  const { anio, mes, dia } = partesDeFecha(fecha);
  return `${dia} ${MESES[mes - 1]} ${anio}`;
}

/** "13/10/2026" */
export function formatFechaNumerica(fecha: string): string {
  const { anio, mes, dia } = partesDeFecha(fecha);
  return `${dosDigitos(dia)}/${dosDigitos(mes)}/${anio}`;
}

/** "Hoy", "Ayer" o null, comparando fechas de calendario. */
export function diaRelativo(fecha: string, hoy: string): "Hoy" | "Ayer" | null {
  if (fecha === hoy) return "Hoy";
  if (fecha === sumarDias(hoy, -1)) return "Ayer";
  return null;
}

/** "Hoy · 13 oct 2026", "Ayer · 12 oct 2026" o "10 oct 2026". */
export function etiquetaDia(fecha: string, hoy: string): string {
  const rel = diaRelativo(fecha, hoy);
  return rel ? `${rel} · ${formatFecha(fecha)}` : formatFecha(fecha);
}

/** Fecha elegida en el calendario (Date local) → fecha de calendario, por sus partes. */
export function fechaDeDateLocal(d: Date): string {
  return fechaDePartes(d.getFullYear(), d.getMonth() + 1, d.getDate());
}

/** Fecha de calendario → Date local a medianoche, solo para mostrarla en el calendario. */
export function dateLocalDeFecha(fecha: string): Date {
  const { anio, mes, dia } = partesDeFecha(fecha);
  return new Date(anio, mes - 1, dia);
}
