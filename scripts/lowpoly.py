"""Ilustraciones low-poly de fondo (pulmones, nariz, o cualquier silueta) como fragmento TikZ.

Versión limpia de ~/imagenes/pulmones_lowpoly/lowpoly_2d.py: un solo color (`motivo`, que pone cada
tema), sin halos ni niebla, pocas partículas flotando. Así se tiñe con el tema y funciona igual sobre
fondo claro y oscuro.

  python lowpoly.py pulmones                       -> pulmones.tex
  python lowpoly.py nariz --imagen nariz.png       -> nariz.tex (silueta sacada de un render con fondo blanco)
  python lowpoly.py <nombre> --imagen x.png [--huecos 14] [--seed 3] [--flotantes 8] [--llegando 4]

--imagen: la silueta es lo que no es blanco; --huecos vacía las sombras más oscuras del render (percentil),
que en una nariz son los meatos: así se leen los cornetes y no solo el contorno (0 = solo contorno).
Necesita numpy, scipy, matplotlib y Pillow (entorno conda 'aire').
"""
import argparse
from pathlib import Path

import numpy as np
from matplotlib.path import Path as MPath
from scipy.interpolate import splev, splprep
from scipy.ndimage import binary_fill_holes, gaussian_filter, label
from scipy.spatial import Delaunay, cKDTree

# siluetas de los pulmones (mm, y hacia arriba), de lowpoly_2d.py
PULMON_I = [(34, 104), (27, 100), (21, 92), (16, 81), (12, 68), (8, 54), (5, 40), (3, 27), (2.5, 16),
            (4, 9), (9, 6), (16, 6.5), (24, 9), (32, 12.5), (40, 16.5), (47, 21), (52, 27), (54, 36),
            (55, 48), (55, 60), (54.5, 72), (53, 83), (50, 93), (46, 100), (40, 104)]
PULMON_D = [(86, 104), (93, 100), (99, 92), (104, 81), (108, 68), (112, 54), (115, 40), (117, 27),
            (117.5, 16), (116, 9), (111, 6), (104, 6.5), (96, 8.5), (88, 11), (80, 13), (74, 15), (70, 19),
            (68.5, 25), (69.5, 31), (68, 37), (66, 45), (65.5, 58), (65.5, 70), (67, 83), (70, 93),
            (74, 100), (80, 104)]
TRAQUEA = [(57.5, 117), (62.5, 117), (62.7, 86), (65, 81), (68.5, 75.5), (66.8, 73.5), (62, 79),
           (60, 80.5), (58, 79), (53.2, 73.5), (51.5, 75.5), (55, 81), (57.3, 86)]


# ----------------------------------------------------------------------------- geometría
def suavizar(ctrl, n=600, suave=True):
    P = np.asarray(ctrl, float)
    if not suave:
        return remuestrear(P, perimetro(P) / n, None)
    tck, _ = splprep([P[:, 0], P[:, 1]], s=len(P) * 0.04, per=1)
    x, y = splev(np.linspace(0, 1, n, endpoint=False), tck)
    return np.column_stack([x, y])


def perimetro(c):
    return np.linalg.norm(np.diff(np.vstack([c, c[:1]]), axis=0), axis=1).sum()


def remuestrear(c, h, rng, ruido=0.25):
    C = np.vstack([c, c[:1]])
    s = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(C, axis=0), axis=1))])
    n = max(int(s[-1] / h), 6)
    t = np.arange(n) + (rng.uniform(-ruido, ruido, n) if rng is not None else 0)
    t = np.mod(t * s[-1] / n, s[-1])
    return np.column_stack([np.interp(t, s, C[:, 0]), np.interp(t, s, C[:, 1])])


class Pieza:
    """Una silueta cerrada (con huecos opcionales): test dentro/fuera y distancia al borde más cercano."""

    def __init__(self, curva, huecos=()):
        self.curva, self.huecos = curva, list(huecos)
        self.path = MPath(curva)
        self.paths_h = [MPath(h) for h in self.huecos]
        self.arbol = cKDTree(np.vstack([remuestrear(c, 0.15, None) for c in [curva] + self.huecos]))

    def dentro(self, p):
        p = np.atleast_2d(p)
        ok = self.path.contains_points(p)
        for h in self.paths_h:
            ok &= ~h.contains_points(p)
        return ok

    def dist(self, p):
        return self.arbol.query(np.atleast_2d(p))[0]

    def capa(self, delta, h, rng):
        """Puntos a distancia delta hacia dentro, separados h: triángulos estirados junto al borde."""
        out = []
        for curva in [self.curva] + self.huecos:
            c = remuestrear(curva, h, rng, 0.4)
            sig = np.roll(c, -1, axis=0) - np.roll(c, 1, axis=0)
            nrm = np.column_stack([-sig[:, 1], sig[:, 0]])
            nrm /= np.linalg.norm(nrm, axis=1, keepdims=True) + 1e-12
            q = np.vstack([c + delta * nrm, c - delta * nrm])
            q = q[self.dentro(q) & (np.abs(self.dist(q) - delta) < 0.35 * delta)]
            out.append(q[rng.random(len(q)) > 0.2])
        return np.vstack(out)


def poisson(pieza, tam, rng, dmin, intentos=9000):
    lo, hi = pieza.curva.min(0), pieza.curva.max(0)
    pts, hs = [], []
    for _ in range(intentos):
        p = rng.uniform(lo, hi)
        if not pieza.dentro(p)[0]:
            continue
        d = pieza.dist(p)[0]
        if d < dmin:
            continue
        h = tam(d) * rng.uniform(0.8, 1.25)
        if pts and np.any(np.linalg.norm(np.array(pts) - p, axis=1) < 0.5 * (np.array(hs) + h)):
            continue
        pts.append(p)
        hs.append(h)
    return np.array(pts).reshape(-1, 2)


def mallar(pieza, hb, hc, rng, capas=None):
    """Malla gradada: fina en el contorno y en los huecos (hb), gruesa dentro (hc)."""
    bnd = np.vstack([remuestrear(c, hb, rng) for c in [pieza.curva] + pieza.huecos])
    capas = [(1.6 * hb / 3, 2.1 * hb), (4.2 * hb / 3, 3.0 * hb)] if capas is None else capas
    lay = np.vstack([pieza.capa(d, s, rng) for d, s in capas]) if capas else np.zeros((0, 2))
    d0 = capas[-1][0] + 0.45 * capas[-1][1] if capas else 0.6 * hc
    D, hin = 1.5 * hc, (capas[-1][1] if capas else hb)
    tam = lambda d: hin + (hc - hin) * np.clip((d - d0) / (D - d0 + 1e-9), 0, 1) ** 0.8
    inn = poisson(pieza, tam, rng, d0)
    pts = np.vstack([bnd, lay, inn])
    tri = Delaunay(pts).simplices
    tri = tri[pieza.dentro(pts[tri].mean(axis=1))]
    return pts, tri


# ----------------------------------------------------------------------------- siluetas
def silueta_imagen(ruta, ancho_mm, huecos):
    """Contorno de un render con fondo blanco (lo que no es blanco) y, si huecos > 0, las sombras más
    oscuras como huecos de la malla: en una nariz son los meatos, y dejan ver los cornetes."""
    from PIL import Image
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from scipy.ndimage import binary_erosion

    im = Image.open(ruta).convert("L")
    esc = min(1, 700 / max(im.size))
    g = np.asarray(im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)).astype(float)
    masc = binary_fill_holes(gaussian_filter((g < 245).astype(float), 1.2) > 0.5)
    lab, _ = label(masc)
    masc = lab == (np.argmax(np.bincount(lab.ravel())[1:]) + 1)
    fig, ax = plt.subplots()
    curvas = [max(ax.contour(gaussian_filter(masc.astype(float), 2.0), levels=[0.5]).allsegs[0], key=len)]
    if huecos > 0:
        oscuro = gaussian_filter(g, 3.0) < np.percentile(g[masc], huecos)
        oscuro &= binary_erosion(masc, iterations=14)          # lejos del contorno: sin puentes finos
        lab, n = label(oscuro)
        for i in range(1, n + 1):
            if (lab == i).sum() < 0.004 * masc.sum():
                continue
            segs = ax.contour(gaussian_filter((lab == i).astype(float), 2.5), levels=[0.5]).allsegs[0]
            curvas.append(max(segs, key=len))
    plt.close(fig)
    a_mm = lambda p: np.column_stack([p[:, 0], g.shape[0] - p[:, 1]]) * ancho_mm / g.shape[1]
    return [a_mm(c) for c in curvas]


# ----------------------------------------------------------------------------- escena
def escena(piezas_mallas, rng, n_flot=8, n_tri_flot=3, n_llegando=4):
    """Triángulos, aristas, nodos, triángulos que llegan y unos pocos flotantes. Todo en mm."""
    todos = np.vstack([p.curva for p, *_ in piezas_mallas])
    lo, hi = todos.min(0), todos.max(0)
    off = np.array([12.0, 8.0]) - lo
    W, H = hi - lo + np.array([24.0 + (24 if n_llegando else 0), 16.0 + (6 if n_llegando else 0)])
    tris, aristas, nodos, llegan, estelas, flot = [], set(), [], [], [], []

    quitados = set()
    if n_llegando:                     # huecos en la esquina superior derecha de la pieza mayor
        grandes = [i for i in range(len(piezas_mallas)) if len(piezas_mallas[i][2]) > 60]
        k = max(grandes, key=lambda i: (piezas_mallas[i][0].curva @ [1, 0.6]).max())
        pieza, pts, tri, _ = piezas_mallas[k]
        cen = pts[tri].mean(axis=1)
        ancla = pieza.curva[np.argmax(pieza.curva[:, 0] + 0.6 * pieza.curva[:, 1])]
        T3 = pts[tri]
        u, v = T3[:, 1] - T3[:, 0], T3[:, 2] - T3[:, 0]
        area = 0.5 * np.abs(u[:, 0] * v[:, 1] - u[:, 1] * v[:, 0])
        cerca = np.argsort(np.linalg.norm(cen - ancla, axis=1))
        grandes = [j for j in cerca[1:] if area[j] > 12][:n_llegando - 1]
        orden = np.array([cerca[0]] + grandes)      # uno fino del borde y varios grandes de dentro
        quitados = {(k, int(j)) for j in orden}
        dirc = np.array([1.0, 0.95]) / np.hypot(1, 0.95)
        perp = np.array([-dirc[1], dirc[0]])
        puestos = []
        for t, j in zip(np.linspace(0.3, 1.0, n_llegando), orden):
            T = pts[tri[j]]
            c = T.mean(0)
            for _ in range(200):
                dest = c + t * 40 * dirc + perp * rng.uniform(-9, 9) * t
                if all(np.linalg.norm(dest - q) > 9 for q in puestos):
                    break
            puestos.append(dest)
            a = rng.choice([-1, 1]) * t * rng.uniform(0.7, 1.5)
            R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
            llegan.append(((T - c) @ R.T * (1 - 0.3 * t) + dest + off, 0.45 * (1 - 0.5 * t) + 0.1))
            estelas.append((c + off + (dest - c) * 0.18, dest + off - (dest - c) * 0.12, 0.45 * (1 - 0.4 * t)))
            tris.append((T + off, 0.03, True))      # el hueco: solo contorno discontinuo

    for k, (pieza, pts, tri, hesc) in enumerate(piezas_mallas):
        d = pieza.dist(pts[tri].mean(axis=1)) / hesc
        for j, s in enumerate(tri):
            if (k, j) in quitados:
                continue
            a = 0.40 * np.exp(-d[j] / 0.4) + rng.uniform(0.03, 0.08)
            if rng.random() < 0.05:
                a = rng.uniform(0.25, 0.4)
            tris.append((pts[s] + off, float(min(a, 0.55)), False))
            for e in ((s[0], s[1]), (s[1], s[2]), (s[0], s[2])):
                aristas.add((k,) + tuple(sorted(map(int, e))))
        usados = np.unique(tri)
        nodos += [tuple(p) for p in pts[usados] + off]

    sil = np.vstack([p.curva for p, *_ in piezas_mallas]) + off
    arbol = cKDTree(sil)
    ocupado = [(T.mean(0), 7.0) for T, _ in llegan]

    def hueco(margen):
        for _ in range(800):
            p = rng.uniform([margen + 2, margen + 2], [W - margen - 2, H - margen - 2])
            if arbol.query(p)[0] < margen + 4 or any(piezas_mallas[i][0].dentro(p - off)[0]
                                                     for i in range(len(piezas_mallas))):
                continue
            if any(np.linalg.norm(p - c) < margen + r + 3 for c, r in ocupado):
                continue
            ocupado.append((p, margen))
            return p
        return None

    for _ in range(n_flot):
        p = hueco(2)
        if p is not None:
            flot.append(("punto", p, rng.uniform(0.5, 1.1), rng.uniform(0.35, 0.75)))
    for _ in range(n_tri_flot):
        tam = rng.uniform(3.5, 7)
        p = hueco(tam * 0.8)
        if p is None:
            continue
        ang = rng.uniform(0, 2 * np.pi) + np.array([0, 2.1, 4.3]) + rng.uniform(-0.3, 0.3, 3)
        r = tam * rng.uniform(0.6, 1.0, 3)
        flot.append(("tri", p + np.column_stack([r * np.cos(ang), r * np.sin(ang)]),
                     rng.random() < 0.5, rng.uniform(0.25, 0.4)))

    seg = []
    for k, i, j in aristas:
        P = piezas_mallas[k][1]
        seg.append((P[i] + off, P[j] + off))
    return dict(W=W, H=H, tris=tris, seg=seg, nodos=nodos, llegan=llegan, estelas=estelas, flot=flot)


# ----------------------------------------------------------------------------- TikZ
def f(x):
    return f"{x:.2f}"


def pt(p):
    return f"({f(p[0])},{f(p[1])})"


def tikz(e, nombre, fuente):
    L = [f"%% {nombre} low-poly (charlas-charlie, scripts/lowpoly.py {fuente}).",
         "%% Un solo color: `motivo` (lo define el tema). Escala: \\lpscale (1 = 1 unidad por mm).",
         "\\providecommand{\\lpscale}{1}",
         "\\begin{tikzpicture}[x=\\lpscale mm,y=\\lpscale mm,line join=round,line cap=round]",
         f"\\path (0,0) rectangle ({f(e['W'])},{f(e['H'])});",
         "% --- triángulos (más opacos junto al borde)"]
    for T, a, hueco in e["tris"]:
        if hueco:
            L.append(f"\\draw[motivo,draw opacity=0.55,line width=0.18mm*\\lpscale,dash pattern=on 0.7mm off 0.6mm] "
                     f"{pt(T[0])}--{pt(T[1])}--{pt(T[2])}--cycle;")
        else:
            L.append(f"\\fill[motivo,fill opacity={a:.3f}] {pt(T[0])}--{pt(T[1])}--{pt(T[2])}--cycle;")
    L.append("% --- aristas")
    L.append("\\begin{scope}[motivo,draw opacity=0.7,line width=0.2mm*\\lpscale]")
    L += [f"\\draw {pt(a)}--{pt(b)};" for a, b in e["seg"]]
    L.append("\\end{scope}")
    L.append("% --- nodos")
    L.append("\\begin{scope}[motivo]")
    L += [f"\\fill {pt(p)} circle (0.36);" for p in e["nodos"]]
    L.append("\\end{scope}")
    L.append("% --- triángulos que llegan a la malla")
    for (a, b, op) in e["estelas"]:
        L.append(f"\\draw[motivo,draw opacity={op:.2f},line width=0.18mm*\\lpscale,dash pattern=on 0.5mm off 0.9mm] "
                 f"{pt(a)}--{pt(b)};")
    for T, op in e["llegan"]:
        L.append(f"\\filldraw[fill=motivo,fill opacity={op:.2f},draw=motivo,draw opacity=0.85,"
                 f"line width=0.2mm*\\lpscale] {pt(T[0])}--{pt(T[1])}--{pt(T[2])}--cycle;")
    L.append("% --- unos pocos flotantes")
    for tipo, *r in e["flot"]:
        if tipo == "punto":
            p, rad, op = r
            L.append(f"\\fill[motivo,fill opacity={op:.2f}] {pt(p)} circle ({f(rad)});")
        else:
            T, relleno, op = r
            estilo = f"fill=motivo,fill opacity={op:.2f}" if relleno else \
                "draw=motivo,draw opacity=0.7,line width=0.3mm*\\lpscale"
            L.append(f"\\path[{estilo}] {pt(T[0])}--{pt(T[1])}--{pt(T[2])}--cycle;")
    L.append("\\end{tikzpicture}")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("nombre")
    ap.add_argument("--imagen", help="render con fondo blanco; sin esto: pulmones")
    ap.add_argument("--ancho", type=float, default=150, help="ancho de la silueta en mm")
    ap.add_argument("--huecos", type=float, default=14, help="percentil de sombra que se vacía (0 = ninguno)")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--hborde", type=float, default=3.0)
    ap.add_argument("--hcentro", type=float, default=17.0)
    ap.add_argument("--flotantes", type=int, default=8)
    ap.add_argument("--llegando", type=int, default=4)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    if a.imagen:
        curvas = [suavizar(remuestrear(c, 2.0, None), n=max(60, int(perimetro(c) / 0.5)))
                  for c in silueta_imagen(a.imagen, a.ancho, a.huecos)]
        p = Pieza(curvas[0], curvas[1:])
        mallas = [(p, *mallar(p, a.hborde, a.hcentro, rng), 5.0)]
        fuente = f"{a.nombre} --imagen {Path(a.imagen).name}"
    else:
        mallas = []
        for ctrl, hb, hc, suave, capas, hs in [(PULMON_I, a.hborde, a.hcentro, True, None, 5.0),
                                               (PULMON_D, a.hborde, a.hcentro, True, None, 5.0),
                                               (TRAQUEA, 2.4, 4.5, False, [], 3.0)]:
            p = Pieza(suavizar(ctrl, suave=suave))
            mallas.append((p, *mallar(p, hb, hc, rng, capas=capas), hs))
        fuente = a.nombre
    e = escena(mallas, rng, a.flotantes, 3 if a.flotantes else 0, a.llegando)
    out = Path(a.out or f"{a.nombre}.tex")
    out.write_text(tikz(e, a.nombre, fuente))
    print(f"{out}: {len(e['tris'])} triángulos, {len(e['flot'])} flotantes, {len(e['llegan'])} llegando")
