import dao.base_dao as base_dao
import tushareapi.api as api
import service.stock_info_service as service
from const import const
import logging
import datetime

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename=const.LOG_FILE_PATH)


def main():

    logging.info("main方法开始执行...")

    # data = api.stock_base()
    # data = api.stock_company()
    # data = api.daily('20181023')
    # data = api.dividend('000001.SZ')
    # data = api.fina_indicator('000002.SZ')

    # print(data.columns)
    # print(data)

    # base_dao.save_stock_basic(data)
    # base_dao.save_stock_company(data)
    # base_dao.save_daily(data)
    # base_dao.save_dividend(data)
    # base_dao.save_fina_indicator(data)
    # print(base_dao.is_fina_indicator_exist('000002.SZ'))
    # print(base_dao.find_min_daily())

    # service.save_yesterday_daily()
    # service.save_dividend_all()
    service.save_fina_indicator_all()

    logging.info("main方法执行成功。")

main()


