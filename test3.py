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

gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\World-GDP-1978-2018-main\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_422027.csv",header=3))
givegdp = ['Country Name']
giveyears = []
years = []
database = []
datasize = []

for x in range(1978,2019):
    givegdp.append(str(x))
    giveyears.append(str(x))
    
locgdp = gdp.loc[:,givegdp]
price = gdp.loc[:,giveyears]
country = locgdp.loc[:,['Country Name']]
for i in range(1,21):
    price0 = list(chain.from_iterable(price[i-1:i].values//100000000))
    datasize.append(price0)
    
country = list(chain.from_iterable(country.values))
country20 = country[0:10]

print(country20[0])
print(datasize[0])