"""
演示集合的定义和操作
无序，不重复，不支持下表，可修改
"""

my_set = {'a', 'a', 'b', 'b', 'c', 'c'}
my_set_empty = {}
print(my_set, type(my_set))
print(my_set_empty, type(my_set_empty))

my_set.add('d')
print(my_set)

my_set.remove('d')
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

set1 = {1, 2, 3}
set2 = {1, 4, 5}

print(set1.difference(set2))
# set1.difference_update(set2)
# print(set1)

print(set1.union(set2))

print(len(set1))

for elm in set1:
    print(elm)
