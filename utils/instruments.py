from tinkoff.invest import InstrumentStatus
from utils.logger import logger


def get_figi(client, needed_figi):
    try:
        stocks = client.instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)
        return filter(lambda stock: stock in needed_figi, stocks.instruments) if needed_figi else stocks.instruments
    except Exception as e:
        logger.exception(f"❌ Ошибка при получении FIGI: {e}")
