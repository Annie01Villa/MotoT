import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Railway: la imagen Docker solo copia el servidor mínimo (.next/standalone).
  output: "standalone",
  poweredByHeader: false,
  // Las pruebas e2e levantan `next dev` y `next start` a la vez; cada uno usa su carpeta.
  distDir: process.env.NEXT_DIST_DIR || ".next",
  turbopack: {
    rules: {
      "*.css": {
        loaders: ["@tailwindcss/turbopack"],
        as: "*.css",
      },
    },
  },
};

export default nextConfig;
