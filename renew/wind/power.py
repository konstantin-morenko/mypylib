"""Calculating wind power"""

from ...conv import pressure

def set_std(temp, hum, press):
    """Set standard environment"""
    pass

def pwr(speed, temp, hum, press):
    """Calculate specific wind power."""
    return 0

def p_mb_sat(t):
    """Saturated steam pressure."""
    assert t > 0
    return 6.1078*10**((7.5*t-2048.625)/(t-35.85))

def p_sat(t):
    return conv.pressure.mbar2pa(m_mb_sat(t))

def p_u(t, rh):
    """Unsaturated steam pressure."""
    assert rh >= 0 and rh <= 1
    assert t > 0
    return rh * p_mb_sat(t)

def p_d(t, rh, p):
    """Dry air partial pressure."""
    return p - p_u(t, rh)

def rho(t, rh, p):
    """Air density."""
    return p_d(t, rh, p) / (287.058 * t) + p_u(t, rh) / (461.495 * t)

def sp_power(v, t, rh, p):
    """Specific wind power."""
    return (rho(t, rh, p) * v ** 3) / 2
