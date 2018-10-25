import dao.base_dao as base_dao
import tushareapi.api as api

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

# TODO env (test/pro)

def main():

    logging.info("main方法开始执行...")

    data = api.stock_base()

    print(data.columns)

    # base_dao.save_stock_basic(data)

    logging.info("main方法执行成功。")

main()


