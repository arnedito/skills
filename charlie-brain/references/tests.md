# Capas de tests

TDD por defecto: test que falla (_rojo_) → código mínimo → _verde_ → limpiar. Para el ciclo concreto, invoca `mattpocock-skills:tdd`.

Elige en `init` las capas que aplican; no todas encajan en todos los repos.

| Capa | Qué comprueba | Dónde corre |
|---|---|---|
| Unitarios | Cada función o módulo en aislamiento | CI, pre-commit (subconjunto rápido) |
| Matemáticas / paper | Cada ecuación o lema implementado, con valores calculados a mano o sacados del paper; el test cita la ecuación (`// Eq. 7, Autor 1997`) | CI |
| Propiedades | Entradas aleatorias con semilla fija; invariantes que siempre deben cumplirse | CI |
| Invariantes de salida | Toda salida del programa cumple sus reglas de validez (p. ej. malla conforme, volúmenes positivos) | CI, en cada generador |
| Bindings / API | La interfaz pública desde el lenguaje del usuario (p. ej. pytest sobre bindings C++) | CI |
| Interfaz | Backend de la GUI con tests normales; 1–2 tests de humo end-to-end (Playwright) | CI, solo Linux |
| Humo con caso real | Un caso real reducido (datos ligeros versionados) de principio a fin, en menos de ~2 min | CI |
| Regresión / rendimiento | Métricas y tiempos contra una referencia guardada; casos grandes y oráculos externos | Local o HPC, a mano |

## CI

- Matriz de los sistemas donde debe compilar.
- Debug con sanitizers (ASan/UBSan) si hay C/C++; Release aparte.
- `actionlint` sobre los workflows.
- Cobertura visible en el PR, sin umbral que bloquee.
- Un test que falla y no se arregla en el PR se marca como fallo conocido y abre su issue.

## Pre-commit

Solo lo rápido y mecánico: formato, lint, tests unitarios rápidos, y la regla de commits que se eligió en `init`. Lo lento va a la CI.
