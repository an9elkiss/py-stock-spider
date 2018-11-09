import tushare as ts

import logging

from const import const



pro = ts.pro_api(const.TUSHARE_TOKEN)


def stock_base():
    logging.info("api - tushare.stock_basic...")

    return pro.stock_basic(exchange_id='', list_status='L',
                           fields='ts_code,symbol,name,area,industry,market,exchange,list_date')


def stock_company():
    logging.info("api - tushare.stock_company...")

    return pro.stock_company()

def daily(date):
    logging.info("api - tushare.daily...")

    return pro.daily(trade_date=date)

def dividend(ts_code):
    logging.info("api - tushare.dividend...")

    return pro.dividend(ts_code=ts_code, fields='ts_code,end_date,ann_date,div_proc,stk_div,cash_div_tax,pay_date,div_listdate')

def fina_indicator(ts_code):
    logging.info("api - tushare.fina_indicator...")

    return pro.fina_indicator(ts_code=ts_code, fields='ts_code,end_date,eps,dt_eps,total_revenue_ps,revenue_ps,undist_profit_ps,extra_item,' +
                "profit_dedt,gross_margin,inv_turn,ar_turn,ca_turn,fa_turn,assets_turn,op_income,valuechange_income,interst_income," +
                "daa,ebit,ebitda,fcff,fcfe,interestdebt,netdebt,tangible_asset,working_capital,networking_capital," +
                "invest_capital,retained_earnings,diluted2_eps,bps,cfps,ebit_ps,netprofit_margin,grossprofit_margin,cogs_of_sales,expense_of_sales," +
                "roe,roe_waa,roe_dt,roa,npta,roic,debt_to_assets,roa_dp,fixed_assets,profit_prefin_exp," +
                'non_op_profit,rd_exp')




