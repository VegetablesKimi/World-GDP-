import pandas as pd
import numpy as np
import random
import os
import sys
import re
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression
from pyecharts import options as opts
from pyecharts.charts import Bar3D, Tab, Pie, Line, Map, Timeline, Kline
from pyecharts.components import Table
from itertools import chain
from pyecharts.globals import ThemeType


gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\houseprice.csv"))
givegdp = ['Province Name']
giveyears = []
years = []
database = []
datasize = []

for x in range(2000,2020):
    givegdp.append(str(x))
    giveyears.append(str(x))
    
locgdp = gdp.loc[:,givegdp]
price = gdp.loc[:,giveyears]
country = locgdp.loc[:,['Province Name']]
for i in range(1,21):
    price0 = list(chain.from_iterable(price[i-1:i].values))
    datasize.append(price0)
    
country = list(chain.from_iterable(country.values))
country20 = country[0:10]

pdx = pd.Series(giveyears)
pdy1 = pd.Series(country20)
pdy20 = pd.Series(datasize[0])
pdy21 = pd.Series(datasize[1])
pdy22 = pd.Series(datasize[2])
pdy23 = pd.Series(datasize[3])
pdy24 = pd.Series(datasize[4])
pdy25 = pd.Series(datasize[5])
pdy26 = pd.Series(datasize[6])
pdy27 = pd.Series(datasize[7])
pdy28 = pd.Series(datasize[8])
pdy29 = pd.Series(datasize[9])
x_value = [int(value) for value in pdx.values]
y_value1 = [str(value) for value in pdy1.values]
y_value20 = [int(value) for value in pdy20.values]
y_value21 = [int(value) for value in pdy21.values]
y_value22 = [int(value) for value in pdy22.values]
y_value23 = [int(value) for value in pdy23.values]
y_value24 = [int(value) for value in pdy24.values]
y_value25 = [int(value) for value in pdy25.values]
y_value26 = [int(value) for value in pdy26.values]
y_value27 = [int(value) for value in pdy27.values]
y_value28 = [int(value) for value in pdy28.values]
y_value29 = [int(value) for value in pdy29.values]

# print(price)
# print(country)
print(country20[0])
print(type(y_value20))
print(x_value)
print(y_value1[0])
print(y_value20)
# for i in range(0, 10):
#     print(country20[i])
#     print(type(country20[i]))

# for i in range(0, 10):
#     print(price0[i])
#     print(type(price0[i]))