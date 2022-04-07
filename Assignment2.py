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
import statsmodels.api as sm
sns.set()
# mpl.rcParams['font.sans-serif'] = 'WenQuanYi Micro Hei' #中文字体
# pro = ts.pro_api('4b82579de828df5013ba4f165ad9bf6fc831853e6315e111bb6ebaea')

os.chdir(r'D:\Coding\Assignment2')

# import data
sz50 = pd.read_csv('sz50.csv', index_col='trddy')
factor_raw = pd.read_csv('fivefactor_daily.csv',index_col='trddy')
sz50.index = pd.to_datetime(sz50.index)
factor_raw.index = pd.to_datetime(factor_raw.index)
factor_raw = factor_raw.dropna(axis=1)
factor_raw = factor_raw.dropna(axis=0)
sz50 = sz50.dropna(axis=1)
sz50 = sz50.dropna(axis=0)

# stock list 股票池
stock_codes = list(sz50.columns)


# 3-factors
factors = pd.DataFrame()
factors = factor_raw.loc['2021-03-01':'2022-03-01',['mkt_rf','smb','hml','rf']]


# calculate daily return
daily_return = pd.DataFrame()
# daily_return['trddy'] = sz50['trddy']
dreturn = pd.DataFrame()
for stock in stock_codes:
    dreturn[stock] = ((sz50[stock]-sz50[stock].shift(1))/sz50[stock])[:] # return or logreturn?
    daily_return[stock] = dreturn[stock]-0.000041 # excess of not?

# all data set
data_all = pd.DataFrame()
data_all = pd.merge(factors, daily_return, on='trddy',how='inner')

# OLS
def OLS(data_all):
    results = pd.DataFrame()
    stocks_return = data_all.iloc[:,4:]
    for i in range(len(stocks_return.columns)):
        x = data_all.iloc[:,0:3]
        y = stocks_return.iloc[:,i]
        X = sm.add_constant(x)
        model = sm.OLS(y,X)
        result = model.fit()
        results[i] = result.params
    results.columns = stocks_return.columns
    results.rename(index={"const":"Alpha"},inplace=True)
    z = results.sort_values(by="Alpha",axis=1,ascending=False)
    stocks_lists = z.columns.values.tolist()
    top_stocks = stocks_lists[:10]
    print(top_stocks)
    return top_stocks

OLS(data_all)