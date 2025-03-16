from tinkoff.invest import InstrumentStatus
from utils.logger import logger


def get_figi(client, needed_figi):
    try:
        stocks = client.instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)
        return filter(lambda stock: stock in needed_figi, stocks.instruments) if needed_figi else stocks.instruments
    except Exception as e:
        logger.exception(f"❌ Ошибка при получении FIGI: {e}")
        return []


def get_instrument_lot(client, instrument_id, id_type):
    try:
        response = client.instruments.get_instrument_by(id_type=id_type, id=instrument_id)
        return response.instrument.lot
    except Exception as e:
        logger.exception(f'Произошла ошибка при получении лотности: {e}')
        return None
