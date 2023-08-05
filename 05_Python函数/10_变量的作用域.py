"""
变量的作用域
"""

# def f_a():
#     num = 100
#     print(num)
#
#
# f_a()
# print(num)

num = 200


# def f_a():
#     print(num)
#
#
# def f_b():
#     print(num)
#
#
# f_a()
# f_b()
# print(num)

# def f_a():
#     print(num)
#
#
# def f_b():
#     num = 500
#     print(num)
#
#
# f_a()
# f_b()
# print(num)

def f_a():
    print(num)


def f_b():
    global num
    num = 500
    print(num)


f_a()
f_b()
print(num)
