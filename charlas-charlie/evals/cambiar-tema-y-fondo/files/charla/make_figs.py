"""Figuras de la charla, en PDF vectorial y al tamaño final de la slide, en figs/.

Estilo compartido: estilo/charla.mplstyle (Palatino vía LaTeX, fondo transparente) + estilo/charla-<tema>.mplstyle
(colores del tema). El tema se lee de main.tex: si lo cambias allí, vuelve a ejecutar este script.
Uso:  ~/miniforge3/envs/aire/bin/python make_figs.py [nombre ...]   (sin nombres: todas)
"""
from pathlib import Path
import re
import sys

import matplotlib.pyplot as plt
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


def tono(color, i, n):
    """Variantes de una familia: de claro (i = 0) a pleno (i = n-1). Una familia = un color."""
    c = np.array(plt.matplotlib.colors.to_rgb(color))
    t = 0.35 + 0.65 * i / max(n - 1, 1)
    return tuple(1 - t * (1 - c))


# ---- Synthetic model problem -------------------------------------------------------------------
# -(k(u) u')' = f on (0, 1), u(0) = u(1) = 0, k(u) = k0 + u^2, f = 20, central finite differences
# (N = 199 interior nodes, k at faces from the mean of the two nodes). Both methods start from the
# solution of the linear problem (k = 1) and report ||R(u^k)|| / ||R(u^0)||.
N = 199
H = 1 / (N + 1)
F = np.full(N, 20.0)
K0 = [1.0, 0.3, 0.1]          # from mild to strong nonlinearity (small k0 = strong)
K0_FALLA = 0.05               # Picard without relaxation no longer converges here


def _caras(u):
    ue = np.concatenate([[0.0], u, [0.0]])
    return ue, 0.5 * (ue[1:] + ue[:-1])


def _A(u, k0):
    """Picard matrix: diffusion with the coefficient frozen at u (SPD)."""
    from scipy.sparse import diags
    kf = k0 + _caras(u)[1] ** 2
    return diags([-kf[1:-1], kf[:-1] + kf[1:], -kf[1:-1]], [-1, 0, 1], format="csc") / H ** 2


def _J(u, k0):
    """Newton Jacobian: Picard matrix + the derivative of k (non-symmetric)."""
    from scipy.sparse import diags
    ue, um = _caras(u)
    c = 0.5 * (2 * um) * np.diff(ue) / H / H
    return _A(u, k0) + diags([c[1:-1], -(c[1:] - c[:-1]), -c[1:-1]], [-1, 0, 1], format="csc")


def resolver(k0, metodo, maxit=40, tol=1e-12):
    """Residual history and final solution of Picard or Newton for a given k0."""
    from scipy.sparse import diags
    from scipy.sparse.linalg import spsolve
    lap = diags([-np.ones(N - 1), 2 * np.ones(N), -np.ones(N - 1)], [-1, 0, 1], format="csc") / H ** 2
    u = spsolve(lap, F)
    R = lambda v: _A(v, k0) @ v - F
    r0 = np.linalg.norm(R(u))
    hist = [1.0]
    for _ in range(maxit):
        u = spsolve(_A(u, k0), F) if metodo == "picard" else u - spsolve(_J(u, k0), R(u))
        hist.append(np.linalg.norm(R(u)) / r0)
        if hist[-1] < tol:
            break
    return np.array(hist), u


def iteraciones(hist, tol=1e-8):
    i = np.flatnonzero(hist < tol)
    return int(i[0]) if i.size else None


def convergencia():
    """Residual vs iteration: Picard (serieA tones) and Newton (serieD tones), one tone per k0."""
    fig, ax = plt.subplots(figsize=(ANCHO, 5.6 * CM), constrained_layout=True)
    n = len(K0)
    ax.axhline(1e-8, color=TENUE, lw=0.6, ls=(0, (4, 3)))
    ax.text(22, 1.6e-8, r"tolerance $10^{-8}$", color=TENUE, fontsize=8, va="bottom", ha="left")
    hp, _ = resolver(K0_FALLA, "picard")
    ax.semilogy(hp, color=TENUE, lw=0.7, ls=(0, (2, 1.5)))
    ax.text(40.5, 0.15, rf"Picard, $k_0 = {K0_FALLA:g}$: oscillates, never converges", color=TENUE,
            fontsize=8, ha="right", va="top")
    for t, k0 in enumerate(K0):                         # stronger nonlinearity (small k0) = fuller tone
        hp, _ = resolver(k0, "picard")
        hn, _ = resolver(k0, "newton")
        ax.semilogy(hp, color=tono(SERIES[0], t, n), marker="o", ms=2.2)
        ax.semilogy(hn, color=tono(SERIES[3], t, n), marker="s", ms=2.4)
        j = len(hp) - 1
        abajo = j == 40                                  # the curve that leaves by the right edge
        ax.annotate(rf"$k_0 = {k0:g}$", (j, max(hp[j], 1e-12)), xytext=(0, -5) if abajo else (4, 3),
                    textcoords="offset points", color=tono(SERIES[0], t, n), fontsize=8,
                    ha="right" if abajo else "left", va="top" if abajo else "bottom")
    ax.text(7.3, 1e-10, r"\textbf{Newton}", color=SERIES[3], fontsize=9, ha="left")
    ax.text(25, 1e-3, r"\textbf{Picard}", color=SERIES[0], fontsize=9, ha="left")
    ax.set(xlabel=r"nonlinear iteration $k$", ylabel=r"$\|R(u^k)\| \,/\, \|R(u^0)\|$",
           xlim=(0, 41), ylim=(1e-12, 3e3))
    ax.set_yticks([1e-12, 1e-8, 1e-4, 1e0])
    fig.savefig(FIGS / "convergencia.pdf")
    plt.close(fig)


def perfiles():
    """Converged solutions u(x) for each k0: the problem the solvers are chasing."""
    fig, ax = plt.subplots(figsize=(ANCHO / 2 - 0.3 * CM, 4.6 * CM), constrained_layout=True)
    x = np.linspace(0, 1, N + 2)
    n = len(K0)
    for t, k0 in enumerate(K0):
        _, u = resolver(k0, "newton")
        ue = np.concatenate([[0.0], u, [0.0]])
        ax.plot(x, ue, color=tono(SERIES[0], t, n))
        arriba = t == n - 1
        ax.text(0.5, ue.max() + (0.05 if arriba else -0.1), rf"$k_0 = {k0:g}$", color=tono(SERIES[0], t, n),
                fontsize=8, ha="center", va="bottom" if arriba else "top")
    ax.set(xlabel=r"$x$", ylabel=r"$u(x)$", ylim=(0, 2.3), xlim=(0, 1))
    fig.savefig(FIGS / "perfiles.pdf")
    plt.close(fig)


def tabla():
    """Iterations to 10^-8 for the table on the cost slide (printed, copied into main.tex)."""
    for k0 in K0 + [K0_FALLA]:
        print(f"k0 = {k0:<5g}  Picard {iteraciones(resolver(k0, 'picard', 200)[0])}"
              f"  Newton {iteraciones(resolver(k0, 'newton')[0])}")


FIGURAS = {"convergencia": convergencia, "perfiles": perfiles}

if __name__ == "__main__":
    FIGS.mkdir(exist_ok=True)
    if sys.argv[1:] == ["tabla"]:
        tabla()
        sys.exit()
    for nombre in sys.argv[1:] or FIGURAS:
        FIGURAS[nombre]()
        print(f"figs/{nombre}.pdf  (tema {TEMA})")
