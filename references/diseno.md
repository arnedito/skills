# Criterios de diseño para slides

Los de `impeccable` y del gusto «anti-plantilla», adaptados a slides de Beamer. **Las preferencias de
Carlos pesan más que estas reglas**: borde negro en las cajas de flujo, fondos low-poly en portada y
separadores, nombres de solvers sin traducir. Si una regla choca con algo que él ha pedido, gana lo pedido.

## Jerarquía

- 2–3 tamaños por slide: título, cuerpo y, si hace falta, nota (`\footnotesize` en `tenue`). Más niveles
  se leen como ruido.
- Un solo foco: lo que hay que mirar va en `acento` (o en el color del bloque) y nada más compite con él.
- El título es una frase con el mensaje. Si el título no dice nada, la slide tampoco.
- **El título cabe en una línea**: ~50 caracteres a 11 pt (Bloques, Clásico); dos líneas como mucho.
- **Presupuesto vertical**: en 9 cm de alto, quitando título y pie, quedan ~6 cm para el cuerpo (unas
  8–9 líneas a 11 pt, o una figura de 5–5,5 cm y una línea). Si no cabe, sobra contenido.
- Portada: título ≤ 2 líneas y subtítulo ≤ 2 (el bloque de autor no puede bajar hasta los logos).
- Los frames van centrados en vertical (por defecto de Beamer); con contenido denso, `[t]`.

## Tono antes que líneas

- Agrupa con un fondo suave (`tinta!4!fondo`) o con espacio, no con recuadros dentro de recuadros.
- Texto secundario en `tenue`, no más pequeño y además gris y además en cursiva: con una marca basta.
- Tablas: `booktabs` (sin verticales), cabecera en `tenue`, la columna que importa en negrita o en color.

## Poca tinta que no sea dato

- Figuras sin rejilla, sin marco arriba/derecha, leyenda sin caja o etiquetas directas.
- Nada de iconos decorativos, sombras ni degradados. Los fondos low-poly son la única decoración, y solo
  en portada y separadores (con opacidad baja).

## Composición

- Nada de filas de tarjetas iguales porque sí: si tres cosas no son paralelas, no las dibujes como tres
  cajas iguales. La forma del esquema tiene que contar la estructura (cadena, bucle, árbol, matriz).
- Alinear a una rejilla: márgenes del tema, columnas con `columns`, diagramas con `\dx` fijo.
- Aire: si la slide está llena, sobra contenido. Divídela o manda el detalle al apéndice.
- Slides-frase (`\frase`) para cerrar bloques: grandes, centradas, solas.

## Color

- Un color = una familia en toda la charla (diagramas, figuras y texto).
- Tintes siempre con `fondo`; contraste de texto suficiente también en `oscuro` (texto claro sobre
  relleno oscuro).
- Máximo 4 series en una figura; más, con tonos de una misma familia o en paneles separados.

## Lista para revisar una slide renderizada

1. ¿El título dice el mensaje?
2. ¿Hay un solo foco? ¿Se ve en 3 segundos?
3. ¿Algún texto se sale, se corta o toca el pie, los logos o la tira de progreso?
4. ¿El texto de las figuras mide como el de la slide (figura sin escalar)?
5. ¿Se lee en el tema elegido (contraste, sobre todo `oscuro`)?
6. ¿Sobra algo (líneas, cajas, palabras)?
7. ¿Cuadra con las slides vecinas en la hoja de contactos (márgenes, tamaños, colores)?
