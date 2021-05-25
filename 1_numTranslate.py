def num_translate(key):
    try:
        print(usr_dict[key])
    except:
        print('None')


usr_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

usr_number = input("Введите цифру прописью на английском:")

num_translate(usr_number.lower())
