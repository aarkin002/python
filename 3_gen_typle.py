tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис',
          'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

# Оба закомментированных генератора подойдут для данных списков из методички, тк len(tutors) < len(klasses)
# usr_gen = ((tutor, klass) for tutor,klass in zip(tutors, klasses))
# usr_gen = ((tutors[i], klasses[i])for i in range(len(tutors)))

"""
 Ниже вариант, если len(tutors) > len(klasses), но мне кажется, 
 последняя строка функции usr_generator() является костылем
"""


def usr_generator():
    for i in range(len(tutors)):
        if i < len(klasses):
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None


usr_gen = usr_generator()

print("Тип: ", type(usr_gen))
print("Полный генератор: ", *usr_gen)
print("Пустой генератор: ", *usr_gen)
