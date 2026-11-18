import math

def stokes_einstein(T, mu, r):
    """Diffusion coefficient of a sphere (Einstein 1905, eq. 5)."""
    kB = 1.380649e-23
    return kB * T / (6 * math.pi * mu * r)
