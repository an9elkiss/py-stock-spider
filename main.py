import dao.base_dao as base_dao
import tushareapi.api as api

import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

# TODO git
# TODO constant

def main():

    logging.info("main方法开始执行...")

    data = api.stock_base()

    print(data.columns)

    # for index, row in data.iterrows():
    #     if index > 10:
    #         break
    #
    #
    #
    #     print(row["symbol"], row["name"], row["area"], row["industry"], row["market"], row["exchange_id"],
    #           row["list_date"], row["status"], row["create_time"], row["update_time"])

    logging.info("main方法执行成功。")

main()
