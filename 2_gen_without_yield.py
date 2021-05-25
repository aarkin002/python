n = int(input("Введите целое число :"))

usr_gen = (i**2 for i in range(1, n+1, 2))

print("Тип:", type(usr_gen))
print(*usr_gen)
