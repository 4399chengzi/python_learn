"""
列表操作练习
"""

my_list: list[int] = [21, 25, 21, 23, 22, 20]

my_list.append(31)

my_list.extend([29, 33, 30])

num1 = my_list[0]
print(num1)

num2 = my_list[-1]
print(num2)

index = my_list.index(31)
print(my_list)
print(index)
