from utils.logger import logger
from utils.market import get_candles
from utils.account import get_accounts

def calculate_obv(candles):
    logger.info(f'[calculate_obv] {candles}')
    obv = []
    prev_obv = 0

    for i in range(1, len(candles)):
        logger.info(f'[calculate_obv] iter {i}')
        logger.info(f'[calculate_obv] prev: {candles[i - 1]} curr: {candles[i]}')
        current_close = candles[i].close.units + candles[i].close.nano / 1e9
        prev_close = candles[i - 1].close.units + candles[i - 1].close.nano / 1e9
        logger.info(f'[calculate_obv] prev_close: {prev_close} curr_close: {current_close}')

        if current_close > prev_close:
            prev_obv += candles[i].volume
        elif current_close < prev_close:
            prev_obv -= candles[i].volume

        obv.append(prev_obv)

    logger.info(f'[calculate_obv] OBV: {obv}')
    return obv

def get_obv_analyze(obv, candles):
    """

    :param obv: Array of OBV values
    :param candles: Array of candles from client.market_data.get_candles().candles
    :return: number (-1 - sell signal | 0 - divergence signal | 1 - buy signal)
    """
    current_close = candles[-1].close.units + candles[-1].close.nano / 1e9
    prev_close = candles[-2].close.units + candles[-2].close.nano / 1e9
    current_obv = obv[-1]
    prev_obv = obv[-2]

    if current_close > prev_close and current_obv > prev_obv: return 1
    if current_close < prev_close and current_obv < prev_obv: return -1
    return 0

def start(client, figi_list):
    """

    :param client: Tinkoff Invest client (Sync)
    :param figi_list: companies FIGI
    :return: void
    """
    if not client or not figi_list or len(figi_list) == 0:
        logger.error('[VBS] missing required params on start method')
        return None

    accounts = get_accounts(client)
    account_id = accounts[0].id
    logger.info(f'[VBS] account id: {account_id}')

    for figi in figi_list:
        candles = get_candles(
            client=client,
            instrument_id=figi,
            days=30
        )

        if not candles or len(candles) == 0:
            logger.warning(f'[VBS] candles for FIGI {figi} is empty. Maybe FIGI value is wrong')
            continue

        logger.info(f'[VBS] candles: {candles}')
        obv_params = calculate_obv(candles)
        logger.info(f'[VBS] obv: {obv_params}')
        obv_result = get_obv_analyze(obv_params, candles)
        logger.info(f'[VBS] result for {figi}: {obv_result}')
