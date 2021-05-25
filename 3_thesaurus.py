def thesaurus(*args):
    thesaurus_dict = {}
    for i in range(len(args)):
        thesaurus_dict.setdefault(args[i][0], [])
        thesaurus_dict[args[i][0]].append(args[i])
    print(thesaurus_dict)


name_count = int(input('Введите кол-во(цифру) имен: '))
name = []

for _ in range(name_count):
    name.append(input("Введите 1 имя и нажмите ввод: "))


thesaurus(*name)
