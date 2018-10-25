import tushare as ts

import logging



pro = ts.pro_api('640fd047dc9ca8079402b9d51902f27a545e1c82fd7629ac78ddda36')


def stock_base():
    logging.info("api - tushare.stock_basic...")

    return pro.stock_basic(exchange_id='', list_status='L',
                           fields='symbol,name,area,industry,market,exchange_id,list_date')


