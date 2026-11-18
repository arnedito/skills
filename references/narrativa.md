# Narrativa y estructura

Resumen propio para no depender de otras skills. Para un guion desde cero a fondo, carga
`scientific-slides`; si la charla sale de un paper, `presenting-conference-talks`.

## Antes de escribir: `BRIEF.md`

Público, duración, idioma, el mensaje en una frase, los bloques. Si algo de eso no está claro, pregunta;
lo demás (tema, figuras concretas) puede decidirse sobre la marcha.

## Estructura

- **Bloques** con letra y color (A, B, C…). Cada bloque responde una pregunta. En el tema Bloques, cada
  `\section{}` hasta `\nbloques` es un bloque; las secciones posteriores (Cierre, Apéndice) van en neutro.
- Orden típico de una charla de resultados: planteamiento (por qué y qué se compara) → método → un bloque
  por pregunta → cierre → apéndice.
- Cada bloque **cierra con una slide-frase** (`\begin{frame}[c]\frase{…}\end{frame}`): lo que ese bloque
  ha demostrado, en una o dos líneas.
- **Cierre**: tres mensajes como mucho, y el siguiente paso.
- **Apéndice** (`\appendix` + `appendixnumberbeamer` si se quiere numerar aparte): el detalle para las
  preguntas. Lo que «no cabe» va aquí, no en letra pequeña.

Charlas cortas (< ~8 slides): sin secciones ni separadores; como mucho una slide-frase final. Si
piden fondo en los separadores y no hay secciones, deja `\fondoseccion` puesto y dilo: no añadas secciones solo para eso.

## Slides

- **El título es el mensaje**: «La capa límite pesa más que la densidad del núcleo», no «Resultados de mallas».
  En borrador vale un título provisional, pero márcalo para reescribirlo.
- **Una idea por slide.** Si hay dos, son dos slides.
- **~1 minuto por slide**: 20 min ≈ 18–22 slides; 45 min ≈ 35–40 (más apéndice).
- Texto mínimo: la slide no es el guion. Lo que hay que decir va en `\note{}` (qué contar, de dónde salen
  los datos); se ven con `\def\connotas{}`.
- Las listas, 3–4 puntos como mucho, con `\setlength\itemsep{0.9em}` para que respiren.
- Huecos honestos: mientras falte una figura, `\figura{figs/x.pdf}{…}{…}{qué va · de qué datos}`.

## Revelar por partes

`\only<n>` / `\pause` solo cuando el orden importa (recorrer casos en un selector, construir un esquema).
Cada paso es una slide en el PDF: cuenta para el tiempo.
