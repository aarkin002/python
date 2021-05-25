def thesaurus_adv(*args):
    thesaurus_dict = {}
    usr_lst = []
    for i in range(len(args)):
        usr_lst.append(args[i].split())
    for j in range(len(usr_lst)):
        thesaurus_dict.setdefault(usr_lst[j][1][0], [])
        thesaurus_dict[usr_lst[j][1][0]].append(args[j])
    print(thesaurus_dict)


name_count = int(input('Введите кол-во(цифру) имен: '))
name = []

for _ in range(name_count):
    name.append(input("Введите имя и фамилию через пробел, после чего нажмите ввод: "))

thesaurus_adv(*name)
