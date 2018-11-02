import logging
import time
import job.data_input_jobs as jobs
from const import const


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename=const.LOG_FILE_PATH)

jobs.save_yesterday_daily()
# jobs.save_history_daily()

while True:
    logging.info("job - data_input_jobs running...")
    time.sleep(3600)