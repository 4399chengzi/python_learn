"""
演示
"""


def print_file_info(filename):
    """
    输出文件内容
    :param filename:
    :return:
    """
    f = None
    try:
        f = open(filename, 'r', encoding='utf-8')
        print(f.read())
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    追加内容
    :param file_name:
    :param data:
    :return:
    """
    f = open(file_name, 'a', encoding='utf-8')
    f.write(data)
    f.write('\n')
    f.close()


if __name__ == '__main__':
    print_file_info('1.txt')
    append_to_file('1.txt','123')
