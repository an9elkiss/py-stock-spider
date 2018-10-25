import tushare as ts

import logging

from const import const



pro = ts.pro_api(const.TUSHARE_TOKEN)


def stock_base():
    logging.info("api - tushare.stock_basic...")

    return pro.stock_basic(exchange_id='', list_status='L',
                           fields='symbol,name,area,industry,market,exchange_id,list_date')


