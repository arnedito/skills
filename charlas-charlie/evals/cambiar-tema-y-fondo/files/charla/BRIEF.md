# Brief: charla

Decisiones de esta charla. Se rellena al empezar y se actualiza cuando algo se cierra.

- **Público y contexto**: técnico (métodos numéricos / CFD); charla corta de grupo o seminario. Supuesto: no se preguntó.
- **Duración y nº de slides**: ~6 min, portada + 6 slides de contenido (~1 min por slide).
- **Idioma**: inglés (`\def\idioma{english}`).
- **Tema**: `clasico`. «Tema clásico» se leyó como el tema visual Clásico; el contenido (Newton vs Picard) es además el «tema clásico» de la petición, así que sirve para las dos lecturas.
- **Mensaje principal** (una frase): Picard se frena al crecer la no linealidad y acaba estancándose; Newton se queda en 5–8 iteraciones y compensa en cuanto su paso cuesta menos de 2× uno de Picard.
- **Bloques**: ninguno. Con 6 slides, `\section` añadiría separadores «Part I…» en Clásico y doblaría la longitud; va como un único hilo: problema → bucle (diagrama) → teoría → figura → coste → cierre.
- **Figuras y de dónde salen los datos**: todo sale de `make_figs.py`, con datos sintéticos de un problema modelo calculado de verdad, no inventado:
  `-(k(u) u')' = 20` en (0,1), u = 0 en los bordes, `k(u) = k0 + u²`, diferencias finitas, 199 nodos.
  Ambos métodos arrancan de la solución lineal (k = 1) y se mide `||R(u^k)|| / ||R(u^0)||`.
  - `figs/convergencia.pdf`: residuo frente a iteración, Picard (serieA) y Newton (serieD), un tono por k0 ∈ {1, 0.3, 0.1}; Picard con k0 = 0.05 punteado en `tenue` (oscila, no converge).
  - `figs/perfiles.pdf`: u(x) convergida para cada k0 (media columna).
  - Tabla de la slide 6: `python make_figs.py tabla` imprime las iteraciones hasta 1e-8 (11/5, 17/5, 33/7, —/8). El coste por paso de Newton de 1,5–2× es una cifra típica (GMRES frente a CG), **no está medido** (en 1D se usa un solver directo); viene indicado en la nota del orador.
- **Diagrama**: `diagramas/iteracion.tex`, sale de la plantilla `flujo.tex` (cajas con borde negro, marco gris de la iteración, flecha de vuelta en `acento` con la condición).
- **Fondo de portada**: `pulmones` (identidad de Carlos), aunque el tema no va de pulmones.
- **Glosario del proyecto**: no hay.

## Estado
Compilada (7 páginas), sin cajas desbordadas; las 7 slides revisadas a 110 dpi. Pendiente si se quiere: tiempos reales por paso (2D/3D con solver iterativo) para sustituir la cifra típica de 1,5–2×.
