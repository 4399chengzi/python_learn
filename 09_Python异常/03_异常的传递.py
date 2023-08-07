"""
演示异常的传递
"""


def f1():
    print('f1 b')
    num = 1 / 0
    print('f1 o')


def f2():
    print('f2 b')
    f1()
    print('f2 o')


def main():
    try:
        f2()
    except Exception as e:
        print('bug', e)


main()
