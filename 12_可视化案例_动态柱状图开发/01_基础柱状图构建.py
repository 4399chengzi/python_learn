"""
演示基础柱状图构建
"""

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(['中国', '美国', '英国'])

bar.add_yaxis('GDP', [1, 2, 3], label_opts=LabelOpts(position='right'))

bar.reversal_axis()
bar.render()
