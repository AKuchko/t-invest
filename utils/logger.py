import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
