"""
函数的返回值None
"""


def say_hi():
    print('你好呀')


r = say_hi()


def say_hi2():
    print('你好呀')
    return None


r2 = say_hi2()
print(r2)
print(type(r2))

if not r2:
    print('未成年')

name = None
