"use client";

import { useSyncExternalStore } from "react";

const CONSULTA = "(min-width: 768px)";

function suscribir(cb: () => void) {
  const mq = window.matchMedia(CONSULTA);
  mq.addEventListener("change", cb);
  return () => mq.removeEventListener("change", cb);
}

/** true en computadora (768 px o más). Decide entre menú desplegable y hoja que sube. */
export function useEsEscritorio(): boolean {
  return useSyncExternalStore(
    suscribir,
    () => window.matchMedia(CONSULTA).matches,
    () => false,
  );
}
