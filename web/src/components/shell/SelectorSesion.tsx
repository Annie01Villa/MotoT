"use client";

import { MOSTRAR_SELECTOR_SESION, USUARIOS_PRUEBA, useSesion } from "@/lib/session";

/** Solo en desarrollo: cambia entre Pedro (Ayudante) y Laura (Gerente). */
export function SelectorSesion() {
  const { usuario, cambiar } = useSesion();
  if (!MOSTRAR_SELECTOR_SESION) return null;
  return (
    <div
      data-testid="selector-sesion"
      className="fixed top-2 right-2 z-[80] rounded-lg border border-borde bg-white px-2 py-1 text-xs shadow"
    >
      <label className="flex items-center gap-1">
        Sesión de prueba
        <select
          className="rounded border border-borde px-1"
          value={usuario.nombre}
          onChange={(e) => cambiar(USUARIOS_PRUEBA.find((u) => u.nombre === e.target.value) ?? USUARIOS_PRUEBA[0])}
        >
          {USUARIOS_PRUEBA.map((u) => (
            <option key={u.nombre} value={u.nombre}>
              {u.nombre} · {u.rol}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
}
