"""
演示
"""


def str_reverse(s):
    """
    字符串反转
    :param s:字符串
    :return: 反转
    """
    return s[::-1]


def sub_str(s, x, y):
    """
    切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse('zpc'))
    print(sub_str('zxcvbnm', 1, 2))
