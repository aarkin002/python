import json

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

for i in range(len(usr_lst)):
    if len(usr_lst) == len(hobby_lst):
        usr_dict[usr_lst[i]] = hobby_lst[i]
    elif len(usr_lst) > len(hobby_lst):
        usr_dict[usr_lst[i]] = None

usr_dict_json_dump = json.dumps(usr_dict, ensure_ascii=False)

with open('hobby_users.csv', 'w', encoding='utf-8') as f:
    f.write(usr_dict_json_dump)

with open('hobby_users.csv', 'r', encoding='utf-8') as f:
    usr_dict_load = json.load(f)

print('Получившийся словарь:\n', usr_dict, '\n')

with open('hobby_users.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print('Содержание файла:\n', content, '\n')

print('Десериализация в новый словарь:\n', usr_dict_load)
