# CRM-MotoT · web

Maqueta funcional de la **pantalla principal (Liquidaciones)** y el **menú** (ANN-143 y ANN-145), con datos de prueba.
No hay login real, base de datos ni permisos en servidor: los registros viven en memoria y se reinician al recargar.

## Requisitos

- Node.js 24 o más reciente.

## Comandos

```bash
npm install
npx playwright install chromium   # solo la primera vez, para las pruebas e2e

npm run dev         # http://localhost:3000 (incluye el selector de sesión de prueba)
npm run build && npm run start   # versión de producción

npm run lint        # ESLint (incluye react/no-danger)
npm run test        # Vitest: lógica y componentes
npm run test:e2e    # Playwright a 390 px y 1440 px, con axe; levanta solo sus servidores (puertos 3100 y 3200)
```

No se necesitan variables de entorno. `NEXT_DIST_DIR` solo la usan las pruebas e2e, para que `next dev` y `next start` no compartan carpeta.

## Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Rutas | `src/app/` (`/` lleva a `/liquidaciones`) |
| Menú | `src/lib/nav.ts`, `src/components/shell/AppShell.tsx` |
| Historial, buscador, detalle y formulario | `src/components/liquidaciones/` |
| Modelo y repositorio en memoria | `src/data/` |
| Fechas (México), montos (centavos), búsqueda, reglas del formulario | `src/lib/` |
| Pruebas e2e | `e2e/` |

Fuente visual: `CRM-MotoT-design/.../04-pantallas/liquidaciones/*.dc.html`.
