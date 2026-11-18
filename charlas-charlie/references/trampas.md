# Trampas ya resueltas

## Beamer

- **Subtítulo fantasma**: `\begin{frame}{Título}{…}`: un grupo `{…}` justo después del título es el
  subtítulo del frame. Los temas lo dibujan pequeño en `tenue`, pero si era contenido queda mal. Empieza
  el contenido con `\noindent`, `\par` o una línea en blanco.
- **`\section*` dispara `\AtBeginSection`** igual: el separador sale. Cierre y Apéndice van como
  secciones normales después de `\nbloques` (en Bloques salen en neutro, sin letra).
- **`#` dentro de un frame** (estilos TikZ con `#1`, `\newcommand` con parámetros) rompe la compilación:
  llévalo a un fichero aparte con `\input`, o usa `[fragile]` como último recurso.
- **El PDF no puede incluirse a sí mismo**: si una figura se llama como el `-jobname` (p. ej.
  `figs/main.pdf` con `main.tex`), pdflatex intenta incluir el PDF que está escribiendo.
- **Tablas largas**: 17 filas no caben legibles; parte en dos slides (≤ 9 filas cada una).
- **`\inserttotalframenumber`** vale 1 en la primera pasada: compila con `latexmk` (hace las pasadas que
  hagan falta) antes de mirar la barra de progreso o el «n / N».

## TikZ

- **TikZ anidado hereda opciones**: `\tikz` dentro de un nodo con `text width` o `minimum height` las
  hereda. Resetea con `minimum height=0pt, minimum width=0pt, text width={}`.
- **`transparency group` en un `overlay`** se queda sin caja y no se dibuja: mételo en un `\tikz`
  interno dentro de un nodo del overlay.
- **`\pgfmathparse` con ternario** no devuelve cadenas: `\pgfmathtruncatemacro` + `\ifnum`.
- **Tintes con blanco** (`serieA!12`) salen claros en el tema oscuro y el texto claro no se lee: usa
  `serieA!12!fondo`.

## Imágenes

- **Quitar el fondo blanco** a un PNG/PDF raster: alfa = f(255 − min(RGB)) con fundido suave. Aclara los
  trazos de color claro; revisa el resultado sobre el fondo de la slide.
- Los motivos PDF (`malla`, `remolinos`…) son blancos: sobre fondo claro no se ven.

## Python y matplotlib

- Cadenas multilínea dentro de `python3 - <<EOF`: usa `'''…'''` o concatena; las comillas triples dobles
  chocan con el heredoc si hay `$`.
- `text.usetex` + mathpazo da la misma Palatino que las slides.
- En `.mplstyle`, colores **sin comillas** (`text.color: 1B1B2F`), salvo en `cycler(...)`.
- Exporta la figura al tamaño final (13,8 cm de ancho útil en Bloques) y no la escales al incluirla.
- `plt.style.use` acumula estilos entre llamadas: `plt.style.use("default")` antes de cambiar de tema.

## Shell

- En macOS, `echo '\par'` en `sh` interpreta `\p`… y `\v` (tabulador vertical): para escribir LaTeX
  desde un script usa `printf '%s\n' '…'` o un heredoc con comillas (`<<'EOF'`).
- En zsh, `set -- $var` no parte por espacios: usa `bash -c` o arrays.
