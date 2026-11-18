"""Prepara logos para las charlas: recorta el margen transparente/blanco y crea la versión blanca.

Uso:  python preparar_logos.py logo-x.png [...] --out estilo/logos
Escribe <out>/logo-<n>.png (color, recortado) y <out>/logo-<n>-blanco.png (silueta blanca, para fondos oscuros).
Necesita Pillow y numpy.
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def alfa(im):
    """Alfa real: la del PNG y, si el fondo es blanco opaco, la distancia al blanco."""
    a = np.asarray(im.convert("RGBA")).astype(float)
    rgb, al = a[..., :3], a[..., 3]
    tinta = 255 - rgb.min(axis=2)            # 0 en blanco puro
    return np.minimum(al, np.clip(tinta * 4, 0, 255)) if al.min() == 255 else al


def guardar(im, ruta, ancho_max=1600):
    """Basta con ~1600 px: en la portada el logo mide unos 4 cm."""
    if im.width > ancho_max:
        im = im.resize((ancho_max, round(im.height * ancho_max / im.width)), Image.LANCZOS)
    im.save(ruta, optimize=True)


def preparar(ruta, out):
    im = Image.open(ruta).convert("RGBA")
    a = alfa(im)
    ys, xs = np.nonzero(a > 8)
    caja = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    nombre = Path(ruta).stem.removeprefix("logo-")
    color = np.asarray(im).copy()
    color[..., 3] = a.astype(np.uint8)
    guardar(Image.fromarray(color).crop(caja), out / f"logo-{nombre}.png")
    blanco = np.zeros_like(color)
    blanco[..., :3] = 255
    blanco[..., 3] = a.astype(np.uint8)
    guardar(Image.fromarray(blanco).crop(caja), out / f"logo-{nombre}-blanco.png")
    print(nombre, "->", caja[2] - caja[0], "x", caja[3] - caja[1])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("logos", nargs="+")
    ap.add_argument("--out", default="logos")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for r in args.logos:
        preparar(r, out)
