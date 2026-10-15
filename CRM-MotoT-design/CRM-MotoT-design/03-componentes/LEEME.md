# Componentes · Hoja de componentes CRM-MotoT

Hoja publicada: https://claude.ai/artifact/K8jbcxGVXqKt8VA6Fv2FLm

- `hoja-componentes.html`: la hoja (HTML estático, 1440 px). Es lo que se publica.
- `generar_hoja.py`: genera el HTML (`python3 generar_hoja.py hoja-componentes.html`). Para cambiar algo, edita el script y vuelve a generar.

Design system: el ocre del mensaje de Annie (#C25A12, neutros cálidos, bordes de 1 px, Inter, Lucide 20 px trazo 1.5), el mismo del login (`pantallas/login/`). No usa el azul petróleo de motos y choferes.

12 grupos: navegación, buscador, elementos de lista, vacío/sin resultados, botones, campos, selector de lista, selector de rol, etiquetas, tarjeta de detalle, mensajes y encabezado. Cada componente lleva un nombre tipo `Boton/Principal`.

Supuestos (también listados arriba en la hoja): ocre presionado #8F3F0A; peligro hover #991B1B y presionado #7F1D1D; hover del menú lateral #EEEDEC; opciones del menú lateral de 40 px (mouse); botón flotante 56 px, radio 6, con sombra; icono `settings` para Administración en la barra inferior; datos extra inventados (Carlos Ramírez, Pedro Sánchez Vega, Rosa Hernández Díaz, motos 14-MNR-2 y 09-PLQ-5).
