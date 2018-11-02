import logging
import os
from const import const

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename=const.LOG_FILE_PATH)

logging.info("service - save_yesterday_daily %s ...", "20180806")

ENV_PROFILE = os.getenv("ENV")

logging.info(ENV_PROFILE)

logging.info(const.LOG_FILE_PATH)



