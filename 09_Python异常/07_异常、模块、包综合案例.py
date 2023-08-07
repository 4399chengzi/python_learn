"""
演示异常、模块、包综合案例
"""

# import my_utils.str_util
from my_utils import fill_util

# print(my_utils.str_util.str_reverse('zpc'))
# print(my_utils.str_util.sub_str('zpc', 0, 3))

fill_util.append_to_file('1.txt', '123')
fill_util.print_file_info('1.txt')
