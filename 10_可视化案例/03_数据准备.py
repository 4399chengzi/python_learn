"""
演示数据准备,生成折线图
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts


def DataPrepare(filename, begin_data):
    f = open(filename, 'r', encoding='utf-8')
    data = f.read()

    data = data.replace(begin_data, '')

    data = data[:-2]

    _dict = json.loads(data)
    # print(dict, type(data))

    trend_data = _dict['data'][0]['trend']
    # print(trend_data)

    x_data = trend_data['updateDate'][:314]
    # print(x_data)

    y_data = trend_data['list'][0]['data'][:314]
    # print(y_data)

    f.close()

    return x_data, y_data


us_x_data, us_y_data = DataPrepare('./可视化案例数据/折线图数据/美国.txt', 'jsonp_1629344292311_69436(')
jp_x_data, jp_y_data = DataPrepare('./可视化案例数据/折线图数据/日本.txt', 'jsonp_1629350871167_29498(')
in_x_data, in_y_data = DataPrepare('./可视化案例数据/折线图数据/印度.txt', 'jsonp_1629350745930_63180(')

line = Line()

line.add_xaxis(us_x_data)

line.add_yaxis('美国确诊人数', us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('日本确诊人数', jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数', in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title='2023年美国、日本、印度确诊人数对比折线图', pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

line.render()
