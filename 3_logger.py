"""Задачи возводить в куб не было, поэтому 'func' не использовался"""


def type_logger(func):
    def logger(*args, **kwargs):
        logger_dict = {}
        for arg in args:
            key_a = str(arg)
            logger_dict[key_a] = type(arg)
        for k in kwargs:
            key_k = str(k)
            logger_dict[key_k] = type(k)
        return logger_dict

    return logger


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube('asgir', '509', 5, 5.2)

print(a)
