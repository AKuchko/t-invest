from tinkoff.invest import Client, InstrumentIdType, OrderDirection, OrderType
import time

from config import TOKEN, API_TARGET
from utils.account import sandbox_pay_in, get_balance, get_accounts
from utils.instruments import get_figi, get_instrument_lot
from utils.logger import logger
from utils.orders import sandbox_place_market_order

# === FIGI для выбранных акций ===
FIGI_LIST = {
    'SBER': 'BBG004730N88',  # Сбербанк
    'GAZP': 'BBG004730RP0',  # Газпром
    'LKOH': 'BBG004731032',  # Лукойл
    # 'GMKN': 'BBG00475K6G7',  # Норникель
    'YNDX': 'BBG006L8G4H1'  # Яндекс
}

with Client(TOKEN, target=API_TARGET) as client:
    # === Имитация скальпинга ===
    def scalping(figi_list, account_id):
        for ticker, figi in figi_list.items():
            logger.info(f"Скальпинг для {ticker} ({figi})")
            instrument_last_price = client.market_data.get_last_prices(figi=[figi])

            logger.info(f"Последняя цена акции: {instrument_last_price.last_prices[0].price}")

            figi_lot = get_instrument_lot(client=client, instrument_id=figi,
                                          id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI)
            logger.info(f"Лотность акции: {figi_lot}")

            # Покупаем один лот
            logger.info(f"Покупка {ticker}...")
            buy_order = sandbox_place_market_order(
                account_id=account_id,
                client=client,
                instrument_id=figi,
                direction=OrderDirection.ORDER_DIRECTION_BUY,
                quantity=1,
                price=(instrument_last_price.last_prices[0].price.units * figi_lot),
                order_type=OrderType.ORDER_TYPE_LIMIT
            )
            logger.info(f'Покупка акции: {ticker}, {buy_order}')
            time.sleep(1)  # Задержка в 1 сек для имитации реальной торговли

            # Продаём один лот
            logger.info(f"Продажа {ticker}...")
            sell_order = sandbox_place_market_order(
                client=client,
                instrument_id=figi,
                direction=OrderDirection.ORDER_DIRECTION_SELL,
                account_id=account_id,
                order_type=OrderType.ORDER_TYPE_MARKET,
                quantity=1
            )
            logger.info(f'Продажа акции: {ticker}, {sell_order}')

            time.sleep(1)


    # === Основной блок программы ===
    logger.info("--- Подключение к API Тинькофф в песочнице ---")
    accounts = get_accounts(client)
    account_id = accounts.accounts[0].id

    # Пополнение счёта
    logger.info("--- Пополнение счёта в песочнице ---")
    sandbox_pay_in(client, account_id=account_id, amount=10000)

    # Проверяем баланс после пополнения
    logger.info("--- Проверяем баланс после пополнения ---")
    account_balance = get_balance(client, account_id)
    logger.info(f"--- Текущий баланс:  {account_balance} ---")

    # Проверяем FIGI (необязательно, можно закомментировать)
    logger.info("--- Проверяем FIGI для выбранных акций ---")
    # get_figi()

    # Выполняем скальпинг по всем инструментам в списке
    logger.info("--- Начинаем скальпинг для выбранных акций ---")
    scalping(FIGI_LIST, account_id)

    # Проверяем баланс после торговли
    logger.info("--- Проверяем баланс после скальпинга ---")
    account_balance = get_balance(client, account_id)
    logger.info(f"\n--- Текущий баланс:  {account_balance} ---")

    logger.warning('--- END ---')
