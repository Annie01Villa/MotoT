# CRM-MotoT

Aplicación web para supervisar una flotilla de motos de trabajo y registrar rápido lo del día a día: qué chofer trae cada moto, las liquidaciones de cada chofer y los financiamientos. La contabilidad se lleva aparte.

- **Plan de trabajo:** [CRM-MotoT — MVP en Linear](https://linear.app/annie-villalobos/project/crm-motot-mvp-a201b3e2b6c4)
- **Resumen de la Fase 0 (diseño):** [`CRM motoT.md`](./CRM%20motoT.md)
- **Diseño (fuente visual):** [`CRM-MotoT-design/`](./CRM-MotoT-design)

## Estructura

| Carpeta / archivo | Qué es |
|---|---|
| `web/` | La app (Next.js). Ver [`web/README.md`](./web/README.md) para correrla y probarla. |
| `CRM-MotoT-design/` | Design system, componentes y pantallas de la Fase 0. |
| `Dockerfile`, `railway.json` | Despliegue en Railway. |
| `.github/workflows/ci.yml` | Revisiones automáticas en cada push y pull request. |

## Revisiones automáticas (CI)

En cada push a `main` y en cada pull request, GitHub Actions corre:

1. **Lint, tipos y pruebas unitarias** (ESLint, TypeScript, Vitest).
2. **Pruebas e2e** a 390 px y 1440 px, con revisión de accesibilidad (Playwright + axe).
3. **Imagen de Railway:** compila el `Dockerfile` y comprueba que la app arranca y responde.

## Despliegue en Railway

El servicio se crea desde este repositorio de GitHub y se publica solo con cada push a `main`.

- Railway usa el `Dockerfile` de la raíz (lo indica `railway.json`); no hay que configurar el directorio raíz ni los comandos.
- La app escucha en el puerto que Railway da en `PORT`.
- Revisión de salud: `/liquidaciones`.
- No necesita variables de entorno.
- Recomendado: en el servicio, activar **Wait for CI** para que solo publique cuando las revisiones de GitHub pasen.
