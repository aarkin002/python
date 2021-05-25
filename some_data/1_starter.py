import os

project_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in project_dirs:
    dir_path = os.path.join('my_project', folder)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
