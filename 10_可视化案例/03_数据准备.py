"""
演示数据准备
"""
import json

f_us = open('./可视化案例数据/折线图数据/美国.txt', 'r', encoding='utf-8')
us_data = f_us.read()

us_data = us_data.replace('jsonp_1629344292311_69436(', '')

us_data = us_data[:-2]

us_dict = json.loads(us_data)
# print(us_dict, type(us_data))

trend_data = us_dict['data'][0]['trend']
# print(trend_data)

x_data = trend_data['updateDate'][:314]
print(x_data)

y_data = trend_data['list'][0]['data'][:314]
print(y_data)

