import random


def get_jokes(n):
    jokes_lst = []
    for i in range(n):
        # Перемешиваем списки
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        # Добавляем значения к строке
        jokes_str = nouns[0] + ' ' + adverbs[0] + ' ' + adjectives[0]
        # Добавляем строку в список
        jokes_lst.append(jokes_str)
    print(jokes_lst)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Перехватываем ошибки c помощью try/except
try:
    n = (int(input("Введите нуное Вам кол-во шуток: ")))
except:
    n = (int(input("У Вас последняя попытка. Введите положительную цифру: ")))

# Перехватываем ошибки с помощью "while"
while n <= 0:
    n = (int(input('Цифра должна быть положительной: ')))

# Запускаем функцию
get_jokes(n)
