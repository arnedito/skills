# Batería de pruebas

Cada prueba la hace un subagente que arranca de cero, en una carpeta temporal, con **solo la skill**
(sin ver otras charlas). Se miran los PDF renderizados, se corrige la skill y se repite. Los casos están
en `evals/` (formato de `claude plugin eval`); los resultados, en `../charlas-charlie-workspace/iteration-N/`.

| Caso | Qué se pide |
|---|---|
| `charla-ingles-clasico` | Charla corta en inglés, tema Clásico, 1 figura matplotlib (convergencia) y 1 diagrama de flujo con cajas y bucle |
| `charla-castellano-bloques` | Charla en castellano, tema Bloques: selector de ingredientes, tabla de chips, logos y pulmones en la portada |
| `cambiar-tema-y-fondo` | Coger la charla de la prueba 1 y pasarla a tema oscuro, nariz de fondo y barra de progreso |

## Iteración 1 (estilo 1.0.0)

**Qué salió**: las tres compilan, sin cajas desbordadas en la versión final; cada subagente miró sus
slides a 110 dpi. Las de la prueba 1 tenían datos reales (resolvió el problema 1D), la de la 2 tenía 15
frames y 18 páginas con el selector en 4 pasos, y la 3 quedó legible en oscuro tras los arreglos.

**Qué falló y se corrigió en la skill**:

| Problema (prueba) | Corrección |
|---|---|
| Separadores de Cierre/Apéndice en color en Bloques (2) | color `bloqueactual`, neutro tras `\nbloques` |
| `\etiqueta` de `flujo.tex` nombra su nodo `(c)` y choca con la caja `(c)` (2) | nombres internos `etq@`, `chip@`; trampa documentada |
| Título y subtítulo largos: la fecha pisaba los logos (2) | `\reservalogos` en todas las portadas; regla de ≤ 2 líneas |
| `\caso` dentro de `\frase` perdía las versalitas (2) | `\caso` en `\mdseries`; `compilar.sh` avisa de fuentes que faltan |
| `chips.tex` sin columna Esquema; nota del pie ensanchaba la tabla (2) | columna añadida; aviso en el comentario |
| Todos los títulos a dos líneas; slides desbordadas (1) | reglas: título ~50 caracteres, ~6 cm útiles de alto |
| `\figura{…}{\linewidth}` reescala la figura (1) | aviso en `figuras.md`: `\includegraphics` sin opciones |
| Plantilla con texto en castellano aunque se pida inglés; nombre de la carpeta en el título (1) | `nueva_charla.sh` respeta idioma y usa `--titulo` |
| Charlas cortas: ¿secciones? (1, 3) | `narrativa.md`: < 8 slides sin secciones |
| Texto blanco sobre chips claros en oscuro (3) | token `textochip` |
| `tono()` mezclaba con blanco: tono suave invisible en oscuro (3) | mezcla con el fondo del tema |
| Bloques: segunda línea del título debajo de la letra (revisión propia) | sangría francesa |
| Tintes `color!12` claros en oscuro (revisión propia, antes de la batería) | tintes `!N!fondo` en todas las plantillas |

## Iteración 2 (estilo 1.1.0)

**Qué salió**: las tres compilan sin errores ni desbordes y se leen bien (revisadas las hojas de contactos y
slides a 110 dpi). Ya no aparecen los fallos de la iteración 1. Quedan detalles menores:

| Problema (prueba) | Corrección |
|---|---|
| Plantillas con `textochip` rompían charlas con `estilo/` anterior (3) | `\providecolor` en las plantillas; `assets/estilo/VERSION`; lista para cambiar de tema en `temas.md` |
| Selector pequeño en 16:9 (2) | columnas y chips más anchos; guía de tamaño en `diagramas.md` |
| Sin datos para una figura (2) | regla: hueco `\figura` rotulado, no inventar |
| `\mensaje` tras una tabla se pegaba al lado (1) | `\mensaje` empieza párrafo |
| `make_figs.py` con un python sin matplotlib (1) | mensaje que dice qué python usar |

Pendiente (no bloquea): `flujo.tex` solo trae el bucle por abajo y sin ramas paralelas; no hay ayuda para
colocar etiquetas pegadas a las curvas en matplotlib.
