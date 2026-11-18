"""Figuras de la charla, en PDF vectorial y al tamaño final de la slide, en figs/.

Estilo compartido: estilo/charla.mplstyle (Palatino vía LaTeX, fondo transparente) + estilo/charla-<tema>.mplstyle
(colores del tema). El tema se lee de main.tex: si lo cambias allí, vuelve a ejecutar este script.
Uso:  ~/miniforge3/envs/aire/bin/python make_figs.py [nombre ...]   (sin nombres: todas)
"""
from pathlib import Path
import re
import sys

try:
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("Falta matplotlib: usa un python que lo tenga (en el Mac de Carlos: ~/miniforge3/envs/aire/bin/python)")
import numpy as np

AQUI = Path(__file__).parent
ESTILO = AQUI / "estilo"
FIGS = AQUI / "figs"
CM = 1 / 2.54
TEMA = re.search(r"\\def\\tema\{(\w+)\}", (AQUI / "main.tex").read_text()).group(1)
# ancho útil de la slide (16 cm menos los márgenes del tema): la figura se exporta a este tamaño y
# se incluye sin escalar, así el texto de la figura mide lo mismo que el de la slide
ANCHO = {"bloques": 13.8, "metropolis": 14.6, "clasico": 14.0, "tufte": 13.0,
         "oscuro": 14.0, "editorial": 13.6}[TEMA] * CM

plt.style.use([ESTILO / "charla.mplstyle", ESTILO / f"charla-{TEMA}.mplstyle"])
SERIES = plt.rcParams["axes.prop_cycle"].by_key()["color"]     # serieA..serieD del tema
TINTA, TENUE = plt.rcParams["text.color"], plt.rcParams["axes.edgecolor"]
FONDO = {"bloques": "#FAFAF7", "metropolis": "#FFFFFF", "clasico": "#FFFFFF", "tufte": "#FFFFFF",
         "oscuro": "#111418", "editorial": "#F5EFE4"}[TEMA]          # fondo de la slide (tema-<t>.tex)


def tono(color, i, n):
    """Variantes de una familia: de suave (i = 0) a pleno (i = n-1). Una familia = un color.
    Mezcla con el FONDO del tema (no con blanco): así el tono suave también se ve en `oscuro`."""
    c = np.array(plt.matplotlib.colors.to_rgb(color))
    f = np.array(plt.matplotlib.colors.to_rgb(FONDO))
    t = 0.5 + 0.5 * i / max(n - 1, 1)
    return tuple(f + t * (c - f))


def ejemplo():
    """Plantilla: sustituir por las figuras de la charla. Tamaño: ancho útil × 5.5 cm."""
    fig, ax = plt.subplots(figsize=(ANCHO, 5.5 * CM), constrained_layout=True)
    x = np.linspace(0, 1, 100)
    for i in range(3):
        ax.plot(x, x ** (i + 1), color=tono(SERIES[0], i, 3), label=f"$n = {i + 1}$")
    ax.set(xlabel=r"$x$", ylabel=r"$x^n$")
    ax.legend(loc="upper left")
    fig.savefig(FIGS / "ejemplo.pdf")
    plt.close(fig)


FIGURAS = {"ejemplo": ejemplo}

if __name__ == "__main__":
    FIGS.mkdir(exist_ok=True)
    for nombre in sys.argv[1:] or FIGURAS:
        FIGURAS[nombre]()
        print(f"figs/{nombre}.pdf  (tema {TEMA})")
