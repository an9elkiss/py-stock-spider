import logging
import time
import job.data_input_jobs as jobs


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename='/usr/python/logs/py-stock-spider/py-stock-spider.log')

jobs.save_yesterday_daily()

while True:
    logging.info("job - data_input_jobs running...")
    time.sleep(600)