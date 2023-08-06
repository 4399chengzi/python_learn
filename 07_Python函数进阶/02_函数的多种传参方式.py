"""
演示函数的多种传参方式
"""


# def user_info(name, age, gender):
#     print(name, age, gender)
#
#
# user_info(name='a', age=1, gender='男')
# user_info(age=1, gender='男', name='b')
# user_info('a', gender='2', age=1)
#
#
# def user_info(name, age, gender='男'):  # 默认值必须在最后
#     print(name, age, gender)
#
#
# user_info(name='a', age=1)
# user_info(name='a', age=1, gender='女')


# def user_info(*args):  # 默认值必须在最后
#     print(args)
#
#
# user_info('a', 1, '女')  # 元组

def user_info(**args):  # 默认值必须在最后
    print(args)


user_info(name='a', age=1, gender='女')
