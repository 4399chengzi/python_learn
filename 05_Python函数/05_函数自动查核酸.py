"""
函数自动查核酸
"""


def check(num):
    print('欢迎，查体温')
    print(num, end=' ')
    if num <= 37.5:
        print(f"请进")
    else:
        print(f"隔离")


check(39)
