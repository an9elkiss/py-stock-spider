from datetime import date

import tushareapi.api as api
import datetime
import dao.base_dao as base_dao
import logging

start_date = datetime.date(2018, 9, 30)

def save_yesterday_daily():
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y%m%d")
    logging.info("service - save_yesterday_daily %s ...", yesterday)

    data = api.daily(yesterday)

    base_dao.save_daily(data)

# 线程不安全，使用了全局变量 start_date
def save_history_daily():
    global start_date

    logging.info("service - save_history_daily %s ...", start_date)

    # base_dao.save_daily(start_date_for_history_daily)

    start_date = start_date - datetime.timedelta(1)

