"""
演示lambda匿名函数
"""


def test_A(compute):
    print(compute(1, 2))


test_A(lambda x, y: x + y)
