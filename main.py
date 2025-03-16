from grpc.aio import ClientInterceptor
from tinkoff.invest import Client
import time

from config import TOKEN, API_TARGET
from utils.account import sandbox_pay_in, get_balance
from utils.operations import get_portfolio
from utils.instruments import get_figi
from utils.logger import logger

# === Вставь свой токен для песочницы ===
# TOKEN = 'ТВОЙ_API_КЛЮЧ'

# === FIGI для выбранных акций ===
FIGI_LIST = {
    'SBER': 'BBG004730N88',  # Сбербанк
    'GAZP': 'BBG004730RP0',  # Газпром
    'LKOH': 'BBG004731032',  # Лукойл
    'GMKN': 'BBG00475K6G7',  # Норникель
    'YNDX': 'BBG006L8G4H1'  # Яндекс
}


# === Пополнение баланса в песочнице ===
# def sandbox_pay_in(client, account_id, currency='RUB', balance=100000):
#     try:
#         request = tinvest.SandboxSetCurrencyBalanceRequest(
#             currency=currency,
#             balance=balance
#         )
#         client.set_sandbox_currencies_balance(request)
#         print(f"✅ Баланс песочницы пополнен на {balance} {currency}")
#     except Exception as e:
#         print(f"❌ Ошибка при пополнении баланса: {e}")

with Client(TOKEN, target=API_TARGET) as client:
    # === Проверка текущего портфеля ===
    # def get_balance():
    #     try:
    #         response = client.operations.get_portfolio()
    #         positions = response.positions
    #         if len(positions) == 0:
    #             print("Портфель пуст.")
    #         else:
    #             print("\nТекущий портфель:")
    #             for position in positions:
    #                 print(f"{position.name}: {position.balance} {position.currency}")
    #     except Exception as e:
    #         print(f"❌ Ошибка при получении баланса: {e}")


    # === Проверка FIGI для акций (опционально) ===
    # def get_figi():
    #     try:
    #         response = client.get_market_stocks()
    #         stocks = response.payload.instruments
    #         print("\nДоступные FIGI:")
    #         for stock in stocks:
    #             if stock.ticker in FIGI_LIST:
    #                 print(f"{stock.ticker}: {stock.figi}")
    #     except Exception as e:
    #         print(f"❌ Ошибка при получении FIGI: {e}")


    # === Выставление рыночного ордера ===
    def place_market_order(figi, quantity, direction):
        try:
            order = tinvest.MarketOrderRequest(
                lots=quantity,
                operation=direction
            )
            response = client.post_orders_market_order(figi=figi, market_order_request=order)
            print(f"✅ Ордер {'покупки' if direction == 'Buy' else 'продажи'} для {figi} выполнен: {response.payload}")
        except Exception as e:
            print(f"❌ Ошибка при выставлении ордера для {figi}: {e}")


    # === Имитация скальпинга ===
    def scalping(figi_list):
        for ticker, figi in figi_list.items():
            print(f"\n🚀 Скальпинг для {ticker} ({figi})")

            # Покупаем один лот
            print(f"Покупка {ticker}...")
            place_market_order(figi, 1, 'Buy')
            time.sleep(1)  # Задержка в 1 сек для имитации реальной торговли

            # Продаём один лот
            print(f"Продажа {ticker}...")
            place_market_order(figi, 1, 'Sell')
            time.sleep(1)


    # === Основной блок программы ===
    print("\n--- Подключение к API Тинькофф в песочнице ---")

    # Пополнение счёта
    print("\n--- Пополнение счёта в песочнице ---")
    sandbox_pay_in()

    # Проверяем баланс после пополнения
    print("\n--- Проверяем баланс после пополнения ---")
    get_balance()

    # Проверяем FIGI (необязательно, можно закомментировать)
    print("\n--- Проверяем FIGI для выбранных акций ---")
    get_figi()

    # Выполняем скальпинг по всем инструментам в списке
    print("\n--- Начинаем скальпинг для выбранных акций ---")
    scalping(FIGI_LIST)

    # Проверяем баланс после торговли
    print("\n--- Проверяем баланс после скальпинга ---")
    get_balance()
