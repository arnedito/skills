# Temas, paleta, logos y fondos

## Los 6 temas

| Tema | Carácter | Úsalo para |
|---|---|---|
| `bloques` (por defecto) | Un color por bloque, tira de progreso arriba, separadores a sangre con la letra del bloque, portada oscura | Charlas con varias partes: reuniones de tutores, seminarios largos |
| `metropolis` | El clásico sobrio, barra de título azul | Cuando el público espera algo estándar |
| `clasico` | Palatino, azul marino, sin barras, versalitas | Charlas formales, tribunales |
| `tufte` | Blanco, márgenes amplios, un solo acento, títulos en cursiva | Charlas con muchas figuras de datos |
| `oscuro` | Fondo casi negro, acento cian | Contornos CFD y renders, salas oscuras |
| `editorial` | Crema y terracota, títulos grandes | Divulgación, charlas con más texto |

Para elegir con el usuario: `scripts/comparar_temas.sh main.tex 6 [temas…]` (una fila por tema). En
`docs/temas.png` está la charla de muestra en los seis.

## Paleta (tokens)

Cada `tema-<t>.tex` define los mismos nombres; `charla-<t>.mplstyle` repite los HEX para matplotlib.
Usa siempre el nombre, nunca el HEX, y el diagrama cambia solo con el tema.

| Token | Para |
|---|---|
| `fondo` | fondo de la slide; base de todos los tintes (`serieA!12!fondo`) |
| `tinta` | texto y bordes de las cajas de flujo |
| `tenue` | texto secundario, ejes, notas, cabeceras de tabla |
| `regla` | líneas finas, pistas de progreso |
| `acento` | lo que hay que mirar (`\alert`, `\mensaje`, `\frase`) |
| `motivo` | color de los fondos low-poly |
| `textochip` | texto sobre un relleno de serie (chips): blanco; `fondo` en el tema oscuro |
| `serieA`…`serieD` | casos o familias en figuras y diagramas |
| `bloque1`…`bloque6` | (solo Bloques) color de cada bloque; `bloque0` portada, 7–9 neutros |

En Bloques, `\alert` y `\frase` toman el color del bloque actual.

## Logos

- `\def\logos{harmonie,bsc}` (por defecto). `upc` está disponible: `\def\logos{harmonie,bsc,upc}`.
- Portada: 0,75 cm de alto, abajo a la izquierda. Pie: 0,35 cm, a la izquierda del número.
- Cada tema elige la variante (`\logoportada`, `\logopie`: `color` o `blanco`). Bloques usa blanco en la
  portada; Oscuro, blanco en ambos.
- Compensación óptica por logo: `\def\escalalogo@bsc{1.3}` (dentro de `\makeatletter`). El BSC tiene
  cuatro líneas de texto y a la misma altura parece más pequeño.
- Logo nuevo: `python scripts/preparar_logos.py logo-x.png --out estilo/logos` recorta el margen y crea
  `logo-x.png` y `logo-x-blanco.png`. Después, `\def\logos{harmonie,bsc,x}`.
- Sin logos en una slide concreta: `\ocultarlogos` dentro del frame (`\frase` ya lo hace).

## Fondos de portada y separadores

`\def\fondoportada{…}` (vacío por defecto) y `\def\fondoseccion{…}` (por defecto el mismo):

- `pulmones`: low-poly limpio, un solo color (`motivo`), sin halos, pocas partículas. Grande, a la
  derecha, sangrando `\sangrado` (2,6 cm) por el borde.
- `nariz`: lo mismo con la cavidad nasal (silueta del render de *thesis structure*, con los meatos como
  huecos). Como es apaisada, va abajo a la derecha y más estrecha, lejos del título.
- `pulmones-original`: la versión con halos y niebla (más pesada; mejor sobre fondo claro).
- `malla`, `remolinos`, `espectro`, `curvas`: motivos PDF **blancos** (`motivos.py`), solo para portadas
  oscuras; `espectro` y `curvas` se regeneran con datos de AIRE, `malla` y `remolinos` no necesitan datos.
- Una ruta a una imagen del proyecto (`figs/fondo.png`): abajo a la derecha.

La opacidad la fija cada tema (`\opacidadfondo`, 0,22–0,38). `\def\sinfondo{}` quita todos los fondos.
`\def\adornoportada{remolinos}` añade un motivo pequeño arriba a la izquierda de la portada.

### Un fondo low-poly nuevo

```sh
python scripts/lowpoly.py <nombre> --imagen render.png [--huecos 14] [--seed 7] [--flotantes 8] [--llegando 4]
```

La silueta es lo que no es blanco en el render; `--huecos` vacía las sombras más oscuras (percentil) para
que se lea la forma interior (0 = solo contorno). Copia `<nombre>.tex` a `estilo/` y usa
`\def\fondoportada{<nombre>}`. Mira el resultado sobre un tema claro y otro oscuro antes de darlo por bueno.

## Progreso

`\def\progreso{numeros}` (n / N), `barra` (línea fina a todo el ancho al pie, en `\colorprogreso`: el
acento; en Bloques, el color del bloque) o `ambos`. En Bloques además está la tira de bloques arriba.

## Idioma

`\def\idioma{english}` por defecto; `spanish` para castellano. Lo que escribe el tema (p. ej. «Part» /
«Parte» en Clásico) sale de babel. La fecha `\today` también.

## Cambiar de tema en una charla hecha

1. `\def\tema{…}` en `main.tex` (y fondo/progreso si se piden).
2. `python make_figs.py`: las figuras leen el tema de `main.tex` y cambian de color.
3. Compilar, hoja de contactos y mirar cada slide: en `oscuro`, sobre todo chips y rellenos.
4. Si `estilo/VERSION` es anterior a la de `SKILL/assets/estilo/VERSION`, puede faltar algo nuevo (p. ej.
   `textochip` < 1.1.0: las plantillas lo definen solas con `\providecolor`). No migres sin que lo pidan.
5. Fondo en separadores sin secciones: no hay separadores; dilo, no añadas secciones solo por eso.
