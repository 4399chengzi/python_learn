"""
演示GDP动态柱状图
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

f = open('./动态柱状图数据/1960-2019全球GDP数据.csv', 'r', encoding='GB2312')

data_lines = f.readlines()

f.close()

data_lines.pop(0)

data_dict = {}

for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    gdp = float(line.split(',')[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# print(data_dict)

sorted_year_list = sorted(data_dict.keys())

timeline = Timeline({'theme': ThemeType.LIGHT})

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # x_data.reverse()
    # y_data.reverse()

    bar = Bar()
    bar.add_xaxis(x_data[::-1])

    bar.add_yaxis('GDP(亿)', y_data[::-1], label_opts=LabelOpts(position='right'))

    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title=f'{year}年全球前8GDP数据')
    )

    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

timeline.render('GDP动态柱状图.html')
