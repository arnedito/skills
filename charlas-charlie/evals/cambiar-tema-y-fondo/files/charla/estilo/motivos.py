"""Motivos gráficos de fondo para portadas (PDF vectorial, transparente, un solo color).

  malla      sección del pipe: capas prismáticas en la pared y tetraedros (Delaunay) en el núcleo
  espectro   espectro de energía en los 5 testigos (IMP ASGS, M2B) con la pendiente -5/3
  curvas     perfiles de la DNS (El Khoury 2013): ley de pared y fluctuaciones, sin ejes
  remolinos  cascada de Richardson: espirales que se parten en otras más pequeñas

Uso: python motivos.py [--color FFFFFF]   (entorno conda 'aire'). Escribe motivos/motivo-<nombre>.pdf
"""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

AQUI = Path(__file__).parent
AIRE = Path.home() / "postprocess/aire/data"
RNG = np.random.default_rng(7)


def lienzo(ancho=6, alto=6):
    fig = plt.figure(figsize=(ancho, alto))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    return fig, ax


def malla(ax, c):
    R, capas, r1, crec = 1.0, 7, 0.006, 1.22
    alturas = r1 * crec ** np.arange(capas)
    radios = R - np.concatenate([[0], np.cumsum(alturas)])
    nth = 96
    th = np.linspace(0, 2 * np.pi, nth + 1)
    for r in radios:
        ax.plot(r * np.cos(th), r * np.sin(th), color=c, lw=0.35)
    for t in th[:-1]:
        ax.plot([radios[-1] * np.cos(t), R * np.cos(t)], [radios[-1] * np.sin(t), R * np.sin(t)],
                color=c, lw=0.35)
    # núcleo: puntos en el anillo interior + relleno con densidad algo mayor hacia la pared
    rin = radios[-1]
    borde = np.c_[rin * np.cos(th[:-1]), rin * np.sin(th[:-1])]
    pts = [borde]
    for r in np.linspace(rin * 0.95, 0.05, 15):
        n = max(int(nth * r / rin * 0.85), 6)
        a = np.linspace(0, 2 * np.pi, n, endpoint=False) + RNG.uniform(0, 2 * np.pi)
        jit = RNG.normal(0, 0.012, (n, 2))
        pts.append(np.c_[r * np.cos(a), r * np.sin(a)] + jit)
    pts.append([[0, 0]])
    p = np.vstack(pts)
    tri = Delaunay(p)
    ax.triplot(p[:, 0], p[:, 1], tri.simplices, color=c, lw=0.3)
    ax.set_aspect("equal")
    ax.set(xlim=(-1.02, 1.02), ylim=(-1.02, 1.02))


def espectro(ax, c):
    d = np.load(AIRE / "outputs/methods_m2b/ASGS/witness/spectra.npz")
    f = d["frequency"]
    for e in d["E_k"]:
        m = f > 0
        ax.loglog(f[m], e[m], color=c, lw=1.1)
    f0 = np.logspace(1.6, 2.9, 10)
    ax.loglog(f0, 2e-1 * (f0 / 40) ** (-5 / 3), color=c, lw=2.0, ls=(0, (4, 3)))


def curvas(ax, c):
    def leer(n):
        with open(AIRE / "dns" / n) as fh:
            filas = list(csv.DictReader(fh))
        return {k: np.array([float(r[k]) for r in filas]) for k in filas[0]}
    u, rms = leer("elkhoury_dns_retau180.csv"), leer("dns_pipe_re180.csv")
    ax.semilogx(u["y_plus"], u["u_plus"] / 19, color=c, lw=2.6)
    for k, w in [("uz_rms_plus", 1.8), ("ut_rms_plus", 1.4), ("ur_rms_plus", 1.4), ("uzur_plus", 1.1)]:
        ax.semilogx(rms["y_plus"], rms[k] / 2.8, color=c, lw=w)
    yp = np.logspace(-0.3, 0.9, 20)
    ax.semilogx(yp, yp / 19, color=c, lw=0.6, ls=":")
    ax.set(xlim=(0.6, 200), ylim=(-0.02, 1.05))


def remolinos(ax, c):
    def espiral(x0, y0, r, giro, nivel):
        t = np.linspace(0, 4.2 * np.pi, 260)
        rr = r * np.exp(-0.16 * t)
        ax.plot(x0 + rr * np.cos(giro * t), y0 + rr * np.sin(giro * t), color=c,
                lw=0.6 + 0.8 * nivel)
        if nivel > 0:
            for k in range(3):
                a = RNG.uniform(0, 2 * np.pi) + k * 2.1
                d = r * RNG.uniform(1.05, 1.35)
                espiral(x0 + d * np.cos(a), y0 + d * np.sin(a), r * 0.42, -giro, nivel - 1)
    espiral(0, 0, 1.0, 1, 3)
    ax.set_aspect("equal")
    ax.set(xlim=(-2.6, 2.6), ylim=(-2.6, 2.6))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--color", default="FFFFFF")
    c = "#" + ap.parse_args().color
    (AQUI / "motivos").mkdir(exist_ok=True)
    for nombre, fn, tam in [("malla", malla, (6, 6)), ("espectro", espectro, (7, 5)),
                            ("curvas", curvas, (7, 5)), ("remolinos", remolinos, (6, 6))]:
        fig, ax = lienzo(*tam)
        fn(ax, c)
        fig.savefig(AQUI / f"motivos/motivo-{nombre}.pdf", transparent=True)
        plt.close(fig)
