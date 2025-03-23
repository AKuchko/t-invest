from tinkoff.invest import CandleInterval
from utils.logger import logger
from datetime import datetime, timedelta


def get_candles(client, figi=None, instrument_id=None, days=0, hours=0, minutes=0):
    """

    :param client: Tinkoff Invest client (sync)
    :param figi: FIGI-identifier of instrument
    :param instrument_id: FIGI or instrument_uid
    :param days: Period in days (can bbe combined with hours and minutes)
    :param hours: Period in hours (can bbe combined with days and minutes)
    :param minutes: Period in minutes (can bbe combined with hours and days)
    :return: HistoricCandle[]
    """
    try:
        interval = CandleInterval.CANDLE_INTERVAL_DAY if days > 0 else CandleInterval.CANDLE_INTERVAL_HOUR
        response = client.market_data.get_candles(
            figi=figi,
            instrument_id=instrument_id,
            from_=datetime.utcnow() - timedelta(days=days, hours=hours, minutes=minutes),
            to=datetime.utcnow(),
            interval=interval
        )
        return response.candles
    except Exception as e:
        logger.exception(f'[get_candles] Exception:\n{e}')
