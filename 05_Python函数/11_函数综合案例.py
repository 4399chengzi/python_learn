"""
函数综合案例，黑马ATM
"""

money = 5000000
name = None

name = input("请输入您的姓名：")


def query(showheader):
    if showheader:
        print('-查询余额-')
    print(f'{name},余额{money}元')


def saving(num):
    global money
    money += num
    print('-存钱-')
    print(f'{name},存款{num}元成功')
    query(False)


def geting(num):
    global money
    money -= num
    print('-取款-')
    print(f'{name},取款{num}元成功')
    query(False)


def main():
    print('-主菜单-')
    print(f'{name}欢迎')
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择")


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        saving(int(input("你想要取多少钱")))
        continue
    elif keyboard_input == "3":
        geting(int(input("你想要存多少钱")))
        continue
    else:
        print("程序退出啦")
        break
