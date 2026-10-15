# Visor de pantallas CRM-MotoT

Una sola página con todas las pantallas: menú desplegable por módulo a la izquierda y la pantalla elegida a la derecha (celular o computadora, ajustada o al 100 %, tema claro u oscuro).

El tema oscuro se genera solo: `a_oscuro()` en `generar_visor.py` cambia cada color según su papel (texto, relleno o línea). La tabla de colores está en «CRM motoT.md», sección 6.1.

- `plantilla.html`: diseño del visor (menú, barra, escenario).
- `generar_visor.py`: lee `/pantallas/*/canvas.json` y los `.dc.html`, más las hojas de Componentes y Design system v2, y escribe `visor.html`.
- Para actualizar tras cambiar pantallas: `python3 generar_visor.py` y volver a publicar `visor.html` en el mismo enlace.

Los enlaces dentro de cada pantalla (por ejemplo «Registrar» o una fila de la lista) abren la pantalla correspondiente del mismo módulo.
