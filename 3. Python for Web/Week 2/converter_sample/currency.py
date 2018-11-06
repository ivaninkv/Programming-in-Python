from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get()  # Использовать переданный requests
    # ...
    result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой
