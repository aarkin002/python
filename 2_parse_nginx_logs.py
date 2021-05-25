import requests
import re


def parsed_log_str(usr_re):
    if re.search(usr_re, log_str) is not None:
        remote_addr = re.search(usr_re, log_str)
        usr_ip = remote_addr.group()
        parsed_raw.append(usr_ip)


url = 'https://github.com/elastic/examples/raw/master/' \
      'Common%20Data%20Formats/nginx_logs/nginx_logs'

response = requests.get(url).text.split('\n')

readeable_parsed_raw = []

for log_str in response:
    parsed_raw = []
    parsed_log_str(r'(\d{1,3}\.){3}\d{1,3}')
    parsed_log_str(r'\d{2}/\w{3}/\d{4}(:\d{2}){3}\s\+\d{4}')
    parsed_log_str(r'GET|HEAD|POST|PUT|DELETE')
    parsed_log_str(r'/\w{6,9}/\w{7}_\d+')
    if re.search(r'\d{3}\s\d+', log_str) is not None:
        response_code_size = re.search(r'\d{3}\s\d+', log_str)
        response_code_size = response_code_size.group()
        code_size = re.split(r'\s', response_code_size)
        parsed_raw.extend(code_size)
    if len(parsed_raw) > 1:
        readeable_parsed_raw.append(tuple(parsed_raw))

print(readeable_parsed_raw)
