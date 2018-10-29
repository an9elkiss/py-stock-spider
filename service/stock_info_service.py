import tushareapi.api as api
import datetime
import dao.base_dao as base_dao
import logging


def save_yesterday_daily():
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y%m%d")
    logging.info("service - save_yesterday_daily %s ...", yesterday)

    data = api.daily(yesterday)

    base_dao.save_daily(data)