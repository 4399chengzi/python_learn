"""
演示元组tuple的定义和操作
和字符串的区别：不可以修改，除了内部列表
"""

t1 = (1, 'h', True)

t2 = ()

t3 = tuple()

print(type(t1), t1)
print(type(t2), t2)
print(type(t3), t3)

# t4 = ('h')
# print(type(t4), t4)

t4 = ('h',)
print(type(t4), t4)

t5 = ((1, 2, 3), (4, 5, 6))
print(type(t5), t5)

print(t5[1][1])

t6 = ('a', 'b', 'c')
print(t6.index('a'))

print(t6.count('a'))

print(len(t6))

index = 0
while index < len(t6):
    print(t6[index])
    index += 1

for element in t6:
    print(element)

# t6[0] = 'd'

t7 = (1, 2, [1, 2])
t7[2][1] = 1
print(t7)
