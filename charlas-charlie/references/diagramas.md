# Diagramas TikZ

Los criterios, las plantillas, las trampas y el script para renderizar un diagrama suelto viven en la skill
**`tikz-charlie`** (`~/.claude/skills/tikz-charlie`): cárgala para cualquier diagrama. Así hay un solo
criterio para slides, papers y tesis.

Lo propio de las slides:
- El diagrama va en `diagramas/<nombre>.tex` de la charla y se incluye con `\input{diagramas/<nombre>.tex}`
  (nunca pegado en el frame si tiene `#`). Las macros (`selector.tex`, `chips.tex`) se cargan en el preámbulo.
- Los colores son tokens del tema (`tinta`, `fondo`, `acento`, `serieA`…`serieD`, `textochip`): al cambiar de
  tema el diagrama cambia solo. En Bloques, el color del bloque actual es `bloqueactual`.
- Tamaño: ≤ 13–14,5 cm de ancho y ≤ 5–5,5 cm de alto con título.
- Después de compilar la charla, mira la slide renderizada (no solo el PNG del diagrama).

Ejemplos completos de una charla real (algoritmos de Alya, AIRE, ingredientes, recetas, apéndice):
`SKILL/assets/diagramas-charla01/`. Usan colores de ese proyecto (`ingEsq`…) y el estilo anterior (color
por familia en todas las cajas): al copiarlos, pásalos a tokens y al estilo de tikz-charlie.
