from tinkoff.invest import Client

from config import TOKEN, API_TARGET
from strategies.volumeBased import start


FIGI_LIST = {
    'SBER': 'BBG004730N88',  # Сбербанк
    'GAZP': 'BBG004730RP0',  # Газпром
    'LKOH': 'BBG004731032',  # Лукойл
    # 'GMKN': 'BBG00475K6G7',  # Норникель
    'YNDX': 'BBG006L8G4H1'  # Яндекс
}

figi_list = [
    'BBG004730N88',
    'BBG004730RP0',
    'BBG004731032',
    'BBG006L8G4H1',
]

with Client(TOKEN, target=API_TARGET) as client:
    start(client, figi_list)
