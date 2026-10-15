import path from "node:path";
import type { NextConfig } from "next";

// La raíz es esta carpeta (web/): la compilación no depende de lo que haya en carpetas superiores.
const RAIZ = path.join(__dirname);

const nextConfig: NextConfig = {
  // Railway: la imagen Docker solo copia el servidor mínimo (.next/standalone).
  output: "standalone",
  poweredByHeader: false,
  outputFileTracingRoot: RAIZ,
  // Las pruebas e2e levantan `next dev` y `next start` a la vez; cada uno usa su carpeta.
  distDir: process.env.NEXT_DIST_DIR || ".next",
  turbopack: {
    root: RAIZ,
    rules: {
      "*.css": {
        loaders: ["@tailwindcss/turbopack"],
        as: "*.css",
      },
    },
  },
};

export default nextConfig;
