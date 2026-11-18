# retro

Mejora el **entorno** del agente (no el código) a partir de cómo fueron las sesiones. Basada en `/mattpocock-skills:retro`, con cuatro cambios: mira varias sesiones, pregunta primero al usuario, deja issues y poda.

## 1. Pregunta primero

Una ronda corta de `grilling`: qué le frustró al usuario desde la última retro, qué tuvo que repetir, en qué se equivocó el agente. Lo que el usuario sintió pesa más que lo que el agente cree.

## 2. Lee las sesiones

Las sesiones desde la última retro (ver `log.md`), no solo la actual. Delega la lectura de transcripts en un subagente que devuelva solo hallazgos, para no llenar el contexto.

Busca patrones que se repiten, en estas categorías:

- **Navegación**: el agente tardó en encontrar algo → puntero en `CLAUDE.md` o página de wiki.
- **Checks**: un error que un check mecánico habría pillado → hook, pre-commit o CI.
- **Reglas**: un error de juicio repetido → regla en `CLAUDE.md` o en la plantilla de PR.
- **Coste**: llamadas a herramientas caras que se repiten → script o comando del proyecto.
- **Información**: le faltó un dato (logs, datos de prueba, acceso) → hacerlo accesible.
- **Fidelidad**: el código se apartó de su fuente (paper, especificación) sin anotarlo → test que cite la fuente.

Un hallazgo que aparece una sola vez se anota en `log.md`, pero no genera regla.

## 3. Poda

Repasa `CLAUDE.md` y la wiki línea a línea: quita lo que ya no cambia el comportamiento del agente (no-ops), lo que repite otra fuente, y lo que se ha quedado viejo. Quitar es tan importante como añadir.

## 4. Cierra

Presenta hallazgos y podas por gravedad. El usuario elige; cada cambio va como issue o directamente en un PR `brain/retro-<fecha>`. Apunta la retro en `log.md`.

**Hecho:** cada hallazgo elegido tiene issue o está en el PR, y `log.md` tiene la entrada.
