import os
from dotenv import load_dotenv
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX, INVEST_GRPC_API


load_dotenv()

TOKEN = os.getenv('TOKEN')
IS_DEV = os.getenv('ENV') == 'dev'
API_TARGET = INVEST_GRPC_API_SANDBOX if IS_DEV else INVEST_GRPC_API
