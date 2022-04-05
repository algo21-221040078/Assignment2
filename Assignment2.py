# -*- coding: utf-8 -*-
''''
Name: DIAO Xingning
Student ID: 221040078
Assignment2
Fama-French 3 factors model
'''

import pandas as pd
import numpy as np
# import tushare as ts
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import os
sns.set()
# mpl.rcParams['font.sans-serif'] = 'WenQuanYi Micro Hei' #中文字体
# pro = ts.pro_api('4b82579de828df5013ba4f165ad9bf6fc831853e6315e111bb6ebaea')

os.chdir(r'D:\Coding\Assignment2')

# import data
sz50 = pd.read_csv('sz50.csv')
data = sz50.astype(float)
factor = pd.read_csv('fivefactor_daily.csv')

# stock list 股票池
def SZ50_stocks(data):
    #获取上证50成分股
    stock_sz50 = data.drop_duplicates('stkcd')
    stock_sz50['stkcd'] = stock_sz50['stkcd'].apply(lambda x:str(float(x))[:-2])
    stock_sz50 = stock_sz50['stkcd']
    stock_codes = pd.DataFrame(columns=stock_sz50)
    return stock_codes

# 整合数据
df = pd.DataFrame()




def OLS(data):
    results = pd.DataFrame()
    stocks_return = df_final.iloc[:,3:50]
    for i in range(len(stocks_return.columns)):
        x = df_final.iloc[:,0:3]
        y = stocks_return.iloc[:,i]
        X = sm.add_constant(x)
        model = sm.OLS(y,X)
        result = model.fit()
        results[i] = result.params
    results.columns = stocks_return.columns
    results.rename(index={"const":"Alpha"},inplace=True)
    z =results.sort_values(by="Alpha",axis=1,ascending=False)
    stocks_lists = z.columns.values.tolist()
    top_stocks = stocks_lists[:10]
    print(top_stocks)
    return top_stocks