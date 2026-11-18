# Diagramas TikZ: plantillas y estilo

## Contenido
1. Cómo se usan las plantillas
2. Las plantillas
3. Estilo de la casa (cajas, flechas, texto, color)
4. Trampas de TikZ en Beamer

## 1. Cómo se usan

Cada diagrama vive en `diagramas/<nombre>.tex` de la charla y se incluye con `\input{diagramas/<nombre>.tex}`
dentro del frame (o en el preámbulo si define macros). Para empezar uno, **copia la plantilla más
parecida** de `SKILL/assets/diagramas/` y cambia el contenido; no empieces de cero. Las plantillas usan
solo tokens del tema (`tinta`, `tenue`, `fondo`, `acento`, `serieA`…`serieD`), así que cambian solas
con el tema. En `docs/diagramas.png` se ven todas.

`SKILL/assets/diagramas/charla01/` guarda los originales de la charla del pipe (algoritmos de Alya, AIRE,
ingredientes, recetas, apéndice) como ejemplos completos. Usan colores de ese proyecto (`ingEsq`,
`ingTau`…): al copiarlos, cámbialos por `serieA`…`serieD` y sus tintes de `!N` a `!N!fondo`.

## 2. Plantillas

| Fichero | Patrón | Para |
|---|---|---|
| `flujo.tex` | cajas con borde negro + marco gris de la iteración + flecha de vuelta con la condición + entrada/salida n → n+1 | un paso de un algoritmo, un bucle |
| `pipeline.tex` | cadena de cajas iguales + fila de salidas con rótulo | flujo de datos, herramientas |
| `selector.tex` | columnas de opciones (chips), una encendida por columna, unidas por un trazo; la receta debajo | explicar de qué se compone un caso; recorrer casos con `\only` |
| `chips.tex` | tabla `booktabs`, un caso por fila, chips solo donde se aparta de lo básico | mapa de todos los casos |
| `imagen_anotada.tex` | imagen + zona resaltada en coordenadas relativas + flecha curva a otro elemento | de lo real al modelo, señalar una región |
| `ejes.tex` | ejes con flecha, curvas de color etiquetadas al final | una idea cualitativa (no datos) |
| `matriz.tex` | matriz por bloques a escala + operación | álgebra lineal, sistemas por bloques |
| `llamadas.tex` | calles verticales por componente, chips en orden | secuencia de llamadas, protocolo |
| `elemento.tex` | elemento de malla con vecinos, nodos y lo que vive dentro | FEM, discretización |

### Esqueleto mínimo de una caja de flujo

```latex
\begin{tikzpicture}[
    caja/.style={fill=#1!12!fondo,draw=tinta,line width=0.6pt,rounded corners=3pt,align=left,
      inner sep=5pt,font=\scriptsize,text width=2.5cm,minimum height=2.4cm},
    flecha/.style={-{Stealth[length=5pt]},tinta,line width=0.8pt}]
  \node[caja=serieA] (a) at (0,0) {\textbf{1 · Paso}\\ qué hace\\ {\color{tenue}detalle}};
  \node[caja=serieC,right=0.4cm of a] (b) {\textbf{2 · Paso}\\ $A\boldsymbol x = \boldsymbol b$};
  \draw[flecha] (a) -- (b);
\end{tikzpicture}
```

### Chip en línea (etiqueta de solver, caso)

```latex
\newcommand\etiqueta[2]{\tikz[baseline=(c.base)]\node[fill=#1,text=white,rounded corners=1.5pt,
  inner sep=1.4pt,font=\tiny\bfseries,minimum height=0pt,minimum width=0pt,text width={},align=center](c){#2};}
```

`baseline=(c.base)` lo alinea con el texto; el reset de `minimum…`/`text width` evita heredar el tamaño
de la caja que lo contiene.

## 3. Estilo de la casa

Preferencias de Carlos primero:
- **Cajas de flujo con borde negro**: `draw=tinta, line width=0.6pt, rounded corners=3pt`, relleno
  `color!12!fondo`. Todas las cajas de una misma fila, del mismo tamaño (`text width` + `minimum height`).
- Nombres de solvers y métodos **sin traducir** y en chip o en negrita: MOMENTUM, CONTINUITY, ASGS, OSS.

Además:
- **Color = familia.** Un color por tipo de cosa (etapa, solver, ingrediente), el mismo en todo la charla
  y en las figuras. La novedad o lo que hay que mirar, en `acento` o en otro color de serie.
- **Texto sobre chips**: `text=textochip` (blanco en temas claros, oscuro en `oscuro`), nunca `white`.
- **Tintes con `fondo`**: `serieA!12!fondo` (relleno de caja), `!35!fondo` (relleno a escala, matrices),
  `tinta!4!fondo` (marco de grupo). Mezclar con blanco rompe el tema oscuro.
- **Separar con tono antes que con líneas**: un grupo se marca con un fondo `tinta!4!fondo` sin borde
  (`on background layer`, `fit=`), no con otro recuadro.
- **Flechas**: `-{Stealth[length=5pt]}`, `tinta`, 0,8 pt; la flecha de vuelta de un bucle, en color
  (`acento` o el de la familia) con la condición escrita junto a ella.
- **Texto**: tres niveles como mucho dentro del diagrama: negrita (qué es), normal (qué hace), `tenue`
  (detalle). Tamaños `\scriptsize`–`\footnotesize`; nada por debajo de `\tiny`.
- **Ejes esquemáticos**: en `tenue` con flecha, sin marcas salvo las que se nombran; etiqueta al final de
  cada curva, sin leyenda.
- **Coordenadas**: rejillas con `\def\dx{…}` y `at (k*\dx,0)`, o `right=0.4cm of …`; sobre imágenes,
  coordenadas relativas (`($(L.south west)+(0.42*\W,0.6*\H)$)`).
- **Que quepa**: un diagrama ocupa como mucho el ancho útil (~13–14,5 cm) y deja sitio al título. Si no
  cabe, sobra contenido, no falta `\scalebox`. Si hay que escalar, `\resizebox{\linewidth}{!}{…}` y
  comprobar que el texto sigue siendo ≥ `\tiny` efectivo.

## 4. Trampas

- `#` dentro de un frame (estilos con `#1`, macros con parámetros) rompe la compilación: el diagrama va en
  un fichero aparte y se incluye con `\input`.
- TikZ anidado hereda `text width`/`minimum height` del nodo exterior: resetéalos en el interior.
- `transparency group` suelto dentro de un `overlay` se queda sin caja y no se dibuja: mételo en un
  `\tikz` interno dentro de un nodo del overlay (así lo hace `\fondo`).
- `\pgfmathparse` con ternario no devuelve cadenas: usa `\pgfmathtruncatemacro` + `\ifnum`.
- **Los nombres de nodo son globales**: un chip en línea `\tikz…\node(c){…}` pisa a una caja `(c)`
  del diagrama. Dale a los nodos internos nombres raros (`etq@`, `chip@`).
- Comparar claves en macros: `\ifnum\pdfstrcmp{#2}{#3}=0` (como en `selector.tex`).
- `on background layer` necesita `\usetikzlibrary{backgrounds}` (ya está en el preámbulo, con
  `positioning, arrows.meta, calc, fit, matrix, fadings`).
- Verifica renderizando: un diagrama que compila puede tener texto que se sale de su caja o flechas que
  cruzan texto. Míralo a 110 dpi (`scripts/renderizar.sh main.pdf 110 n n`).

## Tamaño y huecos sin datos

- El selector ocupa ~13,5 cm con 4 columnas; con 3, súbele `minimum width` y la separación (`3.4*#2`);
  con 6, bájalas. No lo escales con `\resizebox` (el texto quedaría pequeño).
- Sin datos para una figura: `\figura` con el hueco rotulado (qué va y de qué datos). No inventes resultados
  salvo que lo pidan, y dilo en la respuesta.
