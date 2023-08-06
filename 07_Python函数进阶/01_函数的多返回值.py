"""
演示函数的多返回值
"""


def test_return():
    return 1, 2


x, y = test_return()
print(x, y)
