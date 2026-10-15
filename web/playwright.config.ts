import { defineConfig, devices } from "@playwright/test";

const PROD = "http://127.0.0.1:3200";
const DEV = "http://localhost:3100";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  retries: 0,
  reporter: [["list"]],
  use: { trace: "retain-on-failure", locale: "es-MX", timezoneId: "America/Mexico_City" },
  projects: [
    // Flujos principales contra la compilación de producción, en los dos tamaños del diseño.
    {
      name: "celular",
      testIgnore: /selector-dev/,
      use: { ...devices["Desktop Chrome"], baseURL: PROD, viewport: { width: 390, height: 844 }, isMobile: false },
    },
    {
      name: "computadora",
      testIgnore: /selector-dev/,
      use: { ...devices["Desktop Chrome"], baseURL: PROD, viewport: { width: 1440, height: 900 } },
    },
    // Control: en `next dev` el selector de sesión sí aparece.
    {
      name: "dev",
      testMatch: /selector-dev/,
      use: { ...devices["Desktop Chrome"], baseURL: DEV, viewport: { width: 1440, height: 900 } },
    },
  ],
  webServer: [
    {
      // Igual que en Railway: servidor mínimo de .next/standalone.
      command: "npm run build && npm run start",
      url: `${PROD}/liquidaciones`,
      env: { PORT: "3200", HOSTNAME: "127.0.0.1" },
      reuseExistingServer: false,
      timeout: 300_000,
    },
    {
      // Carpeta propia para no chocar con la compilación de producción.
      command: "npx next dev -p 3100",
      url: `${DEV}/liquidaciones`,
      env: { NEXT_DIST_DIR: ".next-dev" },
      reuseExistingServer: false,
      timeout: 300_000,
    },
  ],
});
