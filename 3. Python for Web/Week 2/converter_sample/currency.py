import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', params = {'date_req':date})  # Использовать переданный requests
    currency_rates = BeautifulSoup(response.text, 'lxml')
    cur = {}
    for val in [cur_from, cur_to]:
        if val == 'RUR':
            cur[val] = {'nominal': Decimal(1), 'value': Decimal(1)}
        else:
            node = currency_rates.find(string=val).parent.parent
            cur[val] = {'nominal': Decimal(node.nominal.text), 'value': Decimal(node.value.text.replace(',', '.'))}
    
    result = (Decimal(amount) * cur[cur_from]['value'] / cur[cur_from]['nominal']) / cur[cur_to]['value'] * cur[cur_to]['nominal']

    return result.quantize(Decimal('0.0001'))

   
def main():
    print(convert(155, 'EUR', 'JPY', '14/11/2018', requests))   

if __name__ == '__main__':
    main()