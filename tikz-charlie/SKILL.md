---
name: tikz-charlie
description: Criterios estéticos y plantillas para dibujar diagramas y esquemas en TikZ con el estilo de Carlos (cajas con borde negro, un solo foco, rejilla, flechas ortogonales redondeadas, color con significado, tintes mezclados con el fondo) y verificarlos renderizando. Úsala SIEMPRE que haya que dibujar, arreglar o pulir un diagrama, esquema, dibujo o figura en TikZ — para slides (la carga charlas-charlie), para un paper o para la tesis — aunque no se nombre la skill: diagramas de flujo, pipelines, bucles de algoritmos, esquemas físicos, matrices por bloques, imágenes anotadas, «hazme un dibujito de…».
---

# tikz-charlie

Cómo dibuja Carlos en TikZ. Complementa a `charlas-charlie` (que la carga para los diagramas de las
slides) y sirve igual para papers y tesis. `SKILL` = la carpeta de esta skill.

Para sintaxis TikZ rara que no esté aquí, `tikz-cheatsheet`. Para criticar un diseño a fondo, los
criterios de `impeccable`.

## El estilo en corto (estilo B)

Las **preferencias de Carlos ganan** a cualquier regla genérica: borde negro (`tinta`, 0,6 pt) en las cajas
de flujo, flechas en `tinta`, diseño plano (sin sombras ni degradados), nombres de solvers y métodos en
mayúscula y sin traducir (MOMENTUM, CONTINUITY, ASGS, OSS).

1. **Un solo foco**: `acento` en 1–2 nodos o en la ruta principal (`fill=acento!10!fondo, draw=acento,
   line width=0.9pt`); el resto neutro (`fill=fondo`).
2. **Color solo si significa**: color por familia (`serieX!12!fondo`) cuando distingue tipos de cosa
   (solvers, ingredientes); si no, neutro. Máximo 4 familias.
3. **La forma cuenta la estructura**: cadena, bucle, árbol, matriz. Nada de filas de cajas iguales porque sí.
4. **Rejilla**: `\def\dx{…}` y dos separaciones (0,4 cm entre hermanas, 0,8–1 cm entre grupos); misma
   altura en una fila.
5. **Agrupar con tono** (`tinta!4!fondo` o `!5!`, sin borde, `on background layer`), no con recuadros anidados.
6. **Flechas**: `-{Stealth[length=5pt]}`, `tinta`, 0,8 pt, ortogonales con `rounded corners=4pt`; rutas
   paralelas a ≥ 0,2 cm; nunca cruzando texto ni pasando detrás de una caja.
7. **Etiquetas**: sobre el trazo con `fill=fondo, inner sep=1pt`, ≤ ~14 caracteres; en curvas, al final, sin leyenda.
8. **Texto**: tres niveles (negrita = qué es, normal = qué hace, `tenue` = detalle), `\scriptsize`–`\footnotesize`,
   nada por debajo de `\tiny`.
9. **Densidad y tamaño**: ≤ ~9 nodos y ~12 flechas; en una slide ≤ 13–14,5 cm de ancho y ≤ 5–5,5 cm de
   alto (`diagrama.sh` avisa con «Overfull» si se pasa); si no cabe, sobra contenido o va en dos vistas.
10. **Contraste**: texto ≥ 4,5:1, flechas principales ≥ 3:1; tintes siempre `!N!fondo` y texto de chips
    `textochip`, para que funcione en el tema oscuro; el foco no solo por color (también grosor).

Detalle, números y anti-patrones: `references/criterios.md`.

## Cómo se trabaja

1. **Elige el patrón** por la estructura de lo que cuentas y copia la plantilla de `SKILL/assets/plantillas/`
   (tabla en `references/patrones.md`) a la carpeta del documento (`diagramas/<nombre>.tex`).
2. **Dibuja en rejilla** con los estilos de la plantilla; cambia contenido, no estilos.
3. **Renderiza y mira**:
   ```sh
   SKILL/scripts/diagrama.sh diagramas/x.tex [tema]   # tema de charlas-charlie (bloques, oscuro…) o 'fijo' (blanco)
   ```
   Abre el PNG y revisa la lista de abajo. En una charla, mira también la slide (`charlas-charlie`).
4. Arregla y vuelve a mirar hasta que pase la lista.

## Lista de revisión (sobre el PNG)

1. ¿Se entiende en 3 segundos? ¿Hay un solo foco?
2. ¿Algún texto se sale de su caja o la toca?
3. ¿Alguna flecha cruza texto, pasa detrás de una caja o va inclinada sin motivo?
4. ¿Las cajas de una fila tienen la misma altura y están alineadas?
5. ¿Las etiquetas de flecha se leen (fondo, sin trazo encima)?
6. ¿El color significa algo? ¿Hay más de 4 familias?
7. ¿Se lee en oscuro (si es para slides) y en gris (si es para imprimir)?
8. ¿Sobra algo (una flecha, una caja, una palabra)?

## En una slide o fuera de ella

- **Slides**: el diagrama va en `diagramas/<nombre>.tex` y se incluye con `\input` (nunca pegado en el frame si
  tiene `#`). Los tokens los pone el tema de charlas-charlie; cambian solos al cambiar de tema.
- **Papers y tesis**: `\input{colores-fijos}` (`SKILL/assets/colores-fijos.tex`) define los mismos tokens con
  valores fijos; diseña al ancho de la columna. `references/fuera-de-beamer.md`.

## Trampas que ya costaron tiempo

- `#` dentro de un frame rompe la compilación: fichero aparte con `\input`.
- TikZ anidado hereda `text width`/`minimum height`: resetéalos en el interior.
- Los nombres de nodo son globales: un chip con `(c)` pisa a la caja `(c)`. Nombres raros para los internos.
- Tintes con blanco y texto `white` se rompen en el tema oscuro: `!N!fondo` y `textochip`.

Lista completa: `references/trampas.md`.

## Referencias

| Fichero | Cuándo |
|---|---|
| `references/criterios.md` | diseñar o criticar un diagrama: reglas con números y anti-patrones |
| `references/patrones.md` | elegir y adaptar una plantilla; esqueleto mínimo; chips en línea |
| `references/trampas.md` | algo no compila o se dibuja raro |
| `references/fuera-de-beamer.md` | diagrama para un paper o la tesis |
