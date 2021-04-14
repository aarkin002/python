import random

numbers = []
numbers_new = []

for m in range(20):
    num_first = round(random.random() * 100, 2)
    numbers.append(num_first)

# Задание A
print('Задание A:')
for k in range(len(numbers)):
    num_next = str(numbers[k])
    numbers_new.append(num_next.split('.'))

for i in range(len(numbers_new)):
    for j in range(len(numbers_new[i])):
        if len(numbers_new[i][j]) < 2:
            numbers_new[i][j] = '0' + numbers_new[i][j]
        if j == 0:
            print(numbers_new[i][j], 'руб', end=' ')
        else:
            if i < len(numbers_new) - 1:
                print(numbers_new[i][j], 'коп,', end=' ')
            else:
                print(numbers_new[i][j], 'коп')
print()

# Задание B
print('Задание B:')
print('id начального списка: ', id(numbers))
numbers.sort()
print(numbers)
print('id отсортированного списка по возрастанию: ', id(numbers))
print()

# Задание C
print('Задание C:')
numbers_sort = sorted(numbers, reverse=True)
print(numbers_sort)
print('id отсортированного  по убыванию: ', id(numbers_sort))
print()

# Задание D
print('Задание D:')
print(sorted(numbers_sort[0:5]))
