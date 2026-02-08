from gas_params import *
import numpy as np
from numpy.polynomial.polynomial import polyroots
R = 8.314462618
import string


def check_input_p():
    msg = 'Введите давление в Паскалях (число > 0): '
    while True:
        p = input(msg)
        try:
            p = float(p)
            if p > 0:
                break
        except ValueError:
            pass
    return p


def check_input_t():
    msg = 'Введите температуру в Кельвинах (число > 0): '
    while True:
        t = input(msg)
        try:
            t = float(t)
            if t > 0:
                break
        except ValueError:
            pass
    return t

def check_input_gas():
    for i, key in enumerate(gases.keys()):
            print(f'{i + 1}: {key}')
    while True:
        gas_number = input('Введи номер газа: ')
        try:
            gas_number = int(gas_number)
            if 0 < gas_number <= len(gases.keys()):
                break
        except ValueError:
            pass
    gas_params = tuple(gases.values())[gas_number - 1]    
    return gas_params


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

def get_Z(A, B):
    f = -(A * B - B**2 - B**3)
    e = A - 2 * B - 3 * B**2 
    d = -(1 - B)
    roots = polyroots([f, e, d, 1])
    real_roots = roots[np.isreal(roots)].real
    positive_real = real_roots[real_roots > 0]
    return np.max(positive_real) if len(positive_real) > 0 else np.nan


P = check_input_p()
T = check_input_t()
# P = 2e6
# T = 300
# T_c, P_c, omega = gases['metan']
T_c, P_c, omega = check_input_gas()
params = (
    get_a_c(T_c, P_c),
    get_a(T_c, P_c, T, omega),
    get_alpha(omega, T, T_c),
    get_b(T_c, P_c),
    get_A(P, T, T_c, P_c, omega),
    get_B(P, T, T_c, P_c)
)
a_c, a, alpha, b, A, B = params
Z = get_Z(A, B)


print(f'для выбранного газа P={P / 1e6:.3f} МПа, T={T} К, T_c={T_c} К, P_c={P_c / 1e6:.3f} МПа , omega={omega}, \
      a_c={a_c:.3f}, a={a:.3f}, alpha={alpha:.3f}, b={b * 1e5:.3f}e-05, A={A:.3f}, B={B:.3f}')
print(f'Коэффициент сжимаемости: {Z:.3f}')



# TO DO сделать функцию вычисления Z
# применить это все к массивам значений и вывести на 3Д график
#  