# Logos

Los logos (HARMONIE, BSC, UPC) son de sus titulares y **no están en el repositorio**. Ponlos aquí con el
nombre `logo-<nombre>-<variante>.png` (variantes `color`, `azul`, `negro`, `blanco`), p. ej.
`logo-bsc-color.png`. `scripts/preparar_logos.py` recorta el margen y genera la versión blanca:

    python scripts/preparar_logos.py mi-logo.png --out assets/estilo/logos

Sin ficheros, la charla compila igual (sin logos y con un aviso). Para quitarlos: `\def\logos{}`.
