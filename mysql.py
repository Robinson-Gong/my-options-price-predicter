import pandas as pd
import tushare as ts
from sqlalchemy import create_engine

engine_ts = create_engine('mysql://user:mima@127.0.0.1:3306/demos?charset=utf8&use_unicode=1')

def read_data():
    sql = """SELECT * FROM stock_basic LIMIT 20"""
    df = pd.read_sql_query(sql, engine_ts)
    return df


def write_data(df):
    res = df.to_sql('stock_basic', engine_ts, index=False, if_exists='append', chunksize=5000)
    print(res)


def get_data():
    ts.set_token('f080e8e80b7d59a508fd93f99e230ab69fabb4727541331ed86ac9e3')
    pro = ts.pro_api()
    df = pro.stock_basic()
    return df


if __name__ == '__main__':
#     df = read_data()
    df = get_data()
    write_data(df)
    print(df)
