"""
演示list列表的循环遍历
for简单普遍，while灵活
"""


# while

def list_while_f():
    """
    使用while循环遍历列表
    :return:
    """
    my_list = ['a', 'b', 'c']

    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1


list_while_f()


def list_for_f():
    """
    使用for循环遍历列表
    :return:
    """
    my_list = ['a', 'b', 'c']

    for element in my_list:
        print(element)


list_for_f()
