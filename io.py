from gas_params import gases, R

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


def make_report(T, P, Z):
    pass


