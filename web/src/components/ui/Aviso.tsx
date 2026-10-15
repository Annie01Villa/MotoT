"use client";

import { CircleCheck, X } from "lucide-react";

/** Aviso temporal de éxito: abajo en celular (sin botón de cerrar), arriba a la derecha en computadora. */
export function Aviso({ mensaje, onCerrar }: { mensaje: string; onCerrar: () => void }) {
  return (
    <div className="toast" role="status">
      <CircleCheck size={24} aria-hidden="true" />
      <span className="num flex-1">{mensaje}</span>
      <span className="solo-pc">
        <button type="button" className="btn btn-ico" aria-label="Cerrar aviso" onClick={onCerrar}>
          <X size={24} aria-hidden="true" />
        </button>
      </span>
    </div>
  );
}
