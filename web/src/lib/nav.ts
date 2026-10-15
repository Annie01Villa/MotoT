import { Bike, Landmark, Receipt, Settings, User, Users, type LucideIcon } from "lucide-react";

export type OpcionMenu = {
  id: "liquidaciones" | "motos" | "choferes" | "usuarios" | "financiamiento";
  nombre: string;
  href: string;
  icono: LucideIcon;
  seccion: "Operación" | "Administración";
};

/** Lista única del menú. Liquidaciones va primero: es la pantalla de inicio. */
export const MENU: OpcionMenu[] = [
  { id: "liquidaciones", nombre: "Liquidaciones", href: "/liquidaciones", icono: Receipt, seccion: "Operación" },
  { id: "motos", nombre: "Motos", href: "/motos", icono: Bike, seccion: "Operación" },
  { id: "choferes", nombre: "Choferes", href: "/choferes", icono: User, seccion: "Operación" },
  { id: "usuarios", nombre: "Usuarios", href: "/usuarios", icono: Users, seccion: "Administración" },
  { id: "financiamiento", nombre: "Financiamiento", href: "/financiamiento", icono: Landmark, seccion: "Administración" },
];

export const SECCIONES = ["Operación", "Administración"] as const;

/** Barra inferior del celular: 4 botones; Usuarios y Financiamiento quedan dentro de Administración. */
export const MENU_CELULAR = [
  ...MENU.filter((o) => o.seccion === "Operación").map((o) => ({ ...o, rutas: [o.href] })),
  {
    id: "administracion" as const,
    nombre: "Administración",
    href: "/usuarios",
    icono: Settings,
    rutas: MENU.filter((o) => o.seccion === "Administración").map((o) => o.href),
  },
];

export const PESTANAS_ADMINISTRACION = MENU.filter((o) => o.seccion === "Administración");

export function rutaActiva(pathname: string, href: string): boolean {
  return pathname === href || pathname.startsWith(`${href}/`);
}
