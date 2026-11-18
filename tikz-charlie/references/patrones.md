# Patrones y plantillas

Las plantillas están en `assets/plantillas/`. Para empezar un diagrama, **copia la más parecida** y cambia
el contenido; no empieces de cero. Solo usan tokens de color (`tinta`, `tenue`, `fondo`, `acento`,
`serieA`…`serieD`, `textochip`), así que cambian solas con el tema de la charla. En `docs/galeria.png` se
ven todas.

| Fichero | Patrón | Para |
|---|---|---|
| `flujo.tex` | cajas con borde + un foco + marco gris de la iteración + flecha de vuelta con la condición + n → n+1 | un paso de un algoritmo, un bucle |
| `pipeline.tex` | cadena de cajas iguales + fila de salidas con rótulo; la novedad en acento | flujo de datos, herramientas |
| `selector.tex` | columnas de opciones (chips), una encendida por columna, unidas por un trazo | de qué se compone un caso; recorrer casos con `\only` |
| `chips.tex` | tabla `booktabs`, un caso por fila, chips solo donde se aparta de la referencia | mapa de casos |
| `imagen_anotada.tex` | imagen + zona resaltada en coordenadas relativas + flecha curva | de lo real al modelo |
| `ejes.tex` | ejes con flecha, curvas etiquetadas al final | una idea cualitativa (no datos) |
| `matriz.tex` | matriz por bloques a escala + operación | álgebra lineal |
| `llamadas.tex` | calles verticales por componente, chips en orden | secuencia de llamadas |
| `esquema_fisico.tex` | geometría a escala, cotas en tenue, ejes en una esquina, un foco | tubo, canal, dominio, condiciones de contorno |
| `elemento.tex` | elemento de malla con vecinos, nodos y lo de dentro | FEM, discretización |

Ejemplos completos de una charla real (algoritmos de Alya, AIRE, ingredientes, recetas, apéndice):
`charlas-charlie/assets/diagramas-charla01/` (usan colores de ese proyecto: cámbialos a tokens al copiar).

## Esqueleto mínimo (estilo B)

```latex
\begin{tikzpicture}[
    caja/.style={fill=fondo,draw=tinta,line width=0.6pt,rounded corners=2.5pt,align=left,
      inner sep=6pt,font=\scriptsize,text width=2.6cm,minimum height=2.2cm},
    foco/.style={caja,fill=acento!10!fondo,draw=acento,line width=0.9pt},
    flecha/.style={-{Stealth[length=5pt]},tinta,line width=0.8pt,rounded corners=4pt},
    rotulo/.style={font=\scriptsize,fill=fondo,inner sep=1pt}]
  \def\dx{3.4}
  \node[caja] (a) at (0,0)     {\textbf{1 · Paso}\\ qué hace\\ {\color{tenue}detalle}};
  \node[foco] (b) at (\dx,0)   {\textbf{2 · Lo importante}\\ $A\boldsymbol x = \boldsymbol b$};
  \draw[flecha] (a) -- (b);
\end{tikzpicture}
```

## Chip en línea (etiqueta de solver, caso)

```latex
\newcommand\etiqueta[2]{\tikz[baseline=(etq@.base)]\node[fill=#1,text=textochip,rounded corners=1.5pt,
  inner sep=1.4pt,font=\tiny\bfseries,minimum height=0pt,minimum width=0pt,text width={},align=center](etq@){#2};}
```

`baseline` lo alinea con el texto; el reset de `minimum…`/`text width` evita heredar el tamaño de la caja
que lo contiene; el nombre raro (`etq@`) evita pisar nodos del diagrama (los nombres son globales).

## Cotas (esquemas físicos)

```latex
cota/.style={{Stealth[length=3pt]}-{Stealth[length=3pt]},tenue,line width=0.4pt},
\draw[cota] (0,-0.4) -- (12,-0.4) node[midway,fill=fondo,inner sep=1pt,text=tinta,font=\small]{$L = 15R$};
```

## Una etapa hacia un grupo

Flecha ortogonal al borde del grupo (el nodo del `fit`), no a una caja concreta:
`\draw[flecha] (d.south) |- (salidas.east);`

## Tamaño

- En una slide: ≤ 13–14,5 cm de ancho y ≤ 5–5,5 cm de alto con título. Si no cabe, sobra contenido.
- El selector ocupa ~13,5 cm con 4 columnas; con 3, súbele `minimum width` y la separación; con 6, bájalas.
- Para otro ancho (p. ej. 15 cm en la tesis) cambia `\dx` y `text width` en proporción, no escales.
- No escales con `\resizebox` salvo como último recurso, y comprueba que el texto siga ≥ `\tiny`.
