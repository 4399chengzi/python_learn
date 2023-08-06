"""
演示字典的常用操作
"""

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['d'] = 4

print(my_dict)

my_dict['a'] = 5
print(my_dict)

my_dict.pop('a')
print(my_dict)

# my_dict.clear()
# print(my_dict)

print(my_dict.keys())

for key in my_dict.keys():
    print(my_dict[key])

for key in my_dict:
    print(my_dict[key])

print(len(my_dict))
