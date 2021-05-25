import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    usr_str = f'{sys.argv[1]}\n'
    f.write(usr_str)
