"""
演示分割字符串
"""
my_str = 'itheima itcast boxuegu'

print(my_str.count('it'))

print(my_str.replace(' ', '|'))

print(my_str.replace(' ', '|').split('|'))
