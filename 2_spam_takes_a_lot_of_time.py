import requests

ip_count = 0
spam_ip = 0

url = 'https://github.com/elastic/examples/raw/master/' \
      'Common%20Data%20Formats/nginx_logs/nginx_logs'

usr_lst = []

response = requests.get(url).text.splitlines()

for item in response[1:]:
    ip_end = item.find(' - - [')
    ip_code = item[0:ip_end]
    if len(ip_code) > 1:
        usr_lst.append(ip_code)

for ip in usr_lst:
    ip_count_spam = usr_lst.count(ip)
    if ip_count < ip_count_spam:
        ip_count = ip_count_spam
        spam_ip = ip

print("Кол-во запросов: ", ip_count)
print("С ip: ", spam_ip)
