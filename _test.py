from demo_orifice_calc import orifice_calc

def test1():
  assert abs(orifice_calc(2.35, 0.881, 6.0) - 0.586) < 1e-3