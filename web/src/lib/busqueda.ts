// Búsqueda de liquidaciones: sin distinguir mayúsculas ni acentos; si hay
// varias palabras, todas tienen que aparecer en el registro (en cualquier campo).
import { diaRelativo, formatFecha, formatFechaNumerica, partesDeFecha } from "./fechas";
import { normalizar, sinSeparadores } from "./texto";

export function palabrasDeBusqueda(q: string): string[] {
  return normalizar(q).trim().split(/\s+/).filter(Boolean);
}

export type CamposBuscables = { placa: string; chofer: string; fecha: string };

function textosDeFecha(fecha: string, hoy: string): string[] {
  const { anio, mes, dia } = partesDeFecha(fecha);
  const textos = [normalizar(formatFecha(fecha)), formatFechaNumerica(fecha), `${dia}/${mes}/${anio}`];
  const rel = diaRelativo(fecha, hoy);
  if (rel) textos.push(normalizar(rel));
  return textos;
}

function palabraCoincide(palabra: string, c: CamposBuscables, hoy: string): boolean {
  const placaBuscada = sinSeparadores(palabra);
  if (placaBuscada && sinSeparadores(normalizar(c.placa)).includes(placaBuscada)) return true;
  if (normalizar(c.chofer).includes(palabra)) return true;
  return textosDeFecha(c.fecha, hoy).some((t) => t.includes(palabra));
}

export function coincide(c: CamposBuscables, q: string, hoy: string): boolean {
  const palabras = palabrasDeBusqueda(q);
  return palabras.every((p) => palabraCoincide(p, c, hoy));
}

export type Segmento = { texto: string; resaltado: boolean };

/**
 * Parte un texto en segmentos resaltados / no resaltados según las palabras buscadas.
 * Devuelve texto plano: quien lo pinta lo hace con nodos de React, nunca como HTML.
 * Con `ignorarSeparadores`, «27abc» resalta «27-ABC» en la placa.
 */
export function segmentar(texto: string, palabras: string[], ignorarSeparadores = false): Segmento[] {
  // Texto normalizado carácter por carácter, guardando a qué posición original corresponde.
  let norm = "";
  const origen: number[] = [];
  Array.from(texto).forEach((ch, i) => {
    if (ignorarSeparadores && /[-\s]/.test(ch)) return;
    for (const n of normalizar(ch)) {
      norm += n;
      origen.push(i);
    }
  });

  const chars = Array.from(texto);
  const marcado = new Array<boolean>(chars.length).fill(false);
  for (const palabra of palabras) {
    const buscada = ignorarSeparadores ? sinSeparadores(palabra) : palabra;
    if (!buscada) continue;
    let desde = norm.indexOf(buscada);
    while (desde !== -1) {
      const ini = origen[desde];
      const fin = origen[desde + buscada.length - 1];
      for (let i = ini; i <= fin; i++) marcado[i] = true;
      desde = norm.indexOf(buscada, desde + 1);
    }
  }

  const segmentos: Segmento[] = [];
  chars.forEach((ch, i) => {
    const ultimo = segmentos[segmentos.length - 1];
    if (ultimo && ultimo.resaltado === marcado[i]) ultimo.texto += ch;
    else segmentos.push({ texto: ch, resaltado: marcado[i] });
  });
  return segmentos;
}
