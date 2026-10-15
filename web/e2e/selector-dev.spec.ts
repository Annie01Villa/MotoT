import { expect, test } from "@playwright/test";

// Control de la prueba de producción: en `next dev` el selector sí aparece.
test("desarrollo: el selector de sesión aparece", async ({ page }) => {
  await page.goto("/liquidaciones");
  await expect(page.getByTestId("selector-sesion")).toBeVisible();
});
