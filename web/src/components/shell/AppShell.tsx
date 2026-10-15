"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Bike, LogOut } from "lucide-react";
import { MENU, MENU_CELULAR, rutaActiva, SECCIONES } from "@/lib/nav";
import { useSesion } from "@/lib/session";
import { SelectorSesion } from "./SelectorSesion";

function MenuLateral({ pathname }: { pathname: string }) {
  const { usuario } = useSesion();
  return (
    <aside className="side">
      <div className="logo">
        <Bike size={24} strokeWidth={2} aria-hidden="true" />
        CRM-MotoT
      </div>
      <nav aria-label="Menú" className="flex flex-col gap-1">
        {SECCIONES.map((seccion) => (
          <div key={seccion} className="flex flex-col gap-1">
            <p className="nav-t">{seccion}</p>
            {MENU.filter((o) => o.seccion === seccion).map((o) => {
              const Icono = o.icono;
              return (
                <Link
                  key={o.id}
                  href={o.href}
                  className="nav-i"
                  aria-current={rutaActiva(pathname, o.href) ? "page" : undefined}
                >
                  <Icono size={24} strokeWidth={2} aria-hidden="true" />
                  {o.nombre}
                </Link>
              );
            })}
          </div>
        ))}
      </nav>
      <div className="mt-auto flex flex-col gap-2 border-t border-borde pt-4">
        <div className="flex flex-col items-start gap-1 px-3">
          <span className="font-semibold">{usuario.nombre}</span>
          <span className={`tag ${usuario.rol === "Gerente" ? "tag-ger" : "tag-ayu"}`}>{usuario.rol}</span>
        </div>
        <Link href="/login" className="nav-i">
          <LogOut size={24} strokeWidth={2} aria-hidden="true" />
          Cerrar sesión
        </Link>
      </div>
    </aside>
  );
}

function BarraInferior({ pathname }: { pathname: string }) {
  return (
    <nav className="bnav" aria-label="Menú principal">
      {MENU_CELULAR.map((o) => {
        const Icono = o.icono;
        const activa = o.rutas.some((r) => rutaActiva(pathname, r));
        return (
          <Link key={o.id} href={o.href} aria-current={activa ? "page" : undefined}>
            <Icono size={24} strokeWidth={2} aria-hidden="true" />
            {o.nombre}
          </Link>
        );
      })}
    </nav>
  );
}

/** Menú siempre visible: lateral en computadora, barra inferior en celular. */
export function AppShell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  return (
    <div className="flex min-h-screen">
      <div className="solo-pc">
        <MenuLateral pathname={pathname} />
      </div>
      <div className="min-w-0 flex-1 pb-[72px] md:pb-0">{children}</div>
      <div className="solo-cel">
        <BarraInferior pathname={pathname} />
      </div>
      <SelectorSesion />
    </div>
  );
}
