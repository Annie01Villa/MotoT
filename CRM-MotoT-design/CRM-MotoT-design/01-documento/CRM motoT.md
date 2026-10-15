# CRM-MotoT · Fase 0

Resumen de todo lo definido y diseñado hasta el 14 oct 2026: producto, roles, alcance del MVP, design system y pantallas.
Las fuentes son los briefs de Annie en el proyecto, los `LEEME.md` de cada carpeta y los lienzos publicados.

---

## 1. Producto

CRM-MotoT es una aplicación web en español (México) para administrar una flotilla de motos de trabajo. Sirve para:

- Saber qué chofer trae cada moto.
- Registrar los pagos (liquidaciones) que entrega cada chofer.
- Llevar el registro de los financiamientos de las motos.

La usan personas no técnicas: textos claros, cortos y sin jerga.

## 2. Roles

| Rol | Puede |
|---|---|
| **Gerente** | Todo: motos, choferes, liquidaciones, dar de alta y de baja usuarios, y financiamientos. |
| **Ayudante** | Registrar y consultar motos, choferes y liquidaciones. Ve la lista de usuarios, pero no puede dar altas ni bajas. No ve Financiamiento. |

## 3. Dispositivos

- Celular 390 × 844 px (se diseña primero) y computadora 1440 × 900 px.
- Áreas táctiles de mínimo 44 px.
- Solo modo claro.

## 4. Alcance del MVP

### Módulos

| Módulo | Sección del menú | Quién lo usa |
|---|---|---|
| Inicio de sesión y recuperar contraseña | (sin menú) | Todos |
| Liquidaciones (pantalla de inicio) | Operación | Gerente y Ayudante |
| Motos | Operación | Gerente y Ayudante |
| Choferes | Operación | Gerente y Ayudante |
| Usuarios | Administración | Gerente (altas y bajas); Ayudante (solo consulta) |
| Financiamiento | Administración | Solo Gerente |

### Datos de cada registro

- **Moto:** placa (MAYÚSCULAS, única), modelo, chofer (opcional, se puede asignar después).
- **Chofer:** nombre completo, teléfono (10 números), domicilio. La moto se le asigna desde la pantalla de Motos.
- **Liquidación:** moto, chofer (se llena solo con el de la moto y se puede cambiar), fecha (hoy por defecto), monto en pesos y nombre (se llena solo como «27-ABC-4 · 13 oct 2026», editable).
- **Financiamiento:** placa (texto, sin enlace a la moto), fecha de inicio y monto financiado.
- **Usuario:** nombre completo, correo (con él entra al CRM), rol (Gerente o Ayudante) y estado (Alta o Baja). Al darlo de alta se le envía un correo para crear su contraseña.

### Reglas generales

- Cada lista tiene un buscador arriba que filtra mientras se escribe; al abrir un detalle y regresar, la lista conserva la búsqueda.
- Los mensajes de éxito son avisos temporales: abajo en celular y arriba a la derecha en computadora.
- Después de entrar, el usuario llega a Liquidaciones.
- Un usuario dado de baja no puede entrar («Tu usuario está dado de baja. Habla con el Gerente para volver a entrar.»).

### Queda fuera del MVP

- Estado de la moto (activa, en taller, de baja).
- Licencia, vigencia de licencia y contacto de emergencia del chofer.
- Plazo, número de pagos, pago periódico, saldo pendiente y barra de avance del financiamiento; enlace del financiamiento a su moto y selector de motos en Financiamiento.
- Historial de quién hizo cada movimiento.
- Permisos detallados por pantalla y fotos de perfil.
- Totales, gráficas y reportes.

## 5. Estructura de la app

- **Celular:** barra superior con el título de la pantalla y barra de navegación inferior fija con 4 opciones: Liquidaciones, Motos, Choferes y Administración. Dentro de Administración: Usuarios y, solo para el Gerente, Financiamiento (como pestañas «Usuarios | Financiamiento» bajo la barra superior).
- **Computadora:** menú lateral izquierdo fijo de 240 px con el logo de texto «CRM-MotoT» (icono bike), sección «Operación» (Liquidaciones, Motos, Choferes) y sección «Administración» (Usuarios y, solo para el Gerente, Financiamiento). Al pie: nombre del usuario, etiqueta de rol y «Cerrar sesión».
- **Opción activa del menú:** texto e icono en primario, fondo suave del primario y barra de acento naranja.
- **Formularios:** en celular, pantalla completa; en computadora, ventana centrada de 560 px (Motos, Choferes, Financiamiento, Usuarios) o panel lateral derecho de 480 px (Liquidaciones).
- **Selectores de lista** (elegir moto o chofer): hoja que sube desde abajo en celular; ventana o menú desplegable en computadora.

## 6. Design system

> El 14 oct 2026 Annie pidió cambiar el azul petróleo por ocre y naranja claro. Ahora todo el proyecto usa el ocre `#C25A12` como color principal: las pantallas de la app cambiaron su azul por ocre, y el inicio de sesión, la hoja de componentes y la hoja del design system ya estaban en ocre. Las pantallas conservan su tipografía, tamaños y radios; solo cambió el color.

### 6.1 Vigente: ocre + naranja claro

**Colores en las pantallas de la app**

| Uso | Color |
|---|---|
| Principal ocre (botones principales, enlaces, opción activa) | `#C25A12` · hover `#A84B0C` · naranja claro (fondo suave, opción activa, etiqueta Gerente) `#FDF3EA` |
| Acento naranja moto (solo detalles: icono del logo, barra de la opción activa, indicadores; nunca texto pequeño sobre blanco) | `#F26B1D` |
| Fondo de la app | `#F7F8FA` |
| Tarjetas y superficies | `#FFFFFF` |
| Bordes | `#E2E8F0` |
| Texto principal / secundario | `#1A202C` / `#5A6475` |
| Éxito y estado Alta | `#1E8E3E` sobre `#E6F4EA` |
| Error, estado Baja y acciones peligrosas | `#C5221F` sobre `#FCE8E6` |
| Aviso («Sin chofer», «Sin moto») | `#B26A00` sobre `#FFF4E5` |
| Etiqueta Gerente | `#C25A12` sobre `#FDF3EA` |
| Etiqueta Ayudante | `#5A6475` sobre `#EEF0F3` |

El inicio de sesión, la hoja de componentes y la hoja del design system usan el mismo ocre con los neutros cálidos de la sección 6.2; unificar esos neutros con los de las pantallas queda como pendiente.

**Tipografía:** Inter.

| Estilo | Celular | Computadora |
|---|---|---|
| Título de pantalla | 24/32 semibold | 28/36 semibold |
| Subtítulo | 18/26 semibold | 18/26 semibold |
| Cuerpo | 16/24 regular | 16/24 regular |
| Secundario | 14/20 regular | 14/20 regular |
| Etiqueta | 12/16 medium | 12/16 medium |

- Montos y fechas con números tabulares.
- Placas en MAYÚSCULAS, semibold, espaciado de letras 0.5 px.

**Espacios:** escala 4, 8, 12, 16, 24, 32, 48 px. Margen lateral 16 px en celular y 32 px en computadora.

**Bordes:** radio 8 px en botones y campos, 12 px en tarjetas, redondo completo en etiquetas. Sombra de tarjeta `0 1px 2px rgba(0,0,0,0.06)`.

**Iconos:** Lucide de línea, 24 px.

| Concepto | Icono |
|---|---|
| Moto | bike |
| Chofer | user |
| Usuarios | users |
| Liquidación | receipt |
| Financiamiento | landmark |
| Buscar | search |
| Agregar | plus |
| Corregir | pencil |
| Regresar | arrow-left |
| Teléfono | phone |
| Cerrar sesión | log-out |

**Formatos:** dinero `$1,500.00` · fecha `13 oct 2026` · teléfono `55 1234 5678`.

**Tema oscuro** (14 oct 2026, derivado del ocre; se ve con el interruptor Claro/Oscuro del [visor de pantallas](https://claude.ai/artifact/12sBptLq8dwRqXPSvKEwkA), reglas en `visor/generar_visor.py`):

| Papel | Claro | Oscuro |
|---|---|---|
| Fondo de la app | `#F7F8FA` / `#FAFAF9` | `#171412` |
| Tarjetas y superficies | `#FFFFFF` | `#24201D` |
| Fondo sutil / hover | `#F5F5F4` / `#EEF0F3` | `#2E2926` |
| Bordes | `#E2E8F0` / `#E7E5E4` · `#D6D3D1` | `#3A3532` · `#4A4440` |
| Texto principal / secundario / tenue | `#1A202C` / `#5A6475` / `#78716C` | `#F5F5F4` / `#C9C4C0` / `#A8A29E` |
| Botón principal | `#C25A12` con texto blanco | igual (`#C25A12`, texto blanco) |
| Ocre como texto, icono o enlace | `#C25A12` | `#EB8F4E` (borde de foco `#E07A33`) |
| Naranja claro (activo, «Nueva») | `#FDF3EA` | `#3A2516` |
| Error texto / fondo | `#C5221F` / `#FCE8E6` | `#F87171` / `#3B1A18` |
| Éxito texto / fondo | `#1E8E3E` / `#E6F4EA` | `#4ADE80` / `#16301F` |
| Aviso texto / fondo | `#B26A00` / `#FFF4E5` | `#FBBF24` / `#36290F` |

El texto en oscuro pasa AA (4.5:1 o más) sobre su fondo; la excepción es el texto blanco del botón ocre, que queda en 4.4:1 igual que en el tema claro. Las hojas de Componentes y Design system siguen solo en claro.

### 6.2 Historia del sistema

Antes del cambio hubo dos iteraciones de design system con ocre-naranja como acento sobre base neutra, inspiradas en Stripe, Attio y Linear (corporativo, sobrio, bordes de 1 px en lugar de sombras, jerarquía por tamaño y peso).

1. **Design system v1** (`design-system/`, lienzo [MotoT](https://claude.ai/artifact/ChhjnhW1oZQ8TdfbXuPptg)): ocre `#C96F1F`, tipografía Geist y Geist Mono, tokens en `tokens.css` y `tokens.json`. Ya no se usa.
2. **Design system v2** (`design-system-v2/`, lienzo [Design system CRM-MotoT](https://claude.ai/artifact/YWatJC14K7odmKowZNh6ef)): ocre `#C25A12` (hover `#A84B0C`, fondo suave `#FDF3EA`), neutros cálidos (`#FAFAF9`, `#F5F5F4`, `#E7E5E4`, `#D6D3D1`), texto `#1C1917` / `#57534E` / `#78716C`, Inter con títulos 22/28 (24/32 en computadora), radios 6/8 px, tarjetas sin sombra, Lucide 20 px trazo 1.5, filas de tabla de 44 px. Es el que usan el inicio de sesión y la hoja de componentes.
3. **Azul petróleo** (`#0F4C5C`, hover `#0B3A47`, fondo suave `#E6F0F2`): el color principal que traían los briefs de las pantallas de la app. El 14 oct 2026 se cambió por el ocre en todas ellas.

### 6.3 Tono de los textos

- Sí: «Liquidación registrada», «No encontramos motos con esa placa», «¿Dar de baja a Sofía Torres? Ya no podrá entrar al CRM.», «Escribe el monto en pesos».
- No: «Error 500», «Registro insertado correctamente».
- Botones con verbo y objeto («Guardar moto», «Registrar chofer»). Errores que dicen qué falta («Escribe la placa», «Elige la moto»).

## 7. Inventario de pantallas

Todas las pantallas están en `/mnt/project-files/pantallas/<carpeta>/`, en celular y computadora, como archivos `.dc.html` con un `canvas.json` que guarda el acomodo.

| Módulo | Carpeta | Lienzo | Pantallas | Sistema | Sesión mostrada |
|---|---|---|---|---|---|
| Inicio de sesión | `login/` | [Login · Inicio de sesión](https://claude.ai/artifact/Pcout1hDmDWFc6LCWEyjFF) | 6 | Ocre | — |
| Motos · Lista | `motos-lista/` | [Motos · Lista](https://claude.ai/artifact/BU5LsVNYQ2GhgdUAp1TVVh) | 4 | Ocre (antes azul) | Pedro · Ayudante |
| Moto · Detalle y formulario | `motos/` | [Moto · Detalle y formulario](https://claude.ai/artifact/BwiajkLqFE55oo5LvuZisK) | 8 | Ocre (antes azul) | Pedro · Ayudante |
| Choferes · Lista | `choferes-lista/` | [Choferes · Lista](https://claude.ai/artifact/S3NPEB7RcgKWfUMYFwaMzv) | 4 | Ocre (antes azul) | Pedro · Ayudante |
| Chofer · Detalle y formulario | `choferes-detalle/` | [Chofer · Detalle y formulario](https://claude.ai/artifact/ReVwL9pY9ZF6K13ghzgq1h) | 6 | Ocre (antes azul) | Pedro · Ayudante |
| Financiamiento | `financiamiento/` | [Financiamiento](https://claude.ai/artifact/7FFLk6JwsimEtRc18j99CZ) | 9 | Ocre (antes azul) | Laura · Gerente |
| Liquidaciones | `liquidaciones/` | [Liquidaciones](https://claude.ai/artifact/7LsAXKFRbYJkd4LP2h9Wxn) | 12 | Ocre (antes azul) | Pedro · Ayudante |
| Usuarios | `usuarios/` | [Usuarios](https://claude.ai/artifact/U2687smPs8Dm63SU9v4qZV) | 10 | Ocre (antes azul) | Laura · Gerente y Pedro · Ayudante |

Piezas de referencia (no son pantallas):

| Pieza | Carpeta | Lienzo | Sistema |
|---|---|---|---|
| Hoja de componentes (12 grupos) | `componentes/` | [Componentes CRM-MotoT](https://claude.ai/artifact/K8jbcxGVXqKt8VA6Fv2FLm) | Ocre |
| Hoja del design system | `design-system-v2/` | [Design system CRM-MotoT](https://claude.ai/artifact/YWatJC14K7odmKowZNh6ef) | Ocre |
| Design system v1 (fundamentos y tokens, ya no se usa) | `design-system/` | [MotoT](https://claude.ai/artifact/ChhjnhW1oZQ8TdfbXuPptg) | Ocre (Geist) |

### 7.1 Inicio de sesión (`login/`)

Login · Error («El correo o la contraseña no son correctos») · Usuario dado de baja · Cargando · Recuperar contraseña · Enlace enviado.
En computadora, tarjeta blanca centrada de 400 px; en celular, pantalla completa en blanco. El aviso de baja va en amarillo de aviso para distinguirlo del error de datos.

### 7.2 Motos (`motos-lista/`, `motos/`)

Lista · Buscando («ital») · Sin resultados («XYZ») · Lista vacía · Detalle · Detalle sin chofer · Elegir chofer · Registrar · Corregir · Error placa vacía · Error placa repetida · Moto registrada (aviso).
Decisiones: botón flotante «+» redondo de 56 px; en la búsqueda se resalta el texto encontrado y aparece una X para borrar; en la lista vacía no se muestra el buscador ni el contador. En computadora el detalle va en dos columnas (datos y chofer a la izquierda, liquidaciones a la derecha).

### 7.3 Choferes (`choferes-lista/`, `choferes-detalle/`)

Lista · Buscando («55 23») · Sin resultados («Roberto») · Lista vacía · Detalle · Detalle sin moto · Registrar · Corregir · Con errores · Chofer registrado (aviso).
Decisiones: en la tarjeta de celular, nombre y placa (o «Sin moto») en la primera línea, luego el teléfono como enlace de 44 px que llama, y el domicilio al final; el teléfono es un enlace aparte encima de la tarjeta. Botón «Llamar» solo en celular. El campo Teléfono usa teclado numérico y la ayuda «10 números», que se cambia por el error cuando aplica. En celular «Corregir datos» va a la derecha de la barra superior.

### 7.4 Financiamiento (`financiamiento/`, solo Gerente)

Lista · Sin resultados · Lista vacía · Detalle · Registrar · Elegir fecha (calendario) · Corregir · Con errores · Financiamiento registrado (aviso).
Decisiones: en celular, pestañas «Usuarios | Financiamiento» dentro de Administración con la activa marcada en naranja; calendario como hoja inferior en celular y recuadro bajo el campo en computadora, semana de domingo a sábado; monto con prefijo $ fijo y teclado decimal; tras guardar se abre el detalle del financiamiento nuevo con el aviso.

### 7.5 Liquidaciones (`liquidaciones/`)

Es la pantalla de inicio. Historial agrupado por día («Hoy», «Ayer») · Buscando («Juan») · Sin resultados («Roberto») · Lista vacía · Registrar · Elegir moto · Fecha con calendario · Monto con teclado numérico · Con errores · Liquidación registrada (aviso) · Detalle · Corregir.
El 14 oct 2026 se eligió la antigua v2 como versión oficial y se borró la v1. Decisiones:

- Sin contador bajo el título (el brief excluye totales).
- Monto del detalle con el tamaño de título del sistema (la v1 usaba 40 px).
- Buscador con botón para borrar.
- Lista vacía sin buscador ni botón flotante.
- Detalle en computadora con Moto y Chofer en dos tarjetas lado a lado y «Corregir» dentro de la tarjeta del monto.
- Formulario en una sola columna también en computadora.
- Aviso de éxito en celular sin botón de cerrar.
- La liquidación nueva se resalta con fondo naranja claro y etiqueta «Nueva» con punto naranja.

Además: botón flotante extendido «+ Registrar liquidación» encima de la barra inferior (sube cuando aparece el aviso); registrar en celular es pantalla completa sin barra inferior y en computadora panel derecho de 480 px; elegir moto con «Sin chofer» en 45-PQR-2.

### 7.6 Usuarios (`usuarios/`, Administración)

Vista Gerente · Menú de tres puntos (celular) · Vista Ayudante · Dar de alta · Con errores · Correo repetido · Confirmar baja · Usuario dado de alta (aviso) · Usuario dado de baja (aviso) · Sin resultados.
Decisiones: la persona con la sesión aparece con «(tú)» y no puede darse de baja a sí misma; el rol viene marcado en Ayudante al abrir el formulario; en celular «Dar de baja» y «Volver a dar de alta» van en el menú de tres puntos; el Ayudante ve el aviso informativo «Solo el Gerente puede dar altas y bajas de usuarios.» con fondo suave del primario, y en celular no ve las pestañas porque solo tiene Usuarios.

## 8. Datos de ejemplo

Ficticios, usados en todas las pantallas en lugar de lorem ipsum.

- **Motos:** 27-ABC-4 · Italika FT150 · Juan Pérez López | 31-XKT-8 · Honda CGL 125 · María González Ruiz | 12-MNO-5 · Yamaha YBR 125 · Luis Hernández Soto | 45-PQR-2 · Italika DM150 · sin chofer.
- **Choferes:** Juan Pérez López · 55 1234 5678 · Calle Hidalgo 45, Col. Centro | María González Ruiz · 55 2345 6789 · Av. Juárez 120, Col. Moderna | Luis Hernández Soto · 55 3456 7890 · Calle Morelos 8, Col. Obrera | Carlos Ramírez Díaz · 55 4567 8901 · Calle Allende 33, Col. Del Valle · sin moto.
- **Liquidaciones:** 13 oct 2026 · 27-ABC-4 · Juan · $350.00 | 13 oct 2026 · 31-XKT-8 · María · $350.00 | 12 oct 2026 · 12-MNO-5 · Luis · $300.00 | 12 oct 2026 · 27-ABC-4 · Juan · $350.00.
- **Financiamientos:** 27-ABC-4 · 1 mar 2026 · $28,500.00 | 31-XKT-8 · 15 jun 2026 · $32,000.00.
- **Usuarios:** Laura Méndez · laura@ejemplo.com · Gerente · Alta | Pedro Martínez · pedro@ejemplo.com · Ayudante · Alta | Sofía Torres · sofia@ejemplo.com · Ayudante · Baja.

## 9. Pendientes para cerrar la fase 0

1. Unificar los neutros y tamaños: las pantallas usan los neutros fríos y la tipografía de sus briefs (fondo `#F7F8FA`, títulos 24/32), mientras el login y las hojas usan los neutros cálidos del design system v2 (fondo `#FAFAF9`, títulos 22/28).
2. Aún no hay logotipo propio; se usa el logo de texto «CRM-MotoT» con el icono bike.
