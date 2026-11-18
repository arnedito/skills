# Fuera de Beamer: papers, tesis, standalone

Las plantillas usan tokens de color. Fuera de una charla, defínelos con valores fijos:

```latex
\usepackage{tikz}
\input{colores-fijos}   % SKILL/assets/colores-fijos.tex: fondo blanco, tinta, tenue, acento, serieA..D, textochip
```

(Copia `colores-fijos.tex` junto al documento o añade su carpeta a `\input@path`.) Valores del tema Bloques
sobre blanco; si el documento tiene su paleta, cambia los HEX ahí y nada más.

Diferencias con las slides:
- **Tamaño**: al ancho de la columna (`\linewidth`, ~8,5 cm en dos columnas, ~15 cm en la tesis). Diseña a ese
  ancho; no escales un diagrama de slide.
- **Letra**: la del documento. Con la plantilla de la tesis (Palatino) casa sin cambios; `\footnotesize`
  en cajas, `\scriptsize` en etiquetas.
- **Imprenta en gris**: el foco tiene que distinguirse también por grosor (`line width=0.9pt`) o negrita, no solo
  por color.
- **Sin fondos low-poly ni logos.**
- Para un PDF suelto: `scripts/diagrama.sh fichero.tex` (modo `fijo`) da `fichero.pdf` recortado para `\includegraphics`.
