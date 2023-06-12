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


def line_base() -> Line:
    gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\houseprice.csv",header=0))
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

    
    
    c = (
        Line(init_opts=opts.InitOpts(width="1525px", height="725px", theme=ThemeType.DARK))
        .add_xaxis(giveyears)
        .add_yaxis(country20[0], datasize[0], symbol_size=10)
        .add_yaxis(country20[1], datasize[1], symbol_size=10)
        .add_yaxis(country20[2], datasize[2], symbol_size=10)
        .add_yaxis(country20[3], datasize[3], symbol_size=10)
        .add_yaxis(country20[4], datasize[4], symbol_size=10)
        .add_yaxis(country20[5], datasize[5], symbol_size=10)
        .add_yaxis(country20[6], datasize[6], symbol_size=10)
        .add_yaxis(country20[7], datasize[7], symbol_size=10)
        .add_yaxis(country20[8], datasize[8], symbol_size=10)
        .add_yaxis(country20[9], datasize[9], symbol_size=10)
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False)
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="1978 - 2018年GDP前10国折线统计图",
                        title_textstyle_opts=opts.TextStyleOpts(color="white")))
    )
    return c

line_base().render("1978 - 2018年GDP前10国折线统计图.html")