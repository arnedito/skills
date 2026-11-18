# tikz-charlie

Criterios estéticos, plantillas y verificación para diagramas **TikZ**, empaquetados como *skill* de
[Claude Code](https://claude.com/claude-code). Es la hermana de [`charlas-charlie`](../charlas-charlie)
(presentaciones Beamer), que la carga para los diagramas de las slides; sirve igual para papers y tesis.

![Plantillas](docs/galeria.png)

## El estilo

Un solo foco en color de acento, cajas neutras con borde negro, grupos marcados con tono (no con
recuadros), flechas ortogonales con esquinas redondeadas, etiquetas sobre el trazo con fondo, color solo
cuando significa algo y tintes mezclados con el fondo (funciona en temas oscuros). Los criterios salen de
skills de diseño (`impeccable`, `design-taste-frontend`, `ui-craft`, `apple-design`, `diagram-design`,
`emil-design-eng`) destilados para diagramas estáticos; las preferencias del autor ganan siempre.
Detalle: [`references/criterios.md`](references/criterios.md).

## Qué hay

```
SKILL.md                    instrucciones para Claude
assets/plantillas/          flujo, pipeline, selector, chips, imagen anotada, ejes, matriz, llamadas, elemento
assets/colores-fijos.tex    los tokens de color con valores fijos, para papers y tesis
references/                 criterios, patrones, trampas, fuera de Beamer
scripts/diagrama.sh         compila un diagrama suelto y lo renderiza a PNG
tests/                      pruebas con subagentes
```

## Uso

```sh
ln -s ~/skills/tikz-charlie ~/.claude/skills/tikz-charlie
cp ~/skills/tikz-charlie/assets/plantillas/flujo.tex mi-doc/diagramas/paso.tex
~/skills/tikz-charlie/scripts/diagrama.sh mi-doc/diagramas/paso.tex          # sobre blanco (colores fijos)
~/skills/tikz-charlie/scripts/diagrama.sh mi-doc/diagramas/paso.tex oscuro   # con un tema de charlas-charlie
```

En un documento LaTeX normal: `\usepackage{tikz}` + `\input{colores-fijos}` y `\input{diagramas/paso.tex}`.

Requisitos: `pdflatex`, `pdftoppm`; para los temas, `charlas-charlie` instalada al lado.

## Licencia

MIT.
