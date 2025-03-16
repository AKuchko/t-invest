from utils.logger import logger


def get_portfolio(client, account_id):
    try:
        return client.opertaions.get_portfolio(account_id=account_id)
    except Exception as e:
        logger.exception(f"❌ Ошибка при получении баланса: {e}")
