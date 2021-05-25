import requests
import sys


def currency_rates(usr_money):
    usr_money = usr_money.upper()
    usr_money_index = usr_lst.index(usr_money)
    return f'Курс на: {usr_date}\n{usr_lst[usr_money_index + 1]} ' \
           f'{usr_lst[usr_money_index + 2]} = {usr_lst[usr_money_index + 3]}'


usr_lst = []

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = requests.get(url)
usr_str = response.text
index_date = usr_str.find('Date=')
usr_date = usr_str[index_date + 6: index_date + 16]
index_del_one = usr_str.find('<Valute ID')
usr_str = usr_str[index_del_one:]

usr_str = usr_str.replace('Valute ID=', '')
usr_str = usr_str.replace('Valute', '')
usr_str = usr_str.replace('NumCode', '')
usr_str = usr_str.replace('CharCode', '')
usr_str = usr_str.replace('Nominal', '')
usr_str = usr_str.replace('Name', '')
usr_str = usr_str.replace('Value', '')
usr_str = usr_str.replace('</>', '')
usr_str = usr_str.replace('<', ';')
usr_str = usr_str.replace('>', ';')

for i in range(len(usr_str)):
    index_del_two = usr_str.find('"')
    usr_str = usr_str.replace(usr_str[index_del_two: index_del_two + 7], '')

usr_lst = usr_str.split(';')

for date in usr_lst:
    if len(date) <= 2:
        usr_lst.remove(date)

try:
    print(*map(currency_rates, sys.argv[1:]), sep='\n')
except ValueError:
    print('У нас нет сведений по данной валюте.')