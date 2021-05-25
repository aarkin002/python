"""
Согласно условию не удалось решить, реализовал,
как смог поэтому мне было бы очень интересно
увидеть правмильное,
"""
import sys


with open('bakery.csv', 'r+', encoding='utf-8') as f:
    usr_line = f.readlines()

    if len(usr_line) >= int(sys.argv[1]):
        usr_data = str(usr_line[int(sys.argv[1]) - 1])
        usr_index = usr_line.index(usr_data)
        usr_line[usr_index] = f'{sys.argv[2]}\n'
        usr_str = ''.join(usr_line)
        f.seek(0)
        f.write(usr_str)
    else:
        print('Такой строки не существует.\n'
              'Запись новых значений осуществляется через '
              '6_add_backery_Terminal.py')
