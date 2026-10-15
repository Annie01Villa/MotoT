import { describe, expect, it, vi, beforeEach } from "vitest";
import { render, screen, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { LiquidacionesProvider } from "@/data/LiquidacionesProvider";
import { SesionProvider } from "@/lib/session";
import { AppShell } from "./shell/AppShell";
import { Historial } from "./liquidaciones/Historial";

// Navegación simulada: ruta y parámetros de búsqueda controlados por la prueba.
const nav = vi.hoisted(() => ({ pathname: "/liquidaciones", search: "", replace: vi.fn() }));
vi.mock("next/navigation", () => ({
  usePathname: () => nav.pathname,
  useSearchParams: () => new URLSearchParams(nav.search),
  useRouter: () => ({ replace: nav.replace, push: vi.fn(), back: vi.fn() }),
}));

beforeEach(() => {
  nav.pathname = "/liquidaciones";
  nav.search = "";
  nav.replace.mockReset();
});

function conProviders(ui: React.ReactNode, semilla?: Parameters<typeof LiquidacionesProvider>[0]["semilla"]) {
  return render(
    <SesionProvider>
      <LiquidacionesProvider semilla={semilla}>{ui}</LiquidacionesProvider>
    </SesionProvider>,
  );
}

describe("menú", () => {
  it("tiene las 5 opciones con Liquidaciones primero y marcada como activa", () => {
    conProviders(<AppShell>contenido</AppShell>);
    const menu = screen.getByRole("navigation", { name: "Menú" });
    const enlaces = within(menu).getAllByRole("link");
    expect(enlaces.map((a) => a.textContent)).toEqual([
      "Liquidaciones",
      "Motos",
      "Choferes",
      "Usuarios",
      "Financiamiento",
    ]);
    expect(enlaces.map((a) => a.getAttribute("href"))).toEqual([
      "/liquidaciones",
      "/motos",
      "/choferes",
      "/usuarios",
      "/financiamiento",
    ]);
    expect(enlaces[0]).toHaveAttribute("aria-current", "page");
    expect(enlaces.slice(1).every((a) => !a.hasAttribute("aria-current"))).toBe(true);
  });

  it("marca la opción de la ruta actual, también en subrutas", () => {
    nav.pathname = "/liquidaciones/liq-001";
    conProviders(<AppShell>contenido</AppShell>);
    const menu = screen.getByRole("navigation", { name: "Menú" });
    expect(within(menu).getByRole("link", { name: "Liquidaciones" })).toHaveAttribute("aria-current", "page");
  });

  it("en celular, Administración agrupa Usuarios y Financiamiento", () => {
    nav.pathname = "/financiamiento";
    conProviders(<AppShell>contenido</AppShell>);
    const barra = screen.getByRole("navigation", { name: "Menú principal" });
    const enlaces = within(barra).getAllByRole("link");
    expect(enlaces.map((a) => a.textContent)).toEqual(["Liquidaciones", "Motos", "Choferes", "Administración"]);
    expect(enlaces[3]).toHaveAttribute("aria-current", "page");
  });
});

describe("historial", () => {
  it("el botón X limpia la búsqueda y devuelve el foco al buscador", async () => {
    nav.search = "q=Juan";
    conProviders(<Historial />);
    const buscador = screen.getAllByRole("searchbox", { name: "Buscar liquidaciones" })[0];
    expect(buscador).toHaveValue("Juan");
    await userEvent.click(screen.getByRole("button", { name: "Borrar búsqueda" }));
    expect(buscador).toHaveValue("");
    expect(buscador).toHaveFocus();
    expect(nav.replace).toHaveBeenLastCalledWith("/liquidaciones", { scroll: false });
  });

  it("escribir en el buscador guarda la búsqueda en la URL", async () => {
    conProviders(<Historial />);
    await userEvent.type(screen.getByRole("searchbox", { name: "Buscar liquidaciones" }), "ju");
    expect(nav.replace).toHaveBeenLastCalledWith("/liquidaciones?q=ju", { scroll: false });
  });

  it("sin resultados muestra el mensaje con lo buscado", () => {
    nav.search = "q=Roberto";
    conProviders(<Historial />);
    expect(screen.getByText('No encontramos liquidaciones con "Roberto"')).toBeInTheDocument();
  });

  it("la lista vacía no muestra ni el buscador ni el botón flotante", () => {
    conProviders(<Historial />, []);
    expect(screen.getByText(/Todavía no hay liquidaciones/)).toBeInTheDocument();
    expect(screen.queryByRole("searchbox")).not.toBeInTheDocument();
    expect(document.querySelector(".fab")).toBeNull();
    // El único botón es el del centro.
    expect(screen.getAllByRole("button", { name: "Registrar liquidación" })).toHaveLength(1);
  });

  it("el resaltado no interpreta HTML", () => {
    nav.search = "q=" + encodeURIComponent("<b>");
    conProviders(<Historial />, [
      {
        id: "liq-x",
        fecha: "2026-10-13",
        creadaEn: "2026-10-13T18:00:00.000Z",
        motoId: "mot-1",
        choferId: "cho-1",
        montoCentavos: 100,
        nombre: "x",
        nombrePersonalizado: false,
      },
    ]);
    expect(document.querySelector("b")).toBeNull();
  });
});
