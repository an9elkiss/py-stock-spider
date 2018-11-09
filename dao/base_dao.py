import pymysql
from DBUtils.PooledDB import PooledDB
from const import const

import logging

pool_db = PooledDB(creator=pymysql,
                    mincached=3,
                    maxcached=20,
                    host=const.DB_HOST,
                    user=const.DB_USER,
                    password=const.DB_PASSWORD,
                    db=const.DB_NAME,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)

def save_stock_basic(data):
    conn = pool_db.connection()
    cursor = conn.cursor()

    for index, row in data.iterrows():
        # if index > 2:
        #     break

        row["status"] = 1
        row["create_by"] = "spy"
        row["update_by"] = "spy"


        cursor.execute(
            "INSERT INTO t_stock_basic(ts_code,symbol,name,area,industry,market,exchange_id,list_date,status,create_by,update_by) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
            (row["ts_code"], row["symbol"], row["name"], row["area"], row["industry"], row["market"], row["exchange"],row["list_date"], row["status"], row["create_by"], row["update_by"])
        )

    conn.commit()

def save_stock_company(data):
    data = data.fillna({'reg_capital': 0, 'employees': 0})
    data = data.fillna('无')

    conn = pool_db.connection()
    cursor = conn.cursor()

    for index, row in data.iterrows():
        # if index > 2:
        #     break

        row["status"] = 1
        row["create_by"] = "spy"
        row["update_by"] = "spy"

        cursor.execute(
            "INSERT INTO t_stock_company(ts_code,chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope,status,create_by,update_by) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
            (row["ts_code"], row["chairman"], row["manager"], row["secretary"], row["reg_capital"], row["setup_date"],
             row["province"], row["city"], row["introduction"],  row["website"],  row["email"],  row["office"],  row["employees"],  row["main_business"], row["business_scope"], row["status"], row["create_by"], row["update_by"])
        )
    conn.commit()

def save_daily(data):
    conn = pool_db.connection()
    cursor = conn.cursor()

    try:
        for index, row in data.iterrows():
            # if index > 2:
            #     break

            row["status"] = 1
            row["create_by"] = "spy"
            row["update_by"] = "spy"

            cursor.execute(
                "INSERT INTO t_daily(ts_code,trade_date,`open`,high,low,`close`,pre_close,`change`,pct_change,vol,amount,status,create_by,update_by) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                (row["ts_code"], row["trade_date"], row["open"], row["high"], row["low"], row["close"],
                 row["pre_close"], row["change"], row["pct_change"], row["vol"], row["amount"], row["status"], row["create_by"], row["update_by"])
            )

        conn.commit()

    except Exception:
        conn.rollback()
        logging.error("dao - save_daily 执行异常 SQL 已回滚！")
        raise
    finally:
        cursor.close()
        conn.close()

def save_dividend(data):
    conn = pool_db.connection()
    cursor = conn.cursor()

    try:
        for index, row in data.iterrows():

            row["status"] = 1
            row["create_by"] = "spy"
            row["update_by"] = "spy"

            cursor.execute(
                "INSERT INTO t_dividend(ts_code,end_date,`ann_date`,div_proc,stk_div,`cash_div_tax`,pay_date,`div_listdate`,status,create_by,update_by) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                (row["ts_code"],
                 row["end_date"], row["ann_date"], row["div_proc"], row["stk_div"], row["cash_div_tax"],
                 row["pay_date"], row["div_listdate"],
                 row["status"], row["create_by"], row["update_by"])
            )

        conn.commit()

    except Exception:
        conn.rollback()
        logging.error("dao - save_dividend 执行异常 SQL 已回滚！")
        raise
    finally:
        cursor.close()
        conn.close()

def save_fina_indicator(data):
    data = data.fillna(0)

    conn = pool_db.connection()
    cursor = conn.cursor()

    current_row = None

    try:
        for index, row in data.iterrows():
            current_row = row

            row["status"] = 1
            row["create_by"] = "spy"
            row["update_by"] = "spy"

            cursor.execute(
                "INSERT INTO t_fina_indicator(ts_code,end_date,eps,dt_eps,total_revenue_ps,revenue_ps,undist_profit_ps,extra_item," +
                "profit_dedt,gross_margin,inv_turn,ar_turn,ca_turn,fa_turn,assets_turn,op_income,valuechange_income,interst_income," +
                "daa,ebit,ebitda,fcff,fcfe,interestdebt,netdebt,tangible_asset,working_capital,networking_capital," +
                "invest_capital,retained_earnings,diluted2_eps,bps,cfps,ebit_ps,netprofit_margin,grossprofit_margin,cogs_of_sales,expense_of_sales," +
                "roe,roe_waa,roe_dt,roa,npta,roic,debt_to_assets,roa_dp,fixed_assets,profit_prefin_exp," +
                "non_op_profit,rd_exp,status,create_by,update_by)" +
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
                (row["ts_code"],
                 row["end_date"], row["eps"], row["dt_eps"], row["total_revenue_ps"], row["revenue_ps"],
                 row["undist_profit_ps"], row["extra_item"],
                 row["profit_dedt"], row["gross_margin"], row["inv_turn"], row["ar_turn"], row["ca_turn"], row["fa_turn"], row["assets_turn"], row["op_income"], row["valuechange_income"], row["interst_income"],
                 row["daa"], row["ebit"], row["ebitda"], row["fcff"], row["fcfe"], row["interestdebt"], row["netdebt"], row["tangible_asset"], row["working_capital"], row["networking_capital"],
                 row["invest_capital"], row["retained_earnings"], row["diluted2_eps"], row["bps"], row["cfps"], row["ebit_ps"], row["netprofit_margin"], row["grossprofit_margin"], row["cogs_of_sales"], row["expense_of_sales"],
                 row["roe"], row["roe_waa"], row["roe_dt"], row["roa"], row["npta"], row["roic"], row["debt_to_assets"], row["roa_dp"], row["fixed_assets"], row["profit_prefin_exp"],
                 row["non_op_profit"], row["rd_exp"], row["status"], row["create_by"], row["update_by"])
            )

        conn.commit()

    except Exception:
        logging.info("dao - save_fina_indicator 异常数据！%s", current_row)
        conn.rollback()
        logging.error("dao - save_fina_indicator 执行异常 SQL 已回滚！")
        raise
    finally:
        cursor.close()
        conn.close()

def is_fina_indicator_exist(ts_code):

    conn = pool_db.connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) n FROM t_fina_indicator WHERE ts_code = %s;", ts_code)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result['n'] > 0

def find_min_daily():

    conn = pool_db.connection()
    cursor = conn.cursor()

    cursor.execute("SELECT CONCAT(CAST(MIN(x.td) AS SIGNED),'') min_date FROM (SELECT d.trade_date+0 td FROM t_daily d GROUP BY d.trade_date) x;")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return str(result['min_date'])


# cursor.execute("SELECT * FROM t_time_entry ;")

# fetchall：获取所有的数据，默认以元祖的方式返回，如果你指定了cursorclass = pymysql.cursors.DictCursor，则以dict的方式返回
# result = cursor.fetchall()
# for row in result:
#     print(row)
# fetchone：获取剩余数据的第一条数据
# result = cursor.fetchone()
# print(result)
# #fetchmany:获取剩余数据的前2条数据
# result = cursor.fetchmany(2)
# print(result)

# cursor.close()
#
# conn.close()
