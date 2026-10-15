# CRM-MotoT · Design

Todo el diseño de la fase 0 del CRM-MotoT. Color principal: ocre #C25A12.

## Qué abrir primero

1. **01-documento/CRM motoT.html**: el resumen completo (producto, roles, alcance del MVP, design system e inventario de pantallas). Ábrelo en el navegador. Es lo mismo que «CRM motoT.md».
2. **05-visor/visor.html**: todas las pantallas en una sola página, con interruptor Claro/Oscuro.

## Carpetas

| Carpeta | Qué tiene |
|---|---|
| 01-documento | El resumen de la fase 0, en md y en HTML. |
| 02-design-system | Hoja del design system vigente (hoja-design-system.html). |
| 03-componentes | Hoja de componentes (hoja-componentes.html). |
| 04-pantallas | Una carpeta por módulo: login, motos-lista, motos, choferes-lista, choferes-detalle, financiamiento, liquidaciones y usuarios. Cada una tiene sus pantallas en .dc.html, su canvas.json y su LEEME.md. |
| 05-visor | Visor de todas las pantallas (visor.html) y el script que lo genera. |
| archivo/design-system-v1 | El primer design system (Geist, ocre #C96F1F). Ya no se usa; se guarda como referencia. |

Nota: los scripts generar_*.py esperan la estructura original del proyecto (pantallas/, componentes/, etc.), no la de este zip.
