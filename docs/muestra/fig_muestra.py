"""Figura de la charla de muestra, una por tema (figs/fig-<tema>.pdf). Datos sintéticos."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

AQUI = Path(__file__).parent
ESTILO = AQUI.parent.parent / "assets/estilo"
CM = 1 / 2.54
for tema in ["bloques", "metropolis", "clasico", "tufte", "oscuro", "editorial"]:
    plt.style.use("default")
    plt.style.use([ESTILO / "charla.mplstyle", ESTILO / f"charla-{tema}.mplstyle"])
    tinta, tenue = plt.rcParams["text.color"], plt.rcParams["axes.edgecolor"]
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0 * CM, 5.4 * CM), constrained_layout=True)
    yp = np.logspace(-1, 2.3, 200)
    ley = lambda y, k: np.log(1 + k * y) / k + 7.8 * (1 - np.exp(-y / 11) - y / 11 * np.exp(-y / 3))  # Reichardt
    a.plot(yp[yp < 12], yp[yp < 12], color=tenue, lw=0.6, ls=":")
    for i, (k, et) in enumerate([(0.41, r"\textsc{imp asgs}"), (0.40, r"\textsc{imp oss}"), (0.43, r"\textsc{exp + vreman}")]):
        a.plot(yp, ley(yp, k) * (1 - 0.02 * i), label=et)
        b.plot(yp, 2.7 * yp / 15 * np.exp(1 - yp / 15) * (1 - 0.05 * i))
    yd = np.logspace(-0.5, 2.2, 14)
    a.plot(yd, ley(yd, 0.41), "o", mfc="none", mew=0.6, color=tinta, ms=2.6, label="DNS")
    b.plot(yd, 2.7 * yd / 15 * np.exp(1 - yd / 15), "o", mfc="none", mew=0.6, color=tinta, ms=2.6)
    a.set(xscale="log", xlim=(0.2, 200), ylim=(0, 21), xlabel=r"$y^+$", ylabel=r"$\bar u_z^+$")
    b.set(xlim=(0, 180), ylim=(0, 3.1), xlabel=r"$y^+$", ylabel=r"$u'^{+}_{z,\mathrm{rms}}$")
    fig.legend(loc="outside upper center", ncol=4, columnspacing=1.0, handlelength=1.4)
    fig.savefig(AQUI / f"figs/fig-{tema}.pdf")
    plt.close(fig)
