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


create_lst('users.csv', usr_lst)
create_lst('hobby.csv', hobby_lst)

with open('hobby_users_no_dict.csv', 'w', encoding='utf-8') as f:
    for i in range(len(usr_lst)):
        p = usr_lst[i] + ':', hobby_lst[i]
        f.write(' '.join(p))
        f.write('\n')

with open('hobby_users_no_dict.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print('Содержание файла:\n' + content)
