from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get()  # Использовать переданный requests
    # ...
    result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой







def main():
    import requests
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002')
    cur = BeautifulSoup(response.text, 'lxml')
    val = cur.find_all('valute')
    for i in val:
        print(i)

if __name__ == '__main__':
    main()