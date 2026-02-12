from gas_params import gases, R
import numpy as np
from numpy.polynomial.polynomial import polyroots


def get_A(P, T, T_c, P_c, omega):
    a = get_a(T_c, P_c, T, omega)
    A = (a * P) / (R**2 * T**2)
    return A


def get_B(P, T, T_c, P_c):
    b = get_b(T_c, P_c)
    B = (b * P) / (R * T)
    return B


def get_a(T_c, P_c, T, omega):
    a = get_a_c(T_c, P_c) * get_alpha(omega, T, T_c)
    return a


def get_a_c(T_c, P_c):
    a_c = 0.45724 * (R**2 * T_c**2) / P_c
    return a_c


def get_alpha(omega, T, T_c):
    k = 0.37464 + 1.54226 * omega - 0.26992 * omega**2
    T_pr = T / T_c
    alpha = (1 + k * (1 - T_pr**0.5))**2
    return alpha


def get_b(T_c, P_c):
    b = 0.07780 * R * T_c / P_c
    return b


def get_Z(P, T, gas='metan'):
    T_c, P_c, omega = gases[gas]
    A = get_A(P, T, T_c, P_c, omega)
    B = get_B(P, T, T_c, P_c)
    f = -(A * B - B**2 - B**3)
    e = A - 2 * B - 3 * B**2 
    d = -(1 - B)
    roots = polyroots([f, e, d, 1])
    real_roots = roots[np.isreal(roots)].real
    positive_real = real_roots[real_roots > 0]
    return np.max(positive_real) if len(positive_real) > 0 else np.nan