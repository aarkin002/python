import os
import shutil

root_dir = r'C:\Users\alexey\Desktop\Учеба\Основная' \
           r'\Yarkin_Alexey_dz_7\my_project_yaml'

if not os.path.exists(root_dir):
    print('Проекта не существует, неоткуда копировать!')
else:
    for root, dirs, file in os.walk(root_dir):
        if dirs == ['templates']:
            dir_path_src = os.path.join(root, 'templates')
            dir_path_dst = os.path.join(root_dir, 'Templates')
            shutil.copytree(dir_path_src, dir_path_dst, dirs_exist_ok=True)
