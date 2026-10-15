# MotoT

Sistema de diseño del CRM de MotoT. Corporativo, sobrio y limpio: una base neutra casi blanca (o casi negra en tema oscuro), tipografía precisa y un único acento ocre-naranja que se reserva para lo que importa. Toma de Stripe la claridad de la información, de Attio la tabla como protagonista y de Linear la densidad tranquila y el foco en el teclado.

Esta primera versión define **solo los fundamentos**: color, tipografía, espaciado, radios, sombras, medidas y capas. Los componentes y las pantallas se diseñan después, siempre a partir de estos tokens.

## Principios

1. **Neutro primero, ocre con intención.** El 90 % de la interfaz es gris cálido muy ligero. El ocre marca una sola cosa por zona: la acción principal, la selección actual o el foco. Si en una vista hay más de tres elementos ocres, sobra alguno.
2. **Los datos mandan.** Un CRM se lee en tablas, listas y fichas. La jerarquía viene del peso y del tono del texto, no de cajas, colores o iconos.
3. **Bordes antes que sombras.** Las superficies se separan con `border-default` de 1px. La sombra (`shadow-md`, `shadow-lg`) queda para lo que flota: menús, popovers, modales.
4. **Denso pero respirable.** Tamaño base de 14px, filas de 40px, retícula de 4px. Compacto como Linear, nunca apretado.
5. **Rápido con el teclado.** Todo lo accionable tiene foco visible (`focus-ring`) y, cuando aplique, atajo de teclado.

## Color

Dos capas de tokens:

- **Primitivos** (`gray-*`, `ocre-*`, `green-*`, `yellow-*`, `red-*`, `blue-*`): la paleta en bruto, igual en ambos temas. No se usan directamente en componentes.
- **Semánticos** (`bg-*`, `border-*`, `text-*`, `accent*`, `success`, `warning`, `danger`, `info`): lo que usan los componentes. Cambian de valor entre tema claro y oscuro.

### Neutros

Gris con un ligerísimo sesgo cálido, para que conviva con el ocre sin parecer gris de sistema.

| Rol | Token | Uso |
| --- | --- | --- |
| Canvas | `bg-canvas` | Fondo de la app, detrás de todo |
| Superficie | `bg-surface` | Tablas, tarjetas, fichas, modales |
| Sutil | `bg-subtle` | Barra lateral, hover de filas, cabeceras de tabla |
| Apagado | `bg-muted` | Chips neutros, campos deshabilitados |
| Borde | `border-subtle` / `border-default` / `border-strong` | Divisores, contornos de tarjeta, contornos de input |
| Texto | `text-primary` / `text-secondary` / `text-tertiary` | Valor / etiqueta / metadato |

### Acento ocre-naranja

`ocre-500` (#c96f1f) es el color de marca. En la interfaz se usa a través de los semánticos:

- `accent` en el botón primario, interruptores activos, indicador de pestaña y checkbox marcado. En claro es `ocre-600` para que el texto blanco tenga contraste AA; en oscuro sube a `ocre-400` con texto oscuro (`text-on-accent`).
- `accent-subtle` para la fila seleccionada y el item activo de la barra lateral.
- `accent-text` para enlaces y texto de acento.
- `focus` para el anillo de foco.

Nunca: degradados con el ocre, ocre como fondo de áreas grandes, ocre para estados (éxito, error) ni texto pequeño en `ocre-500` sobre blanco.

### Estados

`success` (verde), `warning` (amarillo), `danger` (rojo) e `info` (azul), cada uno con su fondo `*-subtle`. El amarillo de advertencia es deliberadamente más amarillo que el ocre para no confundirse con el acento. Los estados siempre van con texto o icono, nunca solo color.

## Tipografía

**Geist** para toda la interfaz y **Geist Mono** para datos (folios, importes en columnas, códigos). Ambas en Google Fonts. Respaldo: Inter y la fuente del sistema.

| Estilo | Tamaño / interlineado | Peso | Uso |
| --- | --- | --- | --- |
| `display` | 32 / 40 | 600 | Una vez por pantalla como máximo |
| `heading-1` | 24 / 32 | 600 | Título de página o de registro |
| `heading-2` | 18 / 26 | 600 | Secciones, títulos de modal |
| `heading-3` | 15 / 22 | 600 | Títulos de tarjeta y grupos de campos |
| `body-lg` | 15 / 24 | 400 | Notas y textos largos |
| `body` | 14 / 20 | 400 | **Base de la interfaz** |
| `body-strong` | 14 / 20 | 500 | Nombres, botones, valores clave |
| `small` | 13 / 18 | 400 | Ayudas, metadatos |
| `caption` | 12 / 16 | 500 | Badges, cabeceras de columna |
| `overline` | 11 / 16 | 600, +0.06em, MAYÚSCULAS | Grupos de la barra lateral |
| `mono` | 13 / 20 | 400 | IDs, importes, códigos |

Reglas: títulos con tracking negativo; cifras siempre con `font-variant-numeric: tabular-nums` cuando se alinean en columnas; importes alineados a la derecha; máximo dos pesos por bloque.

## Espaciado, radios y medidas

- **Espaciado** en retícula de 4px: `space-1` (4) … `space-16` (64). Botones e inputs usan `space-3` de relleno horizontal; tarjetas y modales `space-6`; secciones de página se separan con `space-8`.
- **Radios** contenidos: `radius-xs` 4px (badges, checkboxes), `radius-sm` 6px (botones, inputs), `radius-md` 8px (tarjetas, tablas, menús), `radius-lg` 12px (modales), `radius-full` (avatares, pills).
- **Controles**: `control-sm` 28px, `control-md` 32px (por defecto), `control-lg` 40px. Filas de tabla `row-height` 40px.
- **Layout**: barra lateral `sidebar-width` 240px, barra superior `topbar-height` 48px.

## Elevación

| Nivel | Token | Para |
| --- | --- | --- |
| 0 | borde `border-default` | Tarjetas, tablas, paneles |
| 1 | `shadow-xs` | Inputs y botones secundarios |
| 2 | `shadow-md` | Dropdowns, popovers, menús |
| 3 | `shadow-lg` | Modales, command palette |

En tema oscuro las sombras se oscurecen y las superficies elevadas suben un paso de luminosidad.

## Iconografía

Recomendación: **Lucide**, trazo de 1.5px, a `icon-md` (16px) en la interfaz y `icon-sm` (14px) en badges. Color `text-secondary` por defecto; `text-primary` en hover; `accent-text` solo en el item activo. Sin iconos de colores ni emoji en la interfaz.

## Logotipo

Aún no hay logotipo. Mientras tanto, la marca se escribe como palabra: **MotoT** en Geist 600, tracking −0.03em, en `text-primary`. Cuando exista el logo se añade como recurso del sistema.

## Voz y tono

Español claro y directo, de tú, sin tecnicismos internos. Botones con verbo y objeto: «Crear trato», «Guardar contacto», «Asignar a…». Confirmaciones breves: «Trato guardado». Errores que dicen qué pasó y cómo arreglarlo: «No se pudo guardar: el correo ya existe en otro contacto». Fechas relativas cuando ayudan («hace 3 min», «mañana»), absolutas en tablas (14 oct 2026). Moneda con símbolo y separadores: $ 148,500.00.

## Accesibilidad

Todo par de texto y fondo de este sistema cumple 4.5:1 en ambos temas; `border-control` y `focus` cumplen 3:1 sobre superficie. `border-strong` es más suave que 3:1 a propósito, por estética: úsalo solo en inputs que siempre llevan etiqueta visible. Respetar `prefers-reduced-motion`.

## Próximos pasos

Componentes base, en este orden: botón, input y select, checkbox e interruptor, badge de estado, avatar, tabla de registros, item de barra lateral, menú y command palette, modal, toast.
