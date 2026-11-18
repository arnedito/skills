# Figuras matplotlib con el estilo de las slides

## El patrón (`make_figs.py` de la plantilla)

- Estilo: `plt.style.use([estilo/charla.mplstyle, estilo/charla-<tema>.mplstyle])`. El base pone Palatino
  vía LaTeX (`text.usetex` + mathpazo: la misma letra que las slides), fondo transparente, sin marco
  arriba ni a la derecha, sin rejilla, ejes finos. El del tema pone los colores (`serieA`…`serieD`, tinta, tenue).
- El tema se lee de `main.tex`: si cambias el tema, **vuelve a ejecutar `make_figs.py`** y recompila.
- **Tamaño final**: la figura se exporta al ancho que va a ocupar y se incluye sin escalar
  (`\includegraphics{figs/x.pdf}` o `\figura{figs/x.pdf}{\linewidth}{5cm}{…}` con el mismo ancho). Así
  el texto de la figura (8–9 pt) casa con el de la slide. Ojo: `\figura{…}{\linewidth}{…}` usa
  `keepaspectratio` y **reescala** al ancho dado; para una figura ya a tamaño final, `\includegraphics{figs/x.pdf}`
  sin opciones (o `\figura` con el ancho real de la figura). `bbox: tight` recorta unos mm: normal. Área útil (16 cm menos márgenes):

  | Tema | bloques | metropolis | clasico | tufte | oscuro | editorial |
  |---|---|---|---|---|---|---|
  | Ancho útil (cm) | 13,8 | 14,6 | 14,0 | 13,0 | 14,0 | 13,6 |

  Media slide (columna de 0,5\textwidth): la mitad menos ~0,3 cm. Alto típico: 4,5–5,5 cm con título
  de slide; ~6,5 cm sin texto debajo.
- PDF vectorial en `figs/`. PNG solo para renders e imágenes (con fondo transparente si van sobre color).

## Color

- Un color por familia (método, caso); dentro de la familia, tonos con `tono(color, i, n)` (mezcla con el
  fondo del tema, no con blanco): de suave
  (malla gruesa, menos importante) a pleno (malla fina, lo importante).
- La referencia (DNS, experimento) en `tinta`, con marcadores huecos (`mfc="none"`), por encima de las curvas.
- Líneas de guía (pendiente −5/3, ley lineal) en `tenue`, finas y discontinuas, con la etiqueta pegada.
- Mismos colores en la figura y en el texto de la slide que la comenta (`\textcolor{serieA}{…}`).

## Etiquetas

- Ejes con símbolo y unidades: `r"$f$ (Hz)"`. Nombres de casos en versalitas: `r"\textsc{imp asgs}"`.
- Leyenda sin marco y, si se puede, etiqueta pegada a la curva en vez de leyenda.
- Paneles: título corto a la izquierda (`axes.titlelocation: left`), no «(a)», salvo que se citen.

## Trampas

- Colores en `.mplstyle` **sin comillas** (`text.color: 1B1B2F`), salvo dentro de `cycler('color', ['2E5EAA', …])`.
- `text.usetex` necesita LaTeX en el PATH; en el Mac de Carlos, `~/miniforge3/envs/aire/bin/python`.
- `plt.style.use` acumula: si un script genera varios temas, haz `plt.style.use("default")` antes de cada uno.
- El nombre del PDF de la figura no puede coincidir con el `-jobname` de la charla.
- Quitar el fondo blanco a un PNG: alfa = f(255 − min(RGB)) con fundido suave; ojo, aclara los trazos claros.
