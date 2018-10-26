import dao.base_dao as base_dao
import tushareapi.api as api
import service.stock_info_service as service

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

# TODO env (test/pro)

def main():

    logging.info("main方法开始执行...")

    # data = api.stock_base()
    # data = api.stock_company()
    # data = api.daily('20181023')

    # print(data.columns)
    # print(data)

    # base_dao.save_stock_basic(data)
    # base_dao.save_stock_company(data)
    # base_dao.save_daily(data)

    service.save_yesterday_daily()

    logging.info("main方法执行成功。")

main()


