"""
函数的嵌套调用
"""


def f_b():
    print(2)


def f_a():
    print(1)

    f_b()

    print(3)


f_a()
