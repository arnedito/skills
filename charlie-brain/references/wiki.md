# Wiki del proyecto

Estilo LLM wiki de Karpathy: el agente mantiene un conjunto de páginas markdown que destilan lo que no está en el código. Vive en `docs/wiki/`, versionada, y se actualiza en el mismo PR que el código que describe.

## Estructura

- `index.md`: el mapa. Una línea por página: qué cuenta y cuándo leerla. Es lo único que se lee para orientarse.
- Una página por módulo o concepto: qué hace, por qué es así, papers o fuentes, ADRs que le afectan, dónde están sus tests, trampas conocidas.
- `log.md`: una entrada por PR o decisión, la más reciente arriba: fecha, qué cambió, enlace al PR.

## Fuentes y wiki, separadas

Las fuentes (papers, especificaciones, datos de referencia) viven aparte, por ejemplo en `docs/papers/`, y no se editan: la wiki las resume y enlaza. Así una página siempre puede rastrearse hasta su fuente, y si la fuente cambia se sabe qué páginas revisar.

## Qué entra y qué no

Señal de que algo debe entrar: el agente o el usuario lo ha explicado dos veces.


Entra lo que el agente no puede averiguar mirando: convenciones no escritas, el porqué de una decisión, trampas que ningún fichero de configuración confiesa. No entra lo que el entorno ya dice (lista de ficheros, flags de build, firmas de funciones): se queda viejo y duplica.

## Coste en tokens

Bajo: para orientarse se lee `index.md`, y luego solo la página que toca. Un grafo de conocimiento completo (`/graphify`) es caro: se lanza a demanda y su salida va en `.gitignore`.

## Regla para el CLAUDE.md del repo

Añade una línea así (ajusta las rutas):

```markdown
Antes de tocar un módulo, lee su página en `docs/wiki/` (mapa: `docs/wiki/index.md`). Si tu PR cambia lo que cuenta, actualízala y añade una entrada a `docs/wiki/log.md`.
```
