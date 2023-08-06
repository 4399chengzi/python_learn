"""
演示字典的定义
key不重复
"""

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {}
my_dict3 = dict()
print(my_dict, type(my_dict))
print(my_dict2, type(my_dict2))
print(my_dict3, type(my_dict3))

my_dict4 = {'a': 1, 'a': 2, 'c': 3}
print(my_dict4, type(my_dict4))

print(my_dict['a'])

stu_dict = {
    'a': {
        'a': 1,
        'b': 2,
        'c': 3
    }, 'b': {
        'a': 1,
        'b': 2,
        'c': 3
    }, 'c': {
        'a': 1,
        'b': 2,
        'c': 3
    }
}
print(stu_dict, type(stu_dict))

print(stu_dict['a']['a'])
