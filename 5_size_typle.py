import os
import json

root_dir = r'C:\Users\alexey\Desktop\Учеба\Основная' \
           r'\Yarkin_Alexey_dz_7\some_data'

count_100 = 0
file_ext_100 = []
count_1000 = 0
file_ext_1000 = []
count_10000 = 0
file_ext_10000 = []
count_100000 = 0
file_ext_100000 = []

for root, dirs, files in os.walk(root_dir):
    for i in range(len(files)):
        file_size = os.stat(os.path.join(root, files[i])).st_size
        if 0 <= file_size < 1000:
            count_100 += 1
            file_name, file_ext = os.path.splitext(files[i])
            file_ext_100.append(file_ext)
        if 1000 <= file_size < 10000:
            count_1000 += 1
            file_name, file_ext = os.path.splitext(files[i])
            file_ext_1000.append(file_ext)
        if 10000 <= file_size < 100000:
            count_10000 += 1
            file_name, file_ext = os.path.splitext(files[i])
            file_ext_10000.append(file_ext)
        if 100000 <= file_size:
            count_100000 += 1
            file_name, file_ext = os.path.splitext(files[i])
            file_ext_100000.append(file_ext)


files_size_dict = {'100': (count_100, [*(set(file_ext_100))]), '1000': (count_1000, [*(set(file_ext_1000))]),
                   '10000': (count_10000, [*(set(file_ext_10000))]),
                   '100000': (count_100000, [*(set(file_ext_100000))])}

files_size_dict_json = json.dumps(files_size_dict, ensure_ascii=False)

with open('size_typle.json', 'w', encoding='utf-8') as f:
    f.write(files_size_dict_json)

with open('size_typle.json', 'r', encoding='utf-8') as f:
    files_size_dict_after_json = json.load(f)

print(files_size_dict_after_json)
