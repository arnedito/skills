# audit

Compara el repo con el cerebro que se montó en `init` y con un buen diseño de módulos.

## 1. Cerebro al día

Comprueba, y anota cada desviación:

- Cada módulo del código tiene página en `docs/wiki/` y aparece en `index.md`.
- Las páginas no contradicen el código (muestrea las de módulos con commits recientes).
- `log.md` tiene entrada para los PRs mergeados desde el último audit.
- El `CLAUDE.md` del repo sigue corto y sin reglas que repita el global.
- La CI corre todas las capas elegidas en `init` y ninguna está rota o desconectada.

**Hecho:** cada punto marcado como bien o con su desviación concreta.

## 2. Arquitectura

Invoca `mattpocock-skills:codebase-design` para el vocabulario (módulo, interfaz, profundidad, costura) y busca oportunidades de profundizar en los módulos que más han cambiado (`git log`). Para el informe visual completo con su entrevista, propón al usuario `/mattpocock-skills:improve-codebase-architecture`.

**Hecho:** una lista de candidatos, cada uno con el problema, el cambio propuesto y el coste.

## 3. Cierra

Presenta las desviaciones y los candidatos ordenados por impacto. El usuario elige; cada elegido se convierte en issue. Apunta el audit en `log.md`.
