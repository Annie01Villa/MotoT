"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { PESTANAS_ADMINISTRACION, rutaActiva } from "@/lib/nav";
import { BarraSuperior } from "./BarraSuperior";

/** Página provisional: la pantalla se construye en su propia tarea. */
export function Provisional({ titulo, administracion = false }: { titulo: string; administracion?: boolean }) {
  const pathname = usePathname();
  return (
    <>
      <BarraSuperior>
        <h1 className="t-scr">{administracion ? "Administración" : titulo}</h1>
      </BarraSuperior>
      {administracion && (
        <div className="solo-cel">
          <nav className="tabs" aria-label="Administración">
            {PESTANAS_ADMINISTRACION.map((p) => (
              <Link key={p.id} href={p.href} aria-current={rutaActiva(pathname, p.href) ? "page" : undefined}>
                {p.nombre}
              </Link>
            ))}
          </nav>
        </div>
      )}
      <main className="flex flex-col gap-4 p-4 md:p-8">
        <div className="solo-pc">
          <h1 className="t-scr-pc">{titulo}</h1>
        </div>
        {administracion && <h2 className="solo-cel t-sub">{titulo}</h2>}
        <p className="t-sec">Esta pantalla se construye en su propia tarea.</p>
      </main>
    </>
  );
}
