// Copia public/ y .next/static/ dentro de .next/standalone para que server.js los sirva.
// Lo mismo que hace el Dockerfile; sirve para correr la versión de producción en local y en las pruebas.
import { cpSync, existsSync } from "node:fs";

const destino = ".next/standalone";
if (!existsSync(destino)) {
  console.error("Falta .next/standalone: corre `npm run build` primero.");
  process.exit(1);
}
cpSync("public", `${destino}/public`, { recursive: true });
cpSync(".next/static", `${destino}/.next/static`, { recursive: true });
