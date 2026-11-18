# Criterios estéticos para diagramas TikZ

Destilado de: `impeccable` (IMP), `taste-skill/design-taste-frontend` (TASTE), `emil-design-eng` (EMIL),
`ui-craft` (UIC), `apple-design` (APPLE), `diagram-design` (DD) y la casa (`diagramas.md`, `diseno.md` = CASA).
`emil-design-eng` apenas trae nada estático aplicable (es sobre todo movimiento y pulido de UI).
**Gana siempre la casa** (las preferencias de Carlos): borde negro en las cajas de flujo, flechas en `tinta`,
diseño plano, solvers sin traducir.

**Estilo por defecto (B)**: cajas neutras (`fill=fondo`, borde `tinta`), un solo foco en `acento`
(`fill=acento!10!fondo, draw=acento, line width=0.9pt`), grupo con tono sin borde, flechas ortogonales con
`rounded corners=4pt`, etiqueta del bucle sobre el trazo con `fill=fondo`. **Color por familia
(`serieX!12!fondo`) solo cuando el color significa algo** (tipos de solver, ingredientes, etapas distintas).
⚠ = choque con la casa (y cómo se resuelve).

## 1. Jerarquía

- **Un solo foco (1–2 elementos).** `acento` en 1–2 nodos o en la ruta principal; el resto en `tinta`/`tenue`.
  Si quieres acentuar 4 cosas, no has decidido qué importa. — DD (focal rule), UIC (presupuesto de acento), CASA.
- **La forma cuenta la estructura.** Cadena → `pipeline`, bucle → `flujo` con flecha de vuelta, árbol, matriz.
  Nada de filas de cajas iguales si las cosas no son paralelas. — DD, TASTE, CASA.
- **Jerarquía con peso antes que con tamaño.** Dentro de la caja: `\textbf` (qué es) / normal (qué hace) /
  `\color{tenue}` (detalle); un solo cambio de tamaño como mucho. — APPLE, UIC, CASA.
- **Se entiende en 3 segundos.** Si hace falta leer una leyenda para entenderlo, sobra algo. — DD (densidad 4/10), CASA.

## 2. Rejilla y espaciado

- **Toda la geometría en una rejilla.** `\def\dx{3.2cm}`, `at (k*\dx,0)`; separaciones múltiplo de 0,1 cm
  (equivalente TikZ de la rejilla de 4 px de DD). — DD, CASA.
- **Separaciones constantes y pocas.** Dos valores: entre cajas hermanas `0.4cm`, entre grupos `0.8–1cm`. — DD, IMP (layout).
- **Mismo tamaño en una fila.** `text width=2.5cm, minimum height=…` comunes vía estilo. — CASA.
- **Relleno interior uniforme.** `inner sep=5pt` en cajas, `1.4pt` en chips. — CASA, DD.
- **Cabe en el ancho útil.** ≤ 13–14,5 cm de ancho, ≤ 5–5,5 cm de alto con título; si no cabe, sobra contenido,
  no falta `\scalebox`. — CASA, DD (complexity budget: >9 nodos = dos diagramas).

## 3. Color

- **Color = familia, no adorno.** Un color por tipo de cosa (`serieA…D`), igual en toda la charla y las figuras.
  — CASA, DD (roles semánticos), UIC.
- **≥90 % neutro.** Fondo, `tinta` y `tenue` dominan; color en rellenos tenues `serieX!12!fondo`. — UIC, DD.
- **Tintes mezclados con `fondo`, nunca con blanco.** `!12!fondo` caja, `!35!fondo` relleno a escala,
  `tinta!4!fondo` grupo. — CASA (tema oscuro).
- **Cuidado: en algunos temas una serie coincide con `acento`** (Bloques: `serieB` = acento; Oscuro: `serieA` = acento).
  Si usas `acento` como foco, no uses esa serie para otra cosa. — pruebas.
- **Máx. 4 series por diagrama.** Más, con tonos de una familia o en paneles. — CASA, DD.
- **Sin degradados, brillos ni sombras.** `drop shadow`, `shading=` prohibidos. — TASTE, UIC, DD, CASA.
  ⚠ UIC/APPLE recomiendan sombras en capas para profundidad: no aplica a slides; gana la casa (plano).

## 4. Tipografía

- **2–3 niveles dentro del diagrama.** `\scriptsize`–`\footnotesize`; nunca < `\tiny` efectivo. — CASA, IMP.
- **Texto de la figura = texto de la slide.** Sin escalar el diagrama; si se usa `\resizebox`, comprobar ≥ `\tiny`. — CASA.
- **Mayúsculas sostenidas solo para etiquetas cortas.** Sentence case por defecto. — UIC, DD.
  ⚠ Los nombres de solver (MOMENTUM, CONTINUITY, ASGS, OSS) van tal cual en mayúscula y sin traducir: gana la casa.
- **Monoespaciada solo para lo técnico.** `\texttt` para ficheros, flags, claves de Alya; nombres en la fuente normal. — DD.
- **Matemáticas en modo matemático y en negrita vectorial coherente** (`\boldsymbol x`). — CASA.

## 5. Líneas y flechas

- **Una punta, un grosor.** `-{Stealth[length=5pt]}`, `line width=0.8pt`, `tinta`. — CASA.
  ⚠ DD pone flechas en `muted` por defecto: la casa usa `tinta`; aceptable `tenue` solo para flechas secundarias.
- **Flecha de vuelta / ruta principal en color.** `acento` o el de la familia, con la condición escrita al lado. — CASA, DD.
- **Discontinua = opcional, pasivo, retorno.** `dash pattern=on 3pt off 2pt`. — DD.
- **Ortogonales.** Codos `-|`/`|-` con `rounded corners=4pt`; recta solo si comparten x o y; diagonales no. — DD.
- **Sin solapes.** Rutas paralelas separadas ≥ 0,2 cm; cada flecha con su propio punto de enganche
  (`([xshift=±0.2cm]a.east)`). — DD (reglas de conector 3–4).
- **No pasar por detrás de una caja que no es extremo.** Reencaminar. — DD (regla 5).
- **Trazo de caja < trazo de flecha.** Caja `0.6pt`, flecha `0.8pt`, marco de grupo sin borde. — CASA, DD.

## 6. Cajas y contenedores

- **Caja de flujo: borde negro.** `draw=tinta, line width=0.6pt, rounded corners=2.5pt`, `fill=fondo` (o `serieX!12!fondo` si el color significa). — CASA.
  ⚠ DD/UIC: bordes finos y apagados (hairline). Gana la casa: borde `tinta`.
- **Radio pequeño.** 2–3 pt en cajas, 1,5 pt en chips; nunca cápsulas grandes. — DD (rx 6–10 px máx.), CASA.
  ⚠ UIC pide variar radios por elemento: en TikZ basta con dos (caja 3pt, chip 1.5pt).
- **Agrupar con tono, no con otro recuadro.** `on background layer`, `fit=`, `fill=tinta!4!fondo`, sin `draw`. — CASA, UIC.
- **Nada de cajas dentro de cajas dentro de cajas.** Máx. un nivel de anidamiento. — IMP, CASA.
- **Cada nodo, una idea.** Dos nodos que van siempre juntos son uno. — DD.

## 7. Etiquetas y anotaciones

- **Etiqueta de flecha separada del trazo.** `node[midway,above=2pt,fill=fondo,inner sep=1pt,font=\tiny]`;
  nunca encima de la línea. — DD (regla 2: hueco 6–10 px + máscara opaca).
- **Etiquetas cortas.** ≤ ~14 caracteres en flechas. — DD.
- **Etiqueta directa en lugar de leyenda.** Curvas rotuladas al final (`pos=1, right`); sin leyenda flotante. — CASA, DD.
- **Nada de texto vertical en flechas.** — DD.
- **Sobre imágenes: coordenadas relativas** a la imagen (`($(L.south west)+(0.42*\W,0.6*\H)$)`), zona resaltada
  con `fill=acento, fill opacity=0.15–0.25, draw=acento, line width=0.8pt`. — CASA, DD (callout).
- **Ejes esquemáticos.** `tenue`, con flecha, sin marcas salvo las nombradas, sin rejilla. — CASA.

## 8. Densidad y qué quitar

- **Densidad objetivo 4/10.** ≤ 9 nodos y ≤ 12 flechas; más, dividir en vista general + detalle. — DD.
- **¿Sobra alguna flecha?** Si la disposición ya dice la relación, quítala. — DD.
- **¿Sobra alguna etiqueta?** Si el color o la forma ya lo dicen, quítala. — DD.
- **Sin iconos decorativos.** Los fondos low-poly son la única decoración, y no van detrás de diagramas. — CASA, TASTE.
- **Está acabado cuando no se puede quitar nada.** — DD, IMP (distill).

## 9. Accesibilidad y contraste

- **Texto ≥ 4,5:1 sobre su relleno.** Con rellenos `!12!fondo` se cumple; con `!35!` o más revisar. — UIC, IMP, APPLE.
- **Texto sobre chip con `textochip`, nunca `white`.** — CASA.
- **Elementos gráficos ≥ 3:1** (flechas, bordes de foco): por eso `tinta` y no `tenue` para flechas principales. — UIC/WCAG.
- **No codificar solo con color.** Foco = color + grosor/negrita o etiqueta; discontinua para retorno. — DD, UIC.
- **Probar en tema `oscuro` y a 110 dpi** (`scripts/renderizar.sh`). — CASA, APPLE (`prefers-contrast`).

## 10. Anti-patrones

| Anti-patrón | En su lugar | Fuente |
|---|---|---|
| `acento` en 5 cajas | 1–2 focos | DD, UIC |
| Tres tarjetas iguales en fila «porque sí» | forma según la estructura | DD, TASTE, CASA |
| Recuadro dentro de recuadro | fondo `tinta!4!fondo` sin borde | CASA, UIC |
| Flechas diagonales cruzándose | codos ortogonales, rutas separadas | DD |
| Etiqueta encima del trazo | `fill=fondo`, `above=2pt` | DD |
| Leyenda flotando entre nodos | etiqueta directa | DD, CASA |
| `\scalebox` para que quepa | quitar contenido | CASA |
| Mezclar tintes con `white` | mezclar con `fondo` | CASA |
| Sombras, degradados, brillo | plano | TASTE, UIC, DD |
| `rounded corners=10pt` (cápsulas) | 2–3 pt | DD |
| Texto gris + pequeño + cursiva a la vez | una sola marca (`tenue`) | CASA, IMP |
| Traducir MOMENTUM, ASGS… | sin traducir, en chip o negrita | CASA |
