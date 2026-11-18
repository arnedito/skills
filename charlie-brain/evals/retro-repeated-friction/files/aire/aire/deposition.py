def sedimentation_velocity(rho_p, rho_f, d, mu, g=9.81):
    """Terminal Stokes settling velocity."""
    return (rho_p - rho_f) * g * d**2 / (18 * mu)
