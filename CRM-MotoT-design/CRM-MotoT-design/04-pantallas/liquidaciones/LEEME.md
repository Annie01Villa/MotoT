# Pantallas · Liquidaciones (Gerente y Ayudante; pantalla de inicio)

Lienzo publicado: https://claude.ai/artifact/7LsAXKFRbYJkd4LP2h9Wxn

Es la antigua «v2»: el 14 oct 2026 Annie la eligió como versión oficial y la v1 se borró.

Cada pantalla es un archivo `.dc.html` (celular 390×844 y computadora 1440×900); `canvas.json` guarda el acomodo y los nombres.
`generar_pantallas.py` vuelve a crear todos los archivos: `python3 generar_pantallas.py <carpeta>`.

| # | Pantalla | Celular | Computadora |
|---|---|---|---|
| 1 | Liquidaciones · Historial | Main.dc.html | HistorialPC.dc.html |
| 2 | Liquidaciones · Buscando («Juan») | BuscandoCel.dc.html | BuscandoPC.dc.html |
| 3 | Liquidaciones · Sin resultados («Roberto») | SinResultadosCel.dc.html | SinResultadosPC.dc.html |
| 4 | Liquidaciones · Lista vacía | VaciaCel.dc.html | VaciaPC.dc.html |
| 5 | Liquidaciones · Registrar | RegistrarCel.dc.html | RegistrarPC.dc.html |
| 5a | Liquidaciones · Registrar · Elegir moto | ElegirMotoCel.dc.html | ElegirMotoPC.dc.html |
| 5b | Liquidaciones · Registrar · Fecha (calendario) | FechaCel.dc.html | FechaPC.dc.html |
| 5c | Liquidaciones · Registrar · Monto con teclado numérico | TecladoCel.dc.html | (solo celular) |
| 6 | Liquidaciones · Registrar con errores | ErroresCel.dc.html | ErroresPC.dc.html |
| 7 | Liquidaciones · Liquidación registrada (aviso) | RegistradaCel.dc.html | RegistradaPC.dc.html |
| 8 | Liquidaciones · Detalle | DetalleCel.dc.html | DetallePC.dc.html |
| 9 | Liquidaciones · Corregir | CorregirCel.dc.html | CorregirPC.dc.html |

Sesión: Pedro Martínez · Ayudante (sin Financiamiento en el menú).

Decisiones (frente a la v1 descartada):
- Sin contador «4 liquidaciones» bajo el título (el brief excluye totales).
- El monto del detalle usa el tamaño de título del design system (24/32 celular, 28/36 computadora); la v1 usaba 40 px.
- Se dibujan el calendario (5b) y el teclado numérico del monto (5c); la v1 los daba por supuestos.
- Buscador con botón para borrar (x) cuando tiene texto.
- Lista vacía sin buscador ni botón flotante: el único botón es el del centro.
- Detalle en computadora: Moto y Chofer en dos tarjetas lado a lado, «Corregir» dentro de la tarjeta del monto.
- La fecha y el nombre del detalle se muestran con icono, sin etiquetas extra.
- Aviso de éxito en celular sin botón de cerrar (es temporal) para que quepa en una línea.
- Formulario en una sola columna también en computadora (la v1 ponía Fecha y Monto lado a lado).
- La liquidación nueva se resalta con fondo naranja claro (#FDF3EA) y etiqueta «Nueva» con punto naranja; en el aviso es la primera de «Hoy».

Colores: el 14 oct 2026 el azul petróleo se cambió por ocre #C25A12 (hover #A84B0C) y naranja claro #FDF3EA; el acento #F26B1D se mantiene.
