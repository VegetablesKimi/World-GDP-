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



# def timeline_map() -> Timeline:
#     tl = Timeline(init_opts=opts.InitOpts(width="1525px", height="725px"))
#     tl.add_schema(
#         play_interval=1000,
#         pos_left="200",
#         pos_bottom="20",
#         label_opts=opts.LabelOpts(is_show=True, color="black"),
#     )
    
#     gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\World-GDP-1978-2018-main\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_422027.csv",header=3))
#     givegdp = ['Country Name']

#     for x in range(1978,2019):
#         givegdp.append(str(x))
    
#     locgdp = gdp.loc[:,givegdp]
#     country = locgdp.loc[:,['Country Name']]
#     country = list(chain.from_iterable(country.values))
    
#     for y in range(1978, 2019):
#         money = locgdp.loc[:,[str(y)]]
#         values = list(chain.from_iterable(money.values//100000000))
#         map0 = (
#             Map()
#             .add(
#                 "GDP", [list(z) for z in zip(country, values)], "world", zoom=1.5
#             )
#             .set_series_opts(label_opts=opts.LabelOpts(is_show=True,
#                                                       font_size=10))
                            
#             .set_global_opts(
#                 legend_opts=opts.LegendOpts(
#                 orient="vertical", pos_top="15%", pos_left="2%", is_show=False),
#                 title_opts=opts.TitleOpts(title="{}年世界各国经济总量（GDP）".format(y),
#                 title_textstyle_opts=opts.TextStyleOpts(font_size=25, color="black")),
                
#                 visualmap_opts=opts.VisualMapOpts(
#                     is_calculable=True,
#                     dimension=0,
#                     pos_left="100",
#                     pos_top="500",
#                     range_text=["单位亿美元", ""],
#                     range_color=["lightskyblue", "yellow", "orangered"],
#                     textstyle_opts=opts.TextStyleOpts(color="black"),
#                     max_=150000, min_=1)
#             )
#         )
#         tl.add(map0, "{}年".format(y))
#     return tl







def line_base() -> Line:
    gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\World-GDP-1978-2018-main\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_422027.csv",header=3))
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
        .add_yaxis(country20[0], datasize[0])
        .add_yaxis(country20[1], datasize[1])
        .add_yaxis(country20[2], datasize[2])
        .add_yaxis(country20[3], datasize[3])
        .add_yaxis(country20[4], datasize[4])
        .add_yaxis(country20[5], datasize[5])
        .add_yaxis(country20[6], datasize[6])
        .add_yaxis(country20[7], datasize[7])
        .add_yaxis(country20[8], datasize[8])
        .add_yaxis(country20[9], datasize[9])
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False)
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="1978 - 2018年GDP前10国折线统计图",
                        title_textstyle_opts=opts.TextStyleOpts(color="white")))
    )
    return c




# def line_back():
#     gdp = pd.DataFrame(pd.read_csv("C:\\Users\\noodl\\Desktop\\code\\python\\World-GDP-1978-2018-main\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_422027.csv",header=3))
#     givegdp = ['Country Name']
#     years = []
#     database = []

#     for x in range(1998,2019):
#         givegdp.append(str(x))
#         years.append(str(x))
    
#     locgdp = gdp.loc[:,years]
#     USAdata = locgdp[0:1]
#     CHINAdata = locgdp[1:2]

#     CHINA_train = CHINAdata[:10]
#     USA_train = USAdata[:10]
#     CHINA_test = CHINAdata[-10:]
#     USA_test = USAdata[-10:]

#     model = LinearRegression()
#     CHINA_train_x = np.array(CHINA_train.values).reshape(-1,1)
#     USA_train_y = np.array(USA_train.values).reshape(-1,1)
#     model.fit(CHINA_train_x,USA_train_y)

#     CHINA_test_x = np.array(CHINA_test.values).reshape(-1,1)

#     x = np.array(CHINAdata.values).reshape(-1,1)
#     y = np.array(USAdata.values).reshape(-1,1)
#     plt.plot(x,y,'r.')
#     plt.plot(x,model.predict(x),'b-')

    
    
# tab = Tab()
# tab.add(timeline_map(), "Map")
# tab.add(bar3d_base(), "Bar-World")
# tab.add(line_base(), "Line")
# tab.add(bar3d_base0(), "Bar-20th")
# tab.add(timeline_pie(), "Pie-World")
# tab.add(timeline_pie0(), "Pie-20th")
# tab.add(kline_datazoom_slider(), "China VS USA")
# tab.render()

line_base().render("line.html")

# line_back()


# below is test for function
# line_base().render()