import pymysql

from const import const


conn = pymysql.connect(
    host=const.DB_HOST,
    user=const.DB_USER,
    password=const.DB_PASSWORD,
    database=const.DB_NAME,
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()


def save_stock_basic(data):

    for index, row in data.iterrows():
        # if index > 2:
        #     break

        row["status"] = 1
        row["create_by"] = "spy"
        row["update_by"] = "spy"

        cursor.execute(
            "INSERT INTO t_stock_basic(symbol,name,area,industry,market,exchange_id,list_date,status,create_by,update_by) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
            (row["symbol"], row["name"], row["area"], row["industry"], row["market"], row["exchange_id"],row["list_date"], row["status"], row["create_by"], row["update_by"])
        )

    conn.commit()



    # try:
    #     # 执行一条insert语句，返回受影响的行数 #
    #     cursor.execute(
    #         "INSERT INTO t_time_entry(date,type_id,comment,duration,status,create_by,update_by) VALUES('2018-10-18',3,'aaa',21,1,'sys','sys');")
    #     # 执行多次insert并返回受影响的行数 cursor.executemany("INSERT INTO para5(name,age) VALUES(%s,%s);", [('次牛444', '12'), ("次牛2", '11'), ('次牛3', '10')])
    #     #  提交执行
    #     conn.commit()
    # except Exception as e:
    #     # 如果执行sql语句出现问题，则执行回滚操作
    #     conn.rollback()
    #     print(e)
    # finally:
    #     # 不论try中的代码是否抛出异常，这里都会执行 # 关闭游标和数据库连接
    #     cursor.close()
    #     conn.close()

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
