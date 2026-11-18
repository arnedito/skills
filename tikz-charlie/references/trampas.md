# Trampas de TikZ (ya resueltas)

- **`#` dentro de un frame de Beamer** (estilos con `#1`, `\newcommand` con parámetros) rompe la compilación:
  el diagrama va en un fichero aparte con `\input` (o `[fragile]` como último recurso).
- **TikZ anidado hereda opciones**: `\tikz` dentro de un nodo con `text width`/`minimum height` las hereda.
  Resetea con `minimum height=0pt, minimum width=0pt, text width={}`.
- **Los nombres de nodo son globales**: un chip `\tikz…\node(c){…}` dentro de una caja pisa a una caja `(c)`
  del diagrama y las flechas salen del sitio equivocado. Nombres raros para los internos (`etq@`, `chip@`).
- **`transparency group` suelto en un `overlay`** se queda sin caja y no se dibuja: mételo en un `\tikz`
  interno dentro de un nodo del overlay.
- **`\pgfmathparse` con ternario** no devuelve cadenas: `\pgfmathtruncatemacro` + `\ifnum`.
- **Comparar claves en macros**: `\ifnum\pdfstrcmp{#2}{#3}=0`.
- **Tintes con blanco** (`serieA!12`) salen claros en fondo oscuro: `serieA!12!fondo`.
- **Texto blanco sobre chips**: en el tema oscuro las series son claras; usa `text=textochip`.
- **Librerías cargadas** (preámbulo de charlas-charlie y `colores-fijos.tex`): `positioning, arrows.meta, calc, fit,
  backgrounds, matrix, fadings` (+ `patterns, decorations.pathreplacing` en colores-fijos). Otra, cárgala en el documento.
- **`on background layer`** necesita la librería `backgrounds`; `fit=` necesita `fit`.
- **Cajas de una fila con distinto alto** (el texto de una ocupa más) desalinean las flechas `a.east -- b.west`:
  `minimum height` común suficiente, o flechas a la misma altura (`(a.east) -- (a.east -| b.west)`).
- **Etiqueta encima del trazo**: `fill=fondo, inner sep=1pt` para que la línea no la cruce.
- **`\scalebox`/`\resizebox`** cambia el tamaño del texto: comprueba que sigue siendo legible.
- **Verifica renderizando**: compila no quiere decir que se vea bien (texto que se sale de su caja,
  flechas que cruzan texto). `scripts/diagrama.sh fichero.tex [tema]` y mira el PNG.
