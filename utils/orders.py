from decimal import Decimal
from tinkoff.invest.utils import decimal_to_quotation
from utils.logger import logger
from uuid import uuid4


def sandbox_place_market_order(account_id, direction, instrument_id, client, order_type, quantity, price=None,
                               order_id=None, retry=False):
    _order_id = str(uuid4()) if not order_id else order_id
    try:
        money = None if not price else decimal_to_quotation(Decimal(price))
        logger.info(f'Создание заказа {_order_id}')
        logger.info(f'PRICE: {money}')
        logger.info(f'order_type: {order_type}')
        logger.info(f'instrument_id: {instrument_id}')
        return client.sandbox.post_sandbox_order(
            account_id=account_id,
            direction=direction,
            instrument_id=instrument_id,
            order_id=_order_id,
            order_type=order_type,
            price=money,
            quantity=quantity
        )
    except Exception as e:
        logger.exception(f'Произошла ошибка при выставлении заказа: %s', e, e.args)
        if retry:
            logger.info(f'Повторное высавление заказа: %s', order_id)
            sandbox_place_market_order(
                client=client,
                direction=direction,
                order_id=_order_id,
                order_type=order_type,
                instrument_id=instrument_id,
                quantity=quantity,
                price=price,
                account_id=account_id,
                retry=retry
            )
