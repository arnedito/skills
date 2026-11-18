# init

Monta el cerebro en un repo. Cada paso termina en su criterio de hecho; no pases al siguiente sin cumplirlo.

## 1. Explora

Lee el repo sin tocar nada: lenguaje y build, tests existentes y cómo se lanzan, CI (`.github/workflows/`), `CLAUDE.md`/`AGENTS.md` del repo y el global (`~/.claude/CLAUDE.md`), `docs/`, ADRs, remoto git, si `gh` está autenticado, ficheros grandes o datos sueltos en la raíz.

**Hecho:** un resumen de 5–10 líneas de lo que hay y lo que falta.

## 2. Interroga

Rondas de `grilling` sobre estas ramas. Salta las que la exploración ya resolvió; cada una con tu recomendación:

1. **Qué es el proyecto** y quién lo usa (código propio, paper, herramienta, app).
2. **`CLAUDE.md`**: parte de [`claude-md-base.md`](claude-md-base.md). Recorre sus cuatro principios uno a uno: ¿se queda, se ajusta o sobra en este proyecto? Si el global ya los lleva, el del repo no los repite. Luego, qué reglas propias añade el dominio (stack, idioma de código y docs, de dónde salen los algoritmos, datos sensibles).
3. **Comunicación**: conciso por defecto; `/para-el-carro` para pedir más detalle. Confirma o ajusta.
4. **Commits**: con o sin línea `Co-Authored-By`; idioma de commits, issues y PRs.
5. **Tests**: capas que aplican, según [`tests.md`](tests.md). TDD por defecto en todo código nuevo.
6. **Flujo**: issue tracker (GitHub por defecto), quién hace merge (el humano), protección de `main`, tamaño de PR.
7. **Wiki**: estructura de [`wiki.md`](wiki.md); ¿se publica como sitio (MkDocs en GitHub Pages) o solo en el repo?
8. **Datos y limpieza**: qué ficheros sueltos se mueven, cuáles van a `.gitignore`, cuáles necesitan versión ligera para la CI.

**Hecho:** ninguna rama abierta y el usuario confirma que hay entendimiento compartido.

## 3. Escribe

En una rama `brain/init`, en este orden, un commit por bloque:

1. `CLAUDE.md` del repo: menos de ~80 líneas, reglas propias y punteros (`docs/wiki/index.md`, `CONTRIBUTING.md`, `docs/adr/`). Nada que el global ya diga.
2. `docs/wiki/index.md` y `docs/wiki/log.md` desde [`../templates/`](../templates/), con una página por módulo o concepto que la exploración haya encontrado.
3. `docs/adr/0001-flujo-de-trabajo.md` con las decisiones de la entrevista ([`../templates/adr.md`](../templates/adr.md)).
4. `CONTRIBUTING.md` y `.github/` desde `../templates/CONTRIBUTING.md` y `../templates/github/`, traducidos al idioma elegido para issues y PRs, adaptados y pasados por `humanizer`.
5. Tests que corran de verdad: lanza el comando de tests en limpio; si falla por entorno (dependencias sin declarar, ruta del paquete, versión del intérprete), arréglalo y escribe el comando que funciona en `CONTRIBUTING.md`. Cada ecuación o fórmula ya implementada sin un test que la cite recibe ese test ahora (tests sí, código de producción no). Si ya hay tests que fallan, márcalos como fallo conocido con su issue; no los borres.
6. CI y pre-commit según [`tests.md`](tests.md), con el mismo comando que acabas de comprobar.
7. Etiquetas (`area:*`, `tipo:*`) y milestones con `gh`, si está autenticado.

**Hecho:** la CI pasa en la rama, el PR está abierto y el usuario lo revisa. No hagas merge.

## 4. Deja el siguiente paso

Propón, con el comando exacto, `/mattpocock-skills:setup-matt-pocock-skills` si el usuario quiere usar las skills de ingeniería de Pocock en este repo, y apunta en `log.md` cuándo toca el primer `audit` y la primera `retro` (al cerrar el primer milestone).
