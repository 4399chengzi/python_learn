"""
函数说明文档
"""


def add(x, y):
    """
    add函数可以接受2个参数，进行2数相加的功能
    :param x:其中一个数字
    :param y:另一个数字
    :return:相加的结果
    """
    r = x + y
    print(f"{x + y}")
    return r


add(1, 2)
