# Pantallas · Usuarios (Administración)

Fuente del lienzo publicado: https://claude.ai/artifact/U2687smPs8Dm63SU9v4qZV

Cada pantalla es un archivo `.dc.html` (celular 390×844 y computadora 1440×900).
`canvas.json` guarda el acomodo y el nombre de cada pantalla.

| # | Pantalla | Celular | Computadora |
|---|---|---|---|
| 1 | Usuarios · Vista Gerente | Main.dc.html | ListaPC.dc.html |
| 1b | Usuarios · Vista Gerente · Menú de acciones (tres puntos) | MenuCel.dc.html | — |
| 2 | Usuarios · Vista Ayudante | AyudanteCel.dc.html | AyudantePC.dc.html |
| 3 | Dar de alta usuario | AltaCel.dc.html | AltaPC.dc.html |
| 4a | Dar de alta usuario · Con errores | ErroresCel.dc.html | ErroresPC.dc.html |
| 4b | Dar de alta usuario · Correo repetido | RepetidoCel.dc.html | RepetidoPC.dc.html |
| 5 | Confirmar baja (Pedro Martínez) | BajaCel.dc.html | BajaPC.dc.html |
| 6a | Aviso · Usuario dado de alta | AltaAvisoCel.dc.html | AltaAvisoPC.dc.html |
| 6b | Aviso · Pedro Martínez fue dado de baja | BajaAvisoCel.dc.html | BajaAvisoPC.dc.html |
| 7 | Usuarios · Sin resultados («Roberto») | SinResultadosCel.dc.html | SinResultadosPC.dc.html |

Mismo estilo que /pantallas/financiamiento/ y /pantallas/choferes-lista/.
Decisiones: la persona con la sesión aparece con «(tú)» y no tiene acción de baja sobre sí misma;
el rol viene marcado en Ayudante al abrir el formulario; en celular «Volver a dar de alta» también va en el
menú de tres puntos; el aviso «Usuario dado de alta» se muestra tras volver a dar de alta a Sofía Torres
(así no se inventan usuarios); con el aviso en celular el botón «+» sube para no taparse;
el aviso del Ayudante usa el fondo suave del primario (#FDF3EA) con icono info;
la vista del Ayudante en celular no muestra las pestañas «Usuarios | Financiamiento» porque solo tiene Usuarios.

Colores: el 14 oct 2026 el azul petróleo se cambió por ocre #C25A12 (hover #A84B0C) y naranja claro #FDF3EA; el acento #F26B1D se mantiene.
