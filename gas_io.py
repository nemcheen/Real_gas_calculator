from gas_params import gases, R


alpha_symbol = '\u03B1'
omega_symbol = '\u03C9'


def check_input_p():
    msg = 'Введите давление в Паскалях (Па): '
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
    msg = 'Введите температуру в Кельвинах (К): '
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
    name_gas = tuple((gases.keys()))[gas_number - 1]
    gas_params = gas_params + (name_gas, ) 
    return gas_params


def make_report(T, P, T_c, gas, P_c, omega, a_c, k, alpha, a, b, A, B, Z, V_ideal, V_real):
    """
    Формирует текстовый отчет о расчете коэффициента сжимаемости по уравнению Пенга–Робинсона.
    """
    # Преобразования единиц (используем функции из calc.py)
    from calc import kelvin_to_celsius, pa_to_atm
    
    T_C = kelvin_to_celsius(T)
    P_atm = pa_to_atm(P)
    
    # Давление в МПа (1 МПа = 1e6 Па)
    P_MPa = P / 1e6
    
    # Разница объемов в процентах
    diff_percent = abs(V_ideal - V_real) / V_ideal * 100
    
    # Интерпретация значения Z
    if Z < 0.98:
        interpretation = "Коэффициент сжимаемости меньше 1.\n" \
                         "               В данных условиях силы притяжения между молекулами газа существенны."
    elif Z > 1.02:
        interpretation = "Коэффициент сжимаемости больше 1.\n" \
                         "               В данных условиях преобладают силы отталкивания между молекулами."
    else:
        interpretation = "Коэффициент сжимаемости близок к 1.\n" \
                         "               Газ ведет себя практически как идеальный."
    
    # Форматирование чисел
    # Давление: с разделителями тысяч
    P_formatted = f"{P:,.0f}".replace(",", " ")
    # Объемы: 6 знаков после запятой
    V_ideal_f = f"{V_ideal:.6f}"
    V_real_f  = f"{V_real:.6f}"
    # Z: 2 знака после запятой
    Z_f = f"{Z:.2f}"
    # Процент разницы: 1 знак после запятой
    diff_f = f"{diff_percent:.1f}"
    
    # Сборка отчета
    report = f"""Расчет коэффициента сжимаемости метана по уравнению Пенга-Робинсона.
    ----------------------------------------------------------
    Введено давление (Па): {P_formatted}       ({P_MPa:.1f} МПа ~ {P_atm:.0f} атмосфер)
    Введена температура (К): {T:.0f}     (~{T_C:.0f} °C)
    Газ: {gas}
    T критическая: {T_c} K   (~{kelvin_to_celsius(T_c):.0f} °C) 
    P критическое: {P_c} Па  ({P_c / 1e6:.1f} МПа ~ {pa_to_atm(P_c):.0f} атмосфер)
    ацентрический коэффициент {omega_symbol} = {omega}
    ----------------------------------------------------------
    РЕЗУЛЬТАТЫ РАСЧЕТА:

    Промежуточные параметры:
    a_c = {a_c:.3f}
    k = {k:.3f}
    {alpha_symbol} = {alpha:.3f}
    a = {a:.3f}
    b = {b * 1e6:.3f} * 1e-6
    A = {A:.3f}
    B = {B:.3f}
    ----------------------------------------------------------
    Коэффициент сжимаемости, Z = {Z_f}

    Интерпретация: {interpretation}
    ----------------------------------------------------------
    Сравнение объемов:
    Молярный объем (идеальный газ): {V_ideal_f} м³/моль
    Молярный объем (реальный газ):  {V_real_f} м³/моль
    Разница составляет около {diff_f}%."""
    
    print(report)
    return report


