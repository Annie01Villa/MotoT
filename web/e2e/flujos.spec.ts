import { expect, test, type Page } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

// Reloj fijo: 13 oct 2026, 13:30 en México (después de los registros de prueba de ese día).
// Así «Hoy» y «Ayer» coinciden con los datos de prueba.
test.beforeEach(async ({ page }) => {
  await page.clock.setFixedTime(new Date("2026-10-13T19:30:00Z"));
});

const esCelular = (page: Page) => (page.viewportSize()?.width ?? 0) < 768;
const filas = (page: Page) => page.getByTestId("fila-liquidacion").filter({ visible: true });
const regresar = (page: Page) => page.locator("a.back").filter({ visible: true });
const grupo = (page: Page, nombre: string | RegExp) =>
  page.getByRole("region", { name: nombre }).filter({ visible: true });

async function sinViolacionesGraves(page: Page) {
  const { violations } = await new AxeBuilder({ page }).analyze();
  const graves = violations.filter((v) => v.impact === "critical" || v.impact === "serious");
  expect(graves, JSON.stringify(graves.map((v) => ({ id: v.id, nodos: v.nodes.map((n) => n.target) })), null, 2)).toEqual(
    [],
  );
}

async function abrirRegistrar(page: Page) {
  await page.getByRole("button", { name: "Registrar liquidación" }).click();
  return page.getByRole("dialog", { name: "Registrar liquidación" });
}

async function elegirMoto(page: Page, placa: string) {
  await page.getByRole("button", { name: /^Moto/ }).click();
  await page.getByRole("option", { name: new RegExp(placa) }).click();
}

test("/ lleva a Liquidaciones, marcada en el menú", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveURL(/\/liquidaciones$/);
  await expect(page.getByRole("heading", { level: 1, name: "Liquidaciones" })).toBeVisible();
  const menu = page.getByRole("navigation", { name: esCelular(page) ? "Menú principal" : "Menú" });
  await expect(menu.getByRole("link", { name: "Liquidaciones" })).toHaveAttribute("aria-current", "page");
  await expect(grupo(page, "Hoy · 13 oct 2026")).toBeVisible();
  await expect(grupo(page, "Ayer · 12 oct 2026")).toBeVisible();
  await sinViolacionesGraves(page);
});

test("menú: cada opción llega a su pantalla con un clic", async ({ page }) => {
  await page.goto("/liquidaciones");
  if (esCelular(page)) {
    const barra = page.getByRole("navigation", { name: "Menú principal" });
    for (const [opcion, ruta] of [
      ["Motos", "/motos"],
      ["Choferes", "/choferes"],
      ["Administración", "/usuarios"],
      ["Liquidaciones", "/liquidaciones"],
    ]) {
      await barra.getByRole("link", { name: opcion }).click();
      await expect(page).toHaveURL(new RegExp(`${ruta}$`));
      await expect(barra.getByRole("link", { name: opcion })).toHaveAttribute("aria-current", "page");
    }
  } else {
    const menu = page.getByRole("navigation", { name: "Menú" });
    for (const [opcion, ruta] of [
      ["Motos", "/motos"],
      ["Choferes", "/choferes"],
      ["Usuarios", "/usuarios"],
      ["Financiamiento", "/financiamiento"],
      ["Liquidaciones", "/liquidaciones"],
    ]) {
      await menu.getByRole("link", { name: opcion }).click();
      await expect(page).toHaveURL(new RegExp(`${ruta}$`));
      await expect(menu.getByRole("link", { name: opcion })).toHaveAttribute("aria-current", "page");
    }
  }
});

test("celular: Administración → pestaña Financiamiento → pestaña Usuarios", async ({ page }) => {
  test.skip(!esCelular(page), "Solo en celular");
  await page.goto("/liquidaciones");
  await page.getByRole("navigation", { name: "Menú principal" }).getByRole("link", { name: "Administración" }).click();
  const pestanas = page.getByRole("navigation", { name: "Administración" });
  await expect(pestanas.getByRole("link", { name: "Usuarios" })).toHaveAttribute("aria-current", "page");
  await pestanas.getByRole("link", { name: "Financiamiento" }).click();
  await expect(page).toHaveURL(/\/financiamiento$/);
  await expect(pestanas.getByRole("link", { name: "Financiamiento" })).toHaveAttribute("aria-current", "page");
  await expect(
    page.getByRole("navigation", { name: "Menú principal" }).getByRole("link", { name: "Administración" }),
  ).toHaveAttribute("aria-current", "page");
  await pestanas.getByRole("link", { name: "Usuarios" }).click();
  await expect(page).toHaveURL(/\/usuarios$/);
  await sinViolacionesGraves(page);
});

test("registrar: aparece «Nueva»; al ir a Motos y regresar, la fila sigue sin la etiqueta", async ({ page }) => {
  await page.goto("/liquidaciones");
  const panel = await abrirRegistrar(page);
  await expect(panel.getByRole("button", { name: /^Moto/ })).toBeFocused();
  await elegirMoto(page, "12-MNO-5");
  await expect(panel.getByRole("button", { name: /^Chofer/ })).toContainText("Luis Hernández Soto");
  await expect(panel.getByLabel("Nombre")).toHaveValue("12-MNO-5 · 13 oct 2026");
  await panel.getByLabel("Monto").fill("425.50");
  await sinViolacionesGraves(page);
  await panel.getByRole("button", { name: "Guardar liquidación" }).click();

  await expect(panel).toBeHidden();
  await expect(page.getByRole("status")).toContainText("Liquidación registrada · $425.50");
  await expect(filas(page)).toHaveCount(5);
  const primera = grupo(page, "Hoy · 13 oct 2026").getByTestId("fila-liquidacion").first();
  await expect(primera).toContainText("12-MNO-5");
  await expect(primera).toContainText("Nueva");
  await sinViolacionesGraves(page);

  const menu = page.getByRole("navigation", { name: esCelular(page) ? "Menú principal" : "Menú" });
  await menu.getByRole("link", { name: "Motos" }).click();
  await expect(page).toHaveURL(/\/motos$/);
  await menu.getByRole("link", { name: "Liquidaciones" }).click();
  await expect(filas(page)).toHaveCount(5);
  await expect(filas(page).first()).toContainText("12-MNO-5");
  await expect(page.getByText("Nueva")).toHaveCount(0);
});

test("registrar sin datos muestra los errores", async ({ page }) => {
  await page.goto("/liquidaciones");
  const panel = await abrirRegistrar(page);
  await panel.getByRole("button", { name: "Guardar liquidación" }).click();
  await expect(panel.getByText("Elige la moto", { exact: true }).last()).toBeVisible();
  await expect(panel.getByText("Escribe el monto en pesos")).toBeVisible();
  await expect(panel.getByRole("button", { name: /^Moto/ })).toBeFocused();
  await panel.getByLabel("Monto").fill("0");
  await expect(panel.getByText("El monto debe ser mayor que $0")).toBeVisible();
  await sinViolacionesGraves(page);
});

test("moto sin chofer: se elige de la lista de todos los choferes", async ({ page }) => {
  await page.goto("/liquidaciones");
  const panel = await abrirRegistrar(page);
  await elegirMoto(page, "45-PQR-2");
  await expect(panel.getByText("45-PQR-2 no tiene chofer. Elige quién la trae.")).toBeVisible();
  await panel.getByRole("button", { name: /^Chofer/ }).click();
  const opciones = page.getByRole("listbox", { name: "Choferes" }).getByRole("option");
  await expect(opciones).toHaveCount(4);
  await expect(opciones.first()).toContainText("Carlos Ramírez Díaz");
  await expect(opciones.first()).toContainText("Sin moto");
  await sinViolacionesGraves(page);
  await opciones.first().click();
  await expect(panel.getByRole("button", { name: /^Chofer/ })).toContainText("Carlos Ramírez Díaz");
});

test("corregir la fecha a ayer mueve la liquidación al grupo «Ayer»", async ({ page }) => {
  await page.goto("/liquidaciones/liq-002");
  await expect(page.getByRole("heading", { level: 1, name: "$350.00" })).toBeVisible();
  await sinViolacionesGraves(page);
  await page.getByRole("button", { name: "Corregir" }).click();
  const panel = page.getByRole("dialog", { name: "Corregir liquidación" });
  await expect(panel.getByLabel("Monto")).toHaveValue("350.00");
  await panel.getByRole("button", { name: /^Fecha/ }).click();
  await sinViolacionesGraves(page);
  await page.getByRole("button", { name: /12 de octubre/ }).click();
  await expect(panel.getByRole("button", { name: /^Fecha/ })).toContainText("Ayer · 12 oct 2026");
  // Sin editar el nombre, se recalcula con la fecha nueva.
  await expect(panel.getByLabel("Nombre")).toHaveValue("31-XKT-8 · 12 oct 2026");
  await panel.getByRole("button", { name: "Guardar cambios" }).click();
  await expect(panel).toBeHidden();
  await expect(page.getByText("12 oct 2026").filter({ visible: true }).first()).toBeVisible();

  await regresar(page).click();
  await expect(grupo(page, "Hoy · 13 oct 2026").getByTestId("fila-liquidacion")).toHaveCount(1);
  const ayer = grupo(page, "Ayer · 12 oct 2026").getByTestId("fila-liquidacion");
  await expect(ayer).toHaveCount(3);
  await expect(ayer.first()).toContainText("31-XKT-8");
});

test("buscar, abrir un detalle y regresar conserva la búsqueda", async ({ page }) => {
  await page.goto("/liquidaciones");
  await page.getByRole("searchbox", { name: "Buscar liquidaciones" }).fill("Juan");
  await expect(page).toHaveURL(/\?q=Juan$/);
  await expect(filas(page)).toHaveCount(2);
  await expect(page.locator("mark.hl").filter({ visible: true }).first()).toHaveText("Juan");
  await sinViolacionesGraves(page);

  await filas(page).first().click();
  await expect(page).toHaveURL(/\/liquidaciones\/liq-001\?q=Juan$/);
  await regresar(page).click();
  await expect(page).toHaveURL(/\/liquidaciones\?q=Juan$/);
  await expect(page.getByRole("searchbox", { name: "Buscar liquidaciones" })).toHaveValue("Juan");
  await expect(filas(page)).toHaveCount(2);

  await page.getByRole("button", { name: "Borrar búsqueda" }).click();
  await expect(page.getByRole("searchbox", { name: "Buscar liquidaciones" })).toHaveValue("");
  await expect(page.getByRole("searchbox", { name: "Buscar liquidaciones" })).toBeFocused();
  await expect(filas(page)).toHaveCount(4);
});

test("sin resultados", async ({ page }) => {
  await page.goto("/liquidaciones?q=Roberto");
  await expect(page.getByText('No encontramos liquidaciones con "Roberto"')).toBeVisible();
  await sinViolacionesGraves(page);
});

test("teclado: el panel atrapa el foco, Escape lo cierra y el foco regresa", async ({ page }) => {
  await page.goto("/liquidaciones");
  const abrir = page.getByRole("button", { name: "Registrar liquidación" });
  await abrir.focus();
  await page.keyboard.press("Enter");
  const panel = page.getByRole("dialog", { name: "Registrar liquidación" });
  await expect(panel).toBeVisible();
  for (let i = 0; i < 12; i++) {
    await page.keyboard.press("Tab");
    expect(await panel.evaluate((el) => el.contains(document.activeElement))).toBe(true);
  }
  await page.keyboard.press("Escape");
  await expect(panel).toBeHidden();
  await expect(abrir).toBeFocused();
});

test("teclado: el selector de moto se recorre con flechas y Enter; Escape regresa al campo", async ({ page }) => {
  await page.goto("/liquidaciones");
  const panel = await abrirRegistrar(page);
  const campoMoto = panel.getByRole("button", { name: /^Moto/ });
  await page.keyboard.press("Enter");
  const buscador = page.getByRole("combobox", { name: "Buscar moto por placa" });
  await expect(buscador).toBeFocused();
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("Enter");
  await expect(campoMoto).toContainText("31-XKT-8");
  await expect(campoMoto).toBeFocused();

  await page.keyboard.press("Enter");
  await expect(buscador).toBeFocused();
  await page.keyboard.press("Escape");
  await expect(buscador).toBeHidden();
  await expect(panel).toBeVisible();
  await expect(campoMoto).toBeFocused();
});

test("producción: el selector de sesión no existe", async ({ page }) => {
  await page.goto("/liquidaciones");
  await expect(page.getByRole("heading", { level: 1, name: "Liquidaciones" })).toBeVisible();
  await expect(page.getByTestId("selector-sesion")).toHaveCount(0);
});

async function focoQuedaDentro(page: Page, nombre: string) {
  const contenedor = page.getByRole("dialog", { name: nombre });
  await expect(contenedor).toBeVisible();
  // Modal: el resto del formulario queda fuera de alcance (oculto para lectores de pantalla).
  await expect(page.getByRole("textbox", { name: "Monto" })).toHaveCount(0);
  for (const tecla of ["Tab", "Tab", "Tab", "Tab", "Shift+Tab", "Shift+Tab", "Shift+Tab", "Shift+Tab", "Shift+Tab"]) {
    await page.keyboard.press(tecla);
    expect(await contenedor.evaluate((el) => el.contains(document.activeElement)), `${nombre}: ${tecla}`).toBe(true);
  }
}

test("teclado: Tab y Shift+Tab no salen del selector de moto ni del calendario", async ({ page }) => {
  await page.goto("/liquidaciones");
  const panel = await abrirRegistrar(page);

  await panel.getByRole("button", { name: /^Moto/ }).click();
  await focoQuedaDentro(page, "Elige la moto");
  await page.keyboard.press("Escape");
  await expect(panel.getByRole("button", { name: /^Moto/ })).toBeFocused();

  await panel.getByRole("button", { name: /^Fecha/ }).click();
  await focoQuedaDentro(page, "Elige la fecha");
  await page.keyboard.press("Escape");
  await expect(panel.getByRole("button", { name: /^Fecha/ })).toBeFocused();
  await expect(panel).toBeVisible();
  await expect(page.getByRole("textbox", { name: "Monto" })).toHaveCount(1);
});
