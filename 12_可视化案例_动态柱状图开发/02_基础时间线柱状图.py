"""
演示基础时间线柱状图
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType


def bar_instruct(data_list):
    bar = Bar()

    bar.add_xaxis(['中国', '美国', '英国'])

    bar.add_yaxis('GDP', data_list, label_opts=LabelOpts(position='right'))

    bar.reversal_axis()

    return bar


bar1 = bar_instruct([1, 2, 3])
bar2 = bar_instruct([4, 5, 6])
bar3 = bar_instruct([7, 8, 9])

timeline = Timeline({'theme': ThemeType.DARK})

timeline.add(bar1, '1')
timeline.add(bar2, '2')
timeline.add(bar3, '3')

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

timeline.render('基础时间线柱状图.html')
