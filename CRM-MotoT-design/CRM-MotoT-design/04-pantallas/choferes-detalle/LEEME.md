# Pantallas · Chofer (detalle y formulario)

Fuente del lienzo publicado: https://claude.ai/artifact/ReVwL9pY9ZF6K13ghzgq1h

Cada pantalla es un archivo `.dc.html` (celular 390×844 y computadora 1440×900).
`canvas.json` guarda el acomodo y el nombre de cada pantalla.

| # | Pantalla | Celular | Computadora |
|---|---|---|---|
| 1 | Chofer · Detalle (Juan Pérez López) | Main.dc.html | DetallePC.dc.html |
| 2 | Chofer sin moto · Detalle (Carlos Ramírez Díaz) | SinMotoCel.dc.html | SinMotoPC.dc.html |
| 3 | Registrar chofer | RegistrarCel.dc.html | RegistrarPC.dc.html |
| 4 | Corregir chofer | CorregirCel.dc.html | CorregirPC.dc.html |
| 5 | Registrar chofer · Con errores | ErroresCel.dc.html | ErroresPC.dc.html |
| 6 | Chofer registrado · Aviso | RegistradoCel.dc.html | RegistradoPC.dc.html |

Mismo estilo que /pantallas/motos/ y /pantallas/choferes-lista/ (design system del mensaje de Annie,
sesión Pedro Martínez · Ayudante).
Decisiones: en celular «Corregir datos» va a la derecha de la barra superior (el nombre largo no cabe junto al título);
teléfono con botón «Llamar» (tel:) solo en celular; el campo Teléfono usa inputmode="numeric" y la ayuda «10 números»,
que se cambia por el error cuando aplica. El chofer nuevo del aviso es Carlos Ramírez Díaz (sin moto ni liquidaciones).
Las ventanas de computadora (560 px) se abren sobre la lista de choferes (registrar) o sobre el detalle (corregir).

Colores: el 14 oct 2026 el azul petróleo se cambió por ocre #C25A12 (hover #A84B0C) y naranja claro #FDF3EA; el acento #F26B1D se mantiene.
