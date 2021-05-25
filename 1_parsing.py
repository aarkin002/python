import requests

url = 'https://github.com/elastic/examples/raw/master/' \
      'Common%20Data%20Formats/nginx_logs/nginx_logs'

usr_lst = []
response = requests.get(url).text.split('\n')

for item in response[1:]:
    ip_end = item.find(' - - [')
    ip_code = item[0:ip_end]
    downloads_start = item.find('/downloads')
    get_start = item.find('] "')
    get_code = item[get_start + 3:downloads_start - 1]
    downloads_code = item[downloads_start:item.find(' HTTP/')]
    if len(ip_code) > 1 and len(get_code) and len(downloads_code):
        usr_tupple = (ip_code, get_code, downloads_code)
        usr_lst.append(usr_tupple)

print(usr_lst)
