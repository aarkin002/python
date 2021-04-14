usr_lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = ''

for i in range(len(usr_lst)):
    if usr_lst[i].isalpha():
        message += usr_lst[i]
        message += ' '
    elif len(usr_lst[i]) < 2:
        message = message + '"' + '0' + usr_lst[i] + '"'
        message += ' '
    elif usr_lst[i].isdigit():
        message = message + '"' + usr_lst[i] + '"'
        message += ' '
    elif '+' in usr_lst[i] and len(usr_lst[i]) == 2:
        usr_lst_2 = usr_lst[i].split('+')
        usr_lst_2.insert(0, "+0")
        usr_lst_2 = ''.join(usr_lst_2)
        message = message + '"' + usr_lst_2 + '"'
        message += ' '
    elif '-' in usr_lst[i] and len(usr_lst[i]) == 2:
        usr_lst_2 = usr_lst[i].split('-')
        usr_lst_2.insert(0, "-0")
        usr_lst_2 = ''.join(usr_lst_2)
        message = message + '"' + usr_lst_2 + '"'
        message += ' '

print(message)
