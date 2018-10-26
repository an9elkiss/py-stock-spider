import tushareapi.api as api
import datetime
import dao.base_dao as base_dao

def save_yesterday_daily():
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime("%Y%m%d")

    data = api.daily(yesterday)

    base_dao.save_daily(data)