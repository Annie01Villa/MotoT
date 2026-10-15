# Pantallas · Financiamiento (Administración, solo Gerente)

Fuente del lienzo publicado: https://claude.ai/artifact/7FFLk6JwsimEtRc18j99CZ

Cada pantalla es un archivo `.dc.html` (celular 390×844 y computadora 1440×900).
`canvas.json` guarda el acomodo y el nombre de cada pantalla.

| # | Pantalla | Celular | Computadora |
|---|---|---|---|
| 1 | Financiamiento · Lista | Main.dc.html | ListaPC.dc.html |
| 2a | Financiamiento · Sin resultados («99-ZZZ-9») | SinResultadosCel.dc.html | SinResultadosPC.dc.html |
| 2b | Financiamiento · Lista vacía | VaciaCel.dc.html | VaciaPC.dc.html |
| 3 | Financiamiento · Detalle (27-ABC-4) | DetalleCel.dc.html | DetallePC.dc.html |
| 4 | Financiamiento · Registrar | RegistrarCel.dc.html | RegistrarPC.dc.html |
| 4b | Financiamiento · Registrar · Elegir fecha (calendario) | FechaCel.dc.html | FechaPC.dc.html |
| 5 | Financiamiento · Corregir | CorregirCel.dc.html | CorregirPC.dc.html |
| 6 | Financiamiento · Con errores | ErroresCel.dc.html | ErroresPC.dc.html |
| 7 | Financiamiento registrado · Aviso | RegistradoCel.dc.html | RegistradoPC.dc.html |

Mismo estilo que /pantallas/motos/ y /pantallas/choferes-*/ (design system del mensaje de Annie).
Sesión: Laura Méndez · Gerente (el menú incluye Financiamiento con icono landmark).
Decisiones: en celular, dentro de la pestaña Administración hay pestañas «Usuarios | Financiamiento» bajo la barra superior
(la activa con barra naranja); el calendario es una hoja inferior en celular y un recuadro bajo el campo en computadora,
con semana de domingo a sábado; el monto lleva prefijo $ fijo e inputmode="decimal"; tras guardar se abre el detalle del
financiamiento nuevo (31-XKT-8) con el aviso, igual que en Motos. Corregir en computadora abre la ventana sobre el detalle.

Colores: el 14 oct 2026 el azul petróleo se cambió por ocre #C25A12 (hover #A84B0C) y naranja claro #FDF3EA; el acento #F26B1D se mantiene.
