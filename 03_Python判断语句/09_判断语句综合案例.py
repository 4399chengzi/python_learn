"""
演示判断语句的实战案例，终极猜数字
"""

# 1.构建一个随机的数字变量
import random
num = random.randint(1,10)
a = int(input("猜："))

if a == num:
    print(1)
else:
    if a > num :
        print('大')
    else:
        print('小')
    a = int(input("猜："))
    if a == num:
        print(1)
    else:
        if a > num:
            print('大')
        else:
            print('小')
        a = int(input("猜："))
        if a == num:
            print(1)
        else:
            print(0)