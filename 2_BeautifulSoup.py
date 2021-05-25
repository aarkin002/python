"""
Сначала не поверил, что нужно строку делить стандартными средствами, поэтому долго
рыл интернет, наткнулся BeautifulSoup и сделал с ним, выкидывать жалко, время потратил все же,
поэтому решил вложить, фактическое решение задачи в файле 2_currency_rates.py
"""

import requests
from bs4 import BeautifulSoup


def currency_rates(usr_money):
    usr_money = usr_money.upper()
    usr_money_index = filter_lst.index(usr_money)
    return f'{filter_lst[usr_money_index + 1]} {filter_lst[usr_money_index + 2]} = {filter_lst[usr_money_index + 3]}'


filter_lst = []

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
usr_lst = soup.findAll(['charcode', 'nominal', 'name', 'value'])

for data in usr_lst:
    filter_lst.append(data.text)

try:
    print(currency_rates(input('Введите валюту(например без кавычек "USD"): ')))
except ValueError:
    print('У нас нет сведений по данной валюте.')
