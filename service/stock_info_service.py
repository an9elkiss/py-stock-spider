from datetime import date

import tushareapi.api as api
import datetime
import dao.base_dao as base_dao
import logging
import time

# start_date = datetime.date(2018, 9, 30)

def save_yesterday_daily():
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y%m%d")
    logging.info("service - save_yesterday_daily %s ...", yesterday)

    data = api.daily(yesterday)

    base_dao.save_daily(data)

def save_history_daily():
    start_date = base_dao.find_min_daily()

    while(True):

        start_date = (datetime.datetime.strptime(start_date, '%Y%m%d') - datetime.timedelta(1)).strftime("%Y%m%d")
        logging.info("service - save_history_daily %s ...", start_date)

        data = api.daily(start_date)

        if data.size > 0:
            base_dao.save_daily(data)
            break

def save_dividend_all():
    logging.info("service - save_dividend_all ...")

    stocks = api.stock_base()
    for index, row in stocks.iterrows():
        data = api.dividend(row["ts_code"])
        base_dao.save_dividend(data)

    logging.info("service - save_dividend_all success.")

def save_fina_indicator_all():
    logging.info("service - save_fina_indicator_all ...")

    stocks = api.stock_base()
    for index, row in stocks.iterrows():
        if base_dao.is_fina_indicator_exist(row["ts_code"]):
            continue
        elif row["market"] == '主板':
            data = api.fina_indicator(row["ts_code"])
            base_dao.save_fina_indicator(data)

            time.sleep(3)

    logging.info("service - save_fina_indicator_all success.")

