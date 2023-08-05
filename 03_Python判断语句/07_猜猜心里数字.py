"""
演示if elif else练习题：猜猜心里数字
"""

# 定义一个变量数字
num = 5
# 通过键盘输入获取猜想的数字，通过多次if和elif的组合进行猜想比较
if int(input("请输入一个数字：")) == num:
    print("等")
elif int(input("请再输入一个数字：")) == num:
    print("等")
elif int(input("请再输入一个数字：")) == num:
    print("等")
else:
    print("不等")
