from gas_io import check_input_gas, check_input_p, check_input_t, make_report
from calc import *
from plot import make_plot


def main():
    T_c, P_c, omega, gas = check_input_gas()
    T = check_input_t()
    P = check_input_p()
    a_c = get_a_c(T_c, P_c)
    k = 0.37464 + 1.54226 * omega - 0.26992 * omega**2
    alpha = get_alpha(omega, T, T_c)
    a = get_a(T_c, P_c, T, omega)
    b = get_b(T_c, P_c)
    A = get_A(P, T, T_c, P_c, omega)
    B = get_B(P, T, T_c, P_c)
    Z = get_Z(P, T, gas=gas)
    V_ideal = get_V(T, P)
    V_real = get_V(T, P, Z=Z)
    make_report(T, P, T_c, gas, P_c, omega, a_c, k, alpha, a, b, A, B, Z, V_ideal, V_real)


if __name__ == '__main__':
    while True:
        answer = input("\nРасчитать параметры реального газа: [C]\nВывести 3D график Z(P, T) [Z]\nВыход [E]\n\n").lower()
        match answer:
            case 'c': 
                main()
            case 'с': # kirillic c 
                main()
            case 'z':
                T_c, P_c, omega, gas = check_input_gas()
                make_plot(gas=gas)
            case 'e':
                break
    
