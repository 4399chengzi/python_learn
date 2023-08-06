"""
演示信息去重
"""

my_list = ['a', 'v', 'a', 'c', 'b']

my_set = set()

for elm in my_list:
    my_set.add(elm)

print(my_set)
