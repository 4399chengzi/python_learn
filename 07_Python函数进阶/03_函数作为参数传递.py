"""
演示函数作为参数传递
"""


def test_A(compute):
    print(compute(1, 2))


def compute(x, y):
    return x + y


test_A(compute)
