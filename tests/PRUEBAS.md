# Batería de pruebas

Subagentes que arrancan de cero con **solo la skill**; se miran los PNG renderizados y se corrige la skill.
Casos en `evals/`; resultados en `../tikz-charlie-workspace/iteration-N/`.

| Caso | Qué se pide |
|---|---|
| `flujo-algoritmo` | Paso de tiempo de un método de proyección con bucle sobre las etapas RK, para una slide en Bloques |
| `esquema-pipe` | Dibujo de un tubo periódico con perfil turbulento, R, L = 15R y f_z |
| `diagrama-tesis` | Pipeline de postproceso para la tesis (fondo blanco, columna de 15 cm) |

## Iteración 1

**Qué salió**: los tres compilan sin desbordes y pasan la lista de revisión; un solo foco en los tres; se
leen en Bloques y en oscuro (el de la tesis, también en gris).

| Problema (prueba) | Corrección |
|---|---|
| El primer render se pasaba ~2 cm del ancho (flujo) | límite de tamaño en SKILL.md; `diagrama.sh` explica el aviso Overfull |
| `diagrama.sh` pisaba el PNG al cambiar de tema (flujo) | el tema va en el nombre del fichero |
| Sin plantilla de esquema físico ni estilo de cotas (pipe) | `esquema_fisico.tex` (sale de la propia prueba) y cotas en `patrones.md` |
| `patterns` no cargada (pipe) | cargada en el preámbulo y en `colores-fijos.tex`; lista de librerías en `trampas.md` |
| Una serie coincide con `acento` según el tema (pipe) | aviso en `criterios.md` |
| En `pipeline.tex` las flechas se inclinaban si una caja crecía (tesis) | flechas a altura fija |
| `diagrama.sh` siempre a 10 pt (tesis) | `TAM=11pt` |
| Cómo pasar a 15 cm; flecha de una etapa a un grupo (tesis) | `patrones.md` |
