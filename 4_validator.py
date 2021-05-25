def val_checker(func):
    def checker(*args):
        for arg in args:
            msg = f'ValueError: wrong val {arg}'
            if arg > 0:
                usr_value = func(arg)
                return usr_value
            else:
                raise ValueError(msg)

    return checker


@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(12))
