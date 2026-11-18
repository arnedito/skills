---
name: charlas-charlie
description: Identidad visual y caja de herramientas de las presentaciones de Carlos en Beamer/LaTeX (6 temas con selector, portada con logos HARMONIE/BSC, fondos low-poly de pulmones o nariz, figuras matplotlib con el mismo estilo, plantillas de diagramas TikZ y verificación renderizando cada slide). Úsala SIEMPRE que se trabaje en una charla, presentación, slides, diapositivas, Beamer, una figura o un diagrama para slides, o un póster/handout con su estilo, aunque no se nombre la skill — crear una charla nueva, añadir o pulir slides, arreglar algo que se ve mal, cambiar de tema o de fondo, hacer una figura o un esquema para una slide.
---

# charlas-charlie

El estilo de las charlas de Carlos y cómo trabajar con él. La copia canónica del estilo vive en
`assets/estilo/`; cada charla lleva **su propia copia** en `estilo/`, para que las charlas viejas no se
rompan cuando el estilo cambie.

`SKILL` = la carpeta de esta skill (la que contiene este fichero).

## Cuándo cargar otra skill

Casi siempre esta skill basta. Carga otra solo en estos casos:

| Situación | Skill |
|---|---|
| Guion desde cero o formato nuevo (estructura, tiempos, narrativa a fondo) | `scientific-slides` |
| La charla sale de un paper (y notas del orador) | `presenting-conference-talks` |
| «Esto está feo»: crítica visual a fondo | `impeccable` (sus criterios; sus scripts son de web) |
| Cualquier diagrama o dibujo TikZ (criterios, plantillas, verificación) | `tikz-charlie` |
| Sintaxis TikZ rara que no esté en `tikz-charlie` | `tikz-cheatsheet` |

## Arranque

**Charla nueva**:

```sh
SKILL/scripts/nueva_charla.sh <carpeta> [--tema bloques] [--idioma english|spanish] [--titulo "..."]
```

Monta `main.tex` (portada con logos), `estilo/` (copia, con la versión en `estilo/VERSION`), `figs/`,
`diagramas/`, `make_figs.py` y `BRIEF.md`. Antes de escribir slides, rellena `BRIEF.md` con lo que el
usuario ya haya dicho (público, duración, idioma, mensaje, bloques) y pregunta solo lo que falte y cambie
la charla. Si la carpeta del proyecto tiene `GLOSSARY.md` (nombres de casos, vocabulario), úsalo: los
nombres de casos y los colores de cada proyecto no van en esta skill.

**Charla existente**: lee `main.tex` y mira qué estilo usa (`estilo/VERSION`, o `\input@path`). No migres
una charla vieja al estilo nuevo salvo que te lo pidan; si te lo piden, compara `estilo/` con
`SKILL/assets/estilo/` antes de copiar y apunta la versión nueva en `estilo/VERSION`.

## Parámetros (en `main.tex`, antes de `\input{preambulo}`)

| Macro | Valores (el primero es el de por defecto) |
|---|---|
| `\def\tema{…}` | `bloques` · `metropolis` · `clasico` · `tufte` · `oscuro` · `editorial` |
| `\def\idioma{…}` | `english` · `spanish` |
| `\def\logos{…}` | `harmonie,bsc` · también `harmonie-favicon` (solo el pulmón) y `upc` · vacío = sin logos |
| `\def\logoportada{…}`, `\def\logopie{…}` | `auto` (color en fondo claro, blanco en oscuro) · `color` · `azul` · `negro` · `blanco` · `tenue` (auto al 45 %) |
| `\def\tamlogos{…}` | `normal` · `pequeno` · `grande` |
| `\def\letra{…}` | `palatino` · `charter` · `sans` · `lmodern` |
| `\def\fondoportada{…}` | vacío · `pulmones` · `pulmones-azul`/`-rojo`/`-turquesa`/`-violeta`/`-aire` (colores fijos, fondos claros) · `nariz` · `nariz-llena` · `nariz-silueta` · `vias` · `acino` · `pulmones-original` · `malla`/`remolinos`/`espectro`/`curvas` (PDF blancos: solo portadas oscuras) · ruta a una imagen del proyecto |
| `\def\fondoseccion{…}` | igual que `\fondoportada` |
| `\def\progreso{…}` | `numeros` (n / N) · `barra` (barra fina en el pie) · `ambos` |
| `\def\sangrado{…}` | `poco` (1,2 cm) · `mucho` (2,6 cm) · `0cm` · cualquier medida |
| `\def\nbloques{N}` | Bloques: secciones con letra y color; las posteriores (cierre, apéndice) van en neutro |
| `\def\connotas{}` | notas del orador en pantalla aparte |

Los logos van grandes en la portada y pequeños (0,35 cm) en el pie de las slides de contenido; no salen
en los separadores ni en las slides-frase (`\frase` los oculta; `\ocultarlogos` lo hace en cualquier slide).
Detalle de cada tema, paleta y cómo añadir un logo o un fondo: `references/temas.md`.

## Cómo se trabaja

1. **Estructura antes que slides.** Bloques con letra y color, una idea por slide, ~1 min por slide.
   Resumen de narrativa más abajo; a fondo, `references/narrativa.md`.
2. **Slides.** Título = mensaje (una frase que se pueda discutir, no un tema). Macros del preámbulo:
   `\frase{}` (slide-frase que cierra un bloque, en un frame `[c]`), `\mensaje{}`, `\caso{}` (nombres de
   casos en versalitas), `\figura{fichero}{ancho}{alto}{qué falta}` (si la figura no existe deja un hueco
   rotulado: la charla compila desde el primer día).
3. **Figuras de datos**: matplotlib con `make_figs.py`, al tamaño final y sin escalar. `references/figuras.md`.
4. **Esquemas**: carga la skill `tikz-charlie` (criterios, plantillas y `diagrama.sh`). En la charla van en
   `diagramas/<nombre>.tex` con `\input`; lo propio de slides, en `references/diagramas.md`.
5. **Verificar mirando** (abajo). Siempre.

## Narrativa en corto

- El título de cada slide es el mensaje; el cuerpo lo demuestra.
- Una idea por slide; si hay dos, son dos slides.
- ~1 minuto por slide: una charla de 20 min tiene ~18–22 slides más apéndice.
- Bloques con letra y color (tema Bloques: `\section{}` y `\nbloques`); cada bloque cierra con una
  slide-frase que dice lo que el bloque ha demostrado.
- Cierre: tres mensajes como mucho. El detalle que no cabe va al apéndice (`\appendix`), no a letra pequeña.

## Criterios de diseño en corto

Las **preferencias de Carlos pesan más que las reglas** genéricas: borde negro (tinta, 0,6 pt) en las
cajas de flujo, fondos low-poly en portada y separadores, nombres de solvers y de métodos sin traducir
(MOMENTUM, CONTINUITY, ASGS, OSS, Vreman…). Por lo demás:

- Jerarquía con 2–3 tamaños por slide; el color de acento solo para lo que hay que mirar.
- Separar con tono (rellenos `color!12!fondo`, texto `tenue`) antes que con líneas o recuadros.
- Poca tinta que no sea dato: sin rejillas, sin marcos de gráfico, leyendas pegadas a las curvas.
- Nada de filas de tarjetas iguales «porque sí»; la forma del esquema cuenta la estructura.
- Tintes siempre mezclados con `fondo` (`serieA!12!fondo`), nunca con blanco: así funcionan en `oscuro`.
- Tablas: `booktabs`, cabecera en `tenue`, como mucho ~9 filas legibles; si hay más, dos slides.
- Título en una línea (~50 caracteres); ~6 cm útiles de alto para el cuerpo. Portada: título y subtítulo ≤ 2 líneas.

Más, con ejemplos: `references/diseno.md`.

## Verificar: mirar cada slide renderizada

Nada está hecho hasta que lo has visto. Después de cada cambio:

```sh
SKILL/scripts/compilar.sh main.tex          # errores, cajas que se salen, ficheros que faltan
SKILL/scripts/hoja_contactos.sh main.pdf    # todas las slides en una imagen: ritmo y lo que desentona
SKILL/scripts/renderizar.sh main.pdf 110 [desde hasta]   # PNG por slide en render/, para mirar el detalle
```

Abre las PNG con la herramienta de lectura de imágenes y mira **cada slide que has tocado** a 110 dpi:
texto que se sale o se corta, solapes con el pie o los logos, figuras escaladas (texto de la figura más
grande o más pequeño que el de la slide), contraste (sobre todo en `oscuro`), huecos `\figura` que
quedaron. Para elegir o cambiar tema: `SKILL/scripts/comparar_temas.sh main.tex 6 [temas…]` da una
imagen con las primeras slides en cada tema.

Si algo no se ve bien, arréglalo y vuelve a mirar. Di al usuario qué has mirado y qué queda pendiente.

## Trampas que ya costaron tiempo

- `\begin{frame}{Título}{…}`: un grupo justo después del título es el **subtítulo**. Empieza el contenido
  con `\noindent` o `\par` (o deja una línea en blanco).
- `#` dentro de un frame (estilos TikZ con `#1`) rompe la compilación: el dibujo va en un fichero aparte con `\input`.
- TikZ anidado (`\tikz` dentro de un nodo con `text width`/`minimum height`) hereda esas opciones:
  resetea con `minimum height=0pt, minimum width=0pt, text width={}`.
- Una figura no puede llamarse como el `-jobname` del PDF (pdflatex intenta incluirse a sí mismo).
- `\section*` también dispara `\AtBeginSection`: cierre y apéndice van como secciones después de `\nbloques`.

Lista completa (TikZ, matplotlib, transparencias, Python): `references/trampas.md`.

## Referencias

| Fichero | Cuándo leerlo |
|---|---|
| `references/temas.md` | elegir o cambiar tema, paleta, logos, fondos, añadir un logo o un fondo low-poly |
| `references/diagramas.md` | diagramas dentro de una charla (el resto, en `tikz-charlie`) |
| `references/figuras.md` | figuras matplotlib: estilo, tamaños por tema, familias de color |
| `references/diseno.md` | pulir o criticar una slide; criterios con ejemplos |
| `references/narrativa.md` | estructura de una charla, bloques, tiempos, apéndice, notas |
| `references/trampas.md` | algo falla al compilar o se dibuja raro |

Scripts en `SKILL/scripts/`: `nueva_charla.sh`, `compilar.sh`, `renderizar.sh`, `hoja_contactos.sh`,
`comparar_temas.sh`, `lowpoly.py` (fondos low-poly desde una silueta o un render), `preparar_logos.py`.
Python con matplotlib y LaTeX (en el Mac de Carlos: `~/miniforge3/envs/aire/bin/python`).
