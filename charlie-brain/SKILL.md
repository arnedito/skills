---
name: charlie-brain
description: "Monta y hace evolucionar el cerebro de un repo (CLAUDE.md, wiki, ADRs, tests, CI, flujo issue→PR). Modos: init, audit, retro."
disable-model-invocation: true
---

# charlie-brain

El **cerebro** de un repo es todo lo que un agente necesita para trabajar en él sin redescubrirlo cada sesión: un `CLAUDE.md` corto con punteros, una wiki con lo que el código no cuenta, ADRs con el porqué de cada decisión, tests que hacen de red, y un flujo issue → rama → PR → CI verde → merge humano.

Crece **orgánicamente**: cada PR deja el cerebro un poco más completo (página de wiki, entrada de log, ADR, tests), y cada `retro` poda lo que sobra.

`SKILL` = la carpeta de este fichero.

## Modos

Lee el argumento (`init`, `audit`, `retro`). Sin argumento: si el repo no tiene `docs/wiki/index.md`, es `init`; si lo tiene, pregunta cuál.

| Modo | Cuándo | Pasos |
|---|---|---|
| `init` | Repo nuevo o sin cerebro | [`references/init.md`](references/init.md) |
| `audit` | Al cerrar un milestone, o cuando el código se siente enredado | [`references/audit.md`](references/audit.md) |
| `retro` | Al cerrar un milestone o tras una racha de sesiones torpes | [`references/retro.md`](references/retro.md) |

## Reglas de todos los modos

- **Interroga antes de escribir.** Toda decisión del usuario pasa por una ronda de `grilling` (Skill tool, `mattpocock-skills:grilling`): preguntas numeradas, cada una con su respuesta recomendada, redactada para que "sí" la acepte. Los hechos del repo los averiguas tú; las decisiones son suyas.
- **Una sola fuente de verdad.** Cada regla vive en un sitio. Lo que el entorno ya dice (`CMakeLists.txt`, `pyproject.toml`, la estructura de carpetas) no se copia a la wiki.
- **Checks antes que texto.** Una regla mecánica (formato, mensaje de commit, tests antes del commit) va a un hook, pre-commit o CI. El `CLAUDE.md` guarda solo juicio y punteros.
- **Prosa humana.** Plantillas, issues, PRs y README pasan por `humanizer` antes de escribirse.
- **Skills de apoyo.** Invoca las que el agente puede lanzar: `mattpocock-skills:grilling`, `mattpocock-skills:codebase-design`, `mattpocock-skills:tdd`, `mattpocock-skills:domain-modeling`, `mattpocock-skills:writing-for-agents`, `humanizer`. Las que solo lanza el usuario (`/mattpocock-skills:improve-codebase-architecture`, `/mattpocock-skills:retro`, `/mattpocock-skills:setup-matt-pocock-skills`) se las propones con su comando exacto. Si una no está instalada, sigue sin ella y dilo en una línea.
