# Cambios del estilo

Cada charla anota en `estilo/VERSION` la versión que copió.

## 1.2.0 · 2026-11-18 (tras el grilling)

- Logos oficiales (HARMONIE original/azul/negro/blanco, BSC azul/blanco) más `harmonie-favicon`; variantes
  `auto|color|azul|negro|blanco|tenue` en portada y pie; tamaños `\tamlogos`.
- `\sangrado{poco|mucho|medida}`, por defecto `poco` (1,2 cm).
- Fondos nuevos: `pulmones-<paleta>`, `nariz-llena`, `nariz-silueta`, `vias`, `acino`.
- Portada: reserva para los logos a su medida.
- `\letra{palatino|charter|sans|lmodern}`. `\mensaje` empieza párrafo.

## 1.1.0 · 2026-11-17 (tras la batería de pruebas)

- Bloques: separadores y viñetas de Cierre/Apéndice en neutro (`bloqueactual`); títulos de dos líneas con sangría.
- Portada: hueco para los logos (`\reservalogos`): el bloque de autor ya no los pisa.
- `\caso` en `\mdseries` (Palatino no tiene versalitas negritas).
- Token `textochip` (texto de chips): legible en `oscuro`.
- `make_figs.py`: `tono()` mezcla con el fondo del tema.
- Plantillas: nombres de nodo internos sin choques (`etq@`, `chip@`); `chips.tex` con columna Esquema.
- `compilar.sh` avisa de fuentes que faltan; `nueva_charla.sh` respeta el idioma y toma el nombre del título.

## 1.0.0 · 2026-11-17

Primera versión de la skill, a partir del estilo de `charla01-pipe`:

- 6 temas con selector; **Bloques por defecto**; **inglés por defecto** (`\def\idioma{spanish}` para castellano).
- Logos HARMONIE y BSC (UPC disponible): grandes en la portada, pequeños en el pie de las slides de
  contenido, ocultos en separadores y slides-frase; variantes en blanco para fondos oscuros.
- Fondos: sin fondo por defecto; `pulmones` nuevo (limpio, un color, se tiñe con el tema), `nariz`
  (nuevo), `pulmones-original`, motivos PDF o imagen propia. `\sangrado` regulable.
- Progreso: `\def\progreso{numeros|barra|ambos}`.
- Los temas propios dibujan el subtítulo del frame (antes desaparecía).
- Clásico: «Part/Parte» según el idioma. Bloques: la franja de la portada usa `\nbloques`.
- Estilos matplotlib renombrados: `pipe*.mplstyle` → `charla*.mplstyle`.
- Plantillas de diagrama genéricas con tintes mezclados con `fondo` (se leen en el tema oscuro).
