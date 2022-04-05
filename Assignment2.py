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

data = pd.read_csv('data.csv')
data = data.astype(float)