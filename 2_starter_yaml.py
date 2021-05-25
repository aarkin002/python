import yaml
import os

with open('config.yaml') as f:
    my_project_dict = yaml.safe_load(f)

for i in range(len(my_project_dict)):
    folder_key = list(my_project_dict.keys())[i]
    dir_path = os.path.join('my_project_yaml', folder_key)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for j in range(len(my_project_dict[folder_key])):
        file_lst = my_project_dict[folder_key]
        if '.' in file_lst[j]:
            with open(f'{dir_path}/{file_lst[j]}', 'w') as f:
                f.write('###Start###')
        elif file_lst[j] == dict(file_lst[j]):
            file_dict = file_lst[j]
            for y in range(len(file_dict)):
                file_dict_key = list(file_dict.keys())[y]
                dir_path = os.path.join(dir_path, file_dict_key)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                file_dict_finaly = file_dict[file_dict_key]
                for k in range(len(file_dict[file_dict_key])):
                    if file_dict_finaly == dict(file_dict_finaly):
                        file_dict_finaly_key = list(file_dict_finaly.keys())[k]
                        dir_path = os.path.join(dir_path, file_dict_finaly_key)
                        if not os.path.exists(dir_path):
                            os.makedirs(dir_path)
                        for _ in range(len(file_dict_finaly[file_dict_finaly_key])):
                            file_lst_finaly = file_dict_finaly[file_dict_finaly_key]
                            if '.' in file_lst_finaly[_]:
                                with open(f'{dir_path}/{file_lst_finaly[_]}', 'w') as f:
                                    f.write('###Start###')
