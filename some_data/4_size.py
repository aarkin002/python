import os

root_dir = r'C:\Users\alexey\Desktop\Учеба\Основная' \
           r'\Yarkin_Alexey_dz_7\some_data'

count_100 = 0
count_1000 = 0
count_10000 = 0
count_100000 = 0

for root, dirs, files in os.walk(root_dir):
    for i in range(len(files)):
        file_size = os.stat(os.path.join(root, files[i])).st_size
        if 0 <= file_size < 1000:
            count_100 += 1
        if 1000 <= file_size < 10000:
            count_1000 += 1
        if 10000 <= file_size < 100000:
            count_10000 += 1
        if 100000 <= file_size:
            count_100000 += 1

files_size_dict = {100: count_100, 1000: count_1000, 10000: count_10000,
                   100000: count_100000}

print(files_size_dict)
