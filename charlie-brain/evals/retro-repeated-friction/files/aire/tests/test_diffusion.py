from aire.diffusion import stokes_einstein

def test_positive():
    assert stokes_einstein(300, 1.8e-5, 1e-6) > 0
