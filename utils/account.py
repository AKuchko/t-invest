from decimal import Decimal
from tinkoff.invest import MoneyValue
from tinkoff.invest.utils import quotation_to_decimal, decimal_to_quotation
from utils.logger import logger


def sandbox_create_account(client):
    return client.sandbox.open_sandbox_account()

def sandbox_close_account(client, account_id):
    return client.sandbox.close_sandbox_account(account_id=account_id)

def sandbox_pay_in(client, account_id, amount, currency="rub"):
    try:
        money = decimal_to_quotation(Decimal(amount))
        return client.sandbox.sandbox_pay_in(
            account_id=account_id,
            amount=MoneyValue(units=money.units, nano=money.nano, currency=currency)
        )
    except Exception as e:
        logger.exception(f"❌ Ошибка при пополнении баланса: {e}")

def get_accounts(client):
    response = client.users.get_accounts()
    return response.accounts

def get_balance(client, account_id):
    positions = client.operations.get_positions(account_id=account_id)
    return quotation_to_decimal(positions.money[0]) if len(positions.money) > 0 else 0
