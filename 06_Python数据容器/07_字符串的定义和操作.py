"""
演示字符串的定义和操作
只可以存放字符串，不可以修改，支持for
"""
my_str = 'itheima and itcast'

print(my_str[2])
print(my_str[-16])

# my_str[2] = 'H'

print(my_str.index('and'))

new_my_str = my_str.replace('it', 'chengxu')
print(new_my_str)

my_str_list = my_str.split(' ')
print(my_str_list)

# my_str = ' itheima and itcast '
# print(my_str.strip())
#
# my_str = '12itheima and itcast21'
# print(my_str.strip('21'))

print(my_str.count('it'))

print(len(my_str))
