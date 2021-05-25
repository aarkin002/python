import sys

usr_lst = []
hobby_lst = []
usr_dict = {}


def create_lst(name_file, name_lst):
    with open(name_file, 'r', encoding='utf-8') as f:
        usr_line = f.readline()
        while usr_line:
            usr_line = usr_line.replace('\n', '')
            if name_file == 'users.csv':
                usr_line = usr_line.replace(',', ' ')
            name_lst.append(usr_line)
            usr_line = f.readline()


try:
    create_lst(sys.argv[1], usr_lst)
    create_lst(sys.argv[2], hobby_lst)

    with open(sys.argv[3], 'w', encoding='utf-8') as f:
        for i in range(len(usr_lst)):
            p = usr_lst[i] + ':', hobby_lst[i]
            f.write(' '.join(p))
            f.write('\n')

    with open(sys.argv[3], 'r', encoding='utf-8') as f:
        content = f.read()
        print('Содержание файла:\n' + content)
except IndexError:
    print("Что-то пошло не так, скорее всего, проблема с вводом аргументов!\n"
          "После >python3 5_terminal.py - поочередно, "
          "через пробел, нужно ввести названия уже существующих:\n"
          "Файл с именами пользователей, файл с их хобби и файл с выходными данными.")
