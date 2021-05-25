import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    line_list = content.splitlines()
    try:
        if len(sys.argv) == 1:
            print(content)
        elif len(sys.argv) == 2:
            usr_data = (line_list[i] for i in
                        range(int(sys.argv[1])-1, len(line_list)))
            print(*usr_data, sep='\n')
        elif len(sys.argv) == 3:
            usr_data = (line_list[i] for i in
                        range(int(sys.argv[1]) - 1, int(sys.argv[2])))
            print(*usr_data, sep='\n')
    except IndexError:
        print('В списке всего: ', len(line_list), 'строк.')