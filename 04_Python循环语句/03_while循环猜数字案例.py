"""
演示while循环猜数字案例
"""

# 1.构建一个随机的数字变量
import random

num = random.randint(1, 10)
a = int(input("猜："))
count = 0
while True:
    count += 1
    if a == num:
        print(1, count)
        break
    elif a > num:
        print('大')
    else:
        print('小')
    a = int(input("猜："))
