def usr_generator(usr_n):
    for i in range(1, usr_n+1, 2):
        yield i**2


usr_gen = usr_generator(int(input('Введите целое, положительное число: ')))

print("Тип:", type(usr_gen))
print(*usr_gen)
