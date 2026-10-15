# Entrega a auditoría · Pantalla principal (Liquidaciones) + Menú

**Tareas:** ANN-143 (Historial de liquidaciones con buscador) y ANN-145 (Menú principal)
**Plan de referencia:** v4, con Go de auditoría para la maqueta funcional con datos de prueba
**Fecha:** 14 oct 2026
**Alcance:** maqueta funcional. No incluye login real, base de datos ni permisos en servidor; los registros viven en memoria y se reinician al recargar.

---

## 1. Ubicación y ejecución

| Dato | Valor |
|---|---|
| Repositorio | `github.com/Annie01Villa/orbita-crm` (privado), rama `main` |
| Carpeta del código | `web/` |
| Estado en git | Commits listos en local; se suben a GitHub cuando auditoría dé luz verde. El diff completo queda en el historial. |
| Requisitos | Node.js 24+ |
| Variables de entorno | Ninguna. `NEXT_DIST_DIR` solo la usan las pruebas e2e. No hay secretos. |
| Migraciones de base de datos | No aplica: no hay base de datos en este alcance. |

```bash
cd web
npm install
npx playwright install chromium   # solo la primera vez

npm run dev        # http://localhost:3000
npm run lint       # análisis estático (ESLint, incluye react/no-danger)
npx tsc --noEmit   # tipos
npm run test       # Vitest
npm run test:e2e   # Playwright a 390 y 1440 px + axe; levanta solo sus servidores
```

**Producción (Railway):** `Dockerfile` en la raíz con el servidor mínimo de Next.js (`output: "standalone"`), escucha en `PORT`, revisión de salud en `/liquidaciones`. Las pruebas e2e corren contra ese mismo servidor.

**CI (GitHub Actions):** lint, tipos y Vitest; Playwright + axe; compilación y arranque de la imagen Docker.

**Tecnología:** Next.js 16.4.1 (App Router), React 19.3, TypeScript, Tailwind 4, Radix UI (Dialog y Popover), react-day-picker 10 y lucide-react. Pruebas con Vitest 5, Testing Library, Playwright 1.64 y @axe-core/playwright.

## 2. Resultados

| Verificación | Resultado |
|---|---|
| ESLint | 0 errores, 0 avisos |
| TypeScript | sin errores |
| Vitest | **64/64** pruebas pasan (6 archivos) |
| Playwright | **24/24** pasan (celular, computadora y control en `next dev`); 1 omitida a propósito: la prueba de pestañas solo corre en celular |
| axe | 0 violaciones críticas o serias en historial, búsqueda, sin resultados, formulario, selectores, calendario, detalle y Administración |
| Revisión visual | capturas a 390 y 1440 px comparadas con los `.dc.html` de `04-pantallas/liquidaciones/` |

## 3. Cumplimiento del plan v4

| Punto del plan | Implementación | Prueba |
|---|---|---|
| **B1** Identidad: `id` que no cambia, `creadaEn`, `registrar` devuelve el `id`, `corregir(id)` | `src/data/types.ts`, `src/data/repo.ts`: los campos editables se copian uno por uno, así que `corregir` no puede cambiar `id` ni `creadaEn` aunque vengan en los datos | `repo.test.ts` («identidad», incluido «ignora id y creadaEn aunque vengan en los cambios») |
| Orden siempre igual | `compararLiquidaciones`: fecha ↓, creadaEn ↓, id | `repo.test.ts` («orden y agrupado») |
| Reloj que se puede reemplazar | `src/lib/clock.ts`; reloj fijo con `vi.useFakeTimers` y `page.clock.setFixedTime` | todas las pruebas de fechas y e2e |
| **B2** Monto en centavos enteros, mayor que 0, máximo 2 decimales | `src/lib/monto.ts`: expresión regular `^\d{1,9}(\.\d{1,2})?$` y conversión con texto y enteros, sin `parseFloat` | `monto.test.ts`: 350, 350.5, 1,500.00 ✓ · vacío, 0, 0.00, -5, 350.505, abc, NaN ✗ · 0.1 + 0.2 = 30 centavos |
| **B3** Fecha de calendario de México | `src/lib/fechas.ts`: `formatToParts` con `America/Mexico_City`; «Ayer» por aritmética de calendario; el calendario convierte por partes | `fechas.test.ts`: medianoche (`2026-10-14T05:30Z` → 13 oct), cambio de mes y de año |
| **v4** `nombrePersonalizado` | `src/lib/formulario.ts`: se activa al escribir, aunque quede el mismo texto; se guarda y se carga al corregir; nunca se compara texto | `formulario.test.ts`: los 4 casos del plan, incluido registrar → corregir → cambiar moto y fecha → el nombre se conserva |
| Chofer al cambiar la moto; lista de choferes | reducer en `formulario.ts`; todos los choferes en orden alfabético, cada uno con su placa o «Sin moto» | `formulario.test.ts`; e2e «moto sin chofer» |
| Búsqueda: sin mayúsculas ni acentos, placa con o sin guiones, 3 formatos de fecha, «hoy» y «ayer», todas las palabras | `src/lib/busqueda.ts` | `busqueda.test.ts` |
| Resaltado sin `dangerouslySetInnerHTML` | `segmentar` + `Resaltado.tsx` (nodos `<mark>`); regla `react/no-danger: error` | `busqueda.test.ts` y `componentes.test.tsx`: `<b>` se muestra como texto |
| `?q=` se conserva al ir al detalle y regresar; botón X | `Historial.tsx`, `Detalle.tsx` | e2e «buscar, abrir un detalle y regresar»; `componentes.test.tsx` |
| Lista vacía sin buscador ni botón flotante | `Historial.tsx` | `componentes.test.tsx` |
| Estado de sesión: se comparte entre rutas y se reinicia al recargar | `LiquidacionesProvider.tsx` en el layout raíz (`useSyncExternalStore`), sin `localStorage` | e2e «registrar…» (ir a Motos y regresar) |
| Etiqueta «Nueva» | solo la última registrada; desaparece al salir de la pantalla, al registrar otra o al recargar; corregir no la pone | e2e «registrar…» |
| Corregir la fecha la mueve de grupo | el repositorio vuelve a ordenar | `repo.test.ts`; e2e «corregir la fecha a ayer» |
| Menú: 5 opciones en computadora; 4 botones y pestañas en celular | `src/lib/nav.ts` (lista única), `AppShell.tsx`, `Provisional.tsx`; `aria-current="page"` | `componentes.test.tsx`; e2e «menú» y «Administración → pestañas» |
| Accesibilidad de panel, hoja, selector y calendario | Radix Dialog/Popover: foco atrapado y Escape. Foco inicial en el campo Moto, el buscador o el día elegido. El foco regresa al botón que abrió. Selector tipo combobox con flechas y Enter | e2e «teclado» (2 pruebas) y axe |
| Selector de sesión solo en desarrollo | `MOSTRAR_SELECTOR_SESION = NODE_ENV === "development"` | e2e contra `next build && next start` (cuenta 0) y control en `next dev` (visible) |
| ANN-145: criterio ajustado | actualizado en Linear; ANN-145 en Done | — |
| ANN-143 | In Progress, con comentario; queda abierta hasta conectarla con ANN-137 y ANN-138 | — |

## 4. Desviaciones respecto al diseño o al plan

1. **Contraste (para cumplir «axe sin violaciones críticas o serias»).**
   - El texto en ocre, los enlaces y el fondo del botón principal pasan de `#C25A12` (4.4:1) a `#A84B0C` (5.7:1); el hover queda en `#8F3F0A`.
   - El texto de aviso «Sin chofer» pasa de `#B26A00` a `#8A5300`.
   - Los encabezados del calendario se dejan sin opacidad.
   - `#C25A12` se queda para iconos, foco y acentos.
2. **Versión de Next.js.** Se usa 16.4.1, porque 15.5.x tiene vulnerabilidades críticas publicadas (entre ellas RCE en React Server Components).
3. **`cacheComponents` desactivado.** Esa función de Next 16 deja las rutas ocultas en lugar de desmontarlas al navegar, y eso rompía la regla de la etiqueta «Nueva».
4. **Texto nuevo** cuando la moto no tiene chofer: «45-PQR-2 no tiene chofer. Elige quién la trae.». El diseño no traía texto para ese caso.
5. **Calendario.** Los días de la semana salen como «lu, ma, mi…» (locale de react-day-picker) en lugar de «L M M…». No se pueden elegir fechas futuras, como en el diseño.

## 5. Riesgos conocidos

- `npm audit` todavía reporta avisos altos en dependencias de desarrollo: `braces` (cadena de ESLint) y `postcss`, que Next.js trae dentro para compilar. Ninguno se ejecuta en el navegador ni procesa datos de usuarios.
- Es una maqueta: los datos de prueba están en el cliente, sin servidor ni autenticación. No apta para datos reales; eso queda para las Fases 1 y 2 y para la tarea de login.

## 6. Archivos principales

```
web/
├─ src/app/                      rutas: / → /liquidaciones, [id], motos, choferes, usuarios, financiamiento, login
├─ src/components/shell/         AppShell (menú), BarraSuperior, Provisional, SelectorSesion
├─ src/components/liquidaciones/ Historial, Detalle, FormLiquidacion
├─ src/components/ui/            Desplegable, ListaOpciones, Resaltado, Aviso, useEsEscritorio
├─ src/data/                     types, mock (§8), repo, LiquidacionesProvider
├─ src/lib/                      clock, fechas, monto, busqueda, formulario, nav, session, texto
├─ e2e/                          flujos.spec.ts, selector-dev.spec.ts
├─ playwright.config.ts, vitest.config.mts, eslint.config.mjs
└─ README.md
```
