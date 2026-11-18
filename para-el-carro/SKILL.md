---
name: para-el-carro
description: "Para. Lo último no se entendió: explícalo despacio, con contexto y a lo Feynman."
disable-model-invocation: true
---

El usuario no ha seguido tu último mensaje. Vuelve a explicarlo con la técnica de Feynman: si no puedes contarlo con palabras sencillas, es que aún no está claro, y el hueco suele estar justo donde te salía la jerga.

1. **Dónde estamos**: una o dos frases de contexto (qué se estaba haciendo y por qué).
2. **La idea en llano**: cuéntalo como a alguien listo que no es del campo. Sin jerga; si un término hace falta, defínelo en una frase la primera vez.
3. **Una analogía** con algo cotidiano, y dónde deja de valer.
4. **Un ejemplo concreto**, a ser posible del propio proyecto, con números o código si ayudan.
5. **El hueco**: si al simplificar notas una parte que no sabes explicar bien o que antes diste por sentada, dilo y aclárala.
6. **Qué cambia para el usuario**: qué tiene que decidir o hacer, si algo, atado a lo que está intentando conseguir.
7. **Una fuente**: si el concepto viene de un paper o una doc, enlaza la mejor fuente primaria (sección o ecuación), no tu memoria.
8. **Una pregunta de comprobación**: cierra con una pregunta corta que el usuario pueda responder de cabeza, para ver si ha quedado (recordar fija más que releer).

Si el tema da para varias sesiones (el usuario quiere aprenderlo, no solo desatascarse), propón `/mattpocock-skills:teach`.

## Modo visual

Con `visual` tras el comando, o si el usuario sigue sin entenderlo después de la explicación en texto, haz además una página HTML interactiva: controles para mover los parámetros y ver el efecto, y animación solo si el concepto tiene movimiento (un frente que avanza, un algoritmo paso a paso). Encaja con lo espacial, lo dinámico o lo que depende de parámetros; para una idea abstracta, quédate en texto y dilo. Diseño limpio, estilo Tufte: poca tinta, mucho dato. Publícala como artifact privado (o widget inline si no hay artifacts) y apóyate en `artifact-diagramming` si hay diagrama.

Si el usuario añadió otra palabra o frase tras el comando, céntrate en eso. Vuelve al estilo conciso en el siguiente mensaje.
