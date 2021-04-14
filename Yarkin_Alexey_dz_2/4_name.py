usr_lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(usr_lst)):
    usr_lst_parts = usr_lst[i].split(' ')
    print('Привет,', usr_lst_parts[-1].capitalize() + '!')
