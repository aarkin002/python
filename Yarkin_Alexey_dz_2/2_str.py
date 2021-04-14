usr_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
usr_lst_1 = []

for i in range(len(usr_lst)):
    if usr_lst[i].isalpha():
        usr_lst_1.append(usr_lst[i])
    elif usr_lst[i].isdigit():
        usr_lst_1.append('"')
        if len(usr_lst[i]) < 2:
            usr_lst[i] = '0' + usr_lst[i]
        usr_lst_1.append(usr_lst[i])
        usr_lst_1.append('"')
    elif '+' in usr_lst[i] and len(usr_lst[i]) == 2:
        usr_lst_1.append('"')
        usr_lst_2 = usr_lst[i].split('+')
        usr_lst_2.insert(0, "+0")
        usr_lst_2 = ''.join(usr_lst_2)
        usr_lst_1.append(usr_lst_2)
        usr_lst_1.append('"')
    elif '-' in usr_lst[i] and len(usr_lst[i]) == 2:
        usr_lst_1.append('"')
        usr_lst_2 = usr_lst[i].split('-')
        usr_lst_2.insert(0, "-0")
        usr_lst_2 = ''.join(usr_lst_2)
        usr_lst_1.append(usr_lst_2)
        usr_lst_1.append('"')
print(usr_lst_1)

for j in range(len(usr_lst_1)):
    if usr_lst_1[j].isalpha():
        print(usr_lst_1[j], end=' ')
    elif usr_lst_1[j] == '"':
        print(end='')
    else:
        print('"' + usr_lst_1[j] + '"', end=' ')
