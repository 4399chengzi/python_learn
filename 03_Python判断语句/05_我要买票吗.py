"""
演示Python中
if else的组合判断语句
我要买票吗
"""

# 获取键盘输入
height = int(input("请输入你的身高（cm）："))

# 通过if判断是否成年人
if height > 120:
    print("您的身高超过120cm，需要买票，10元")
else:
    print("你的身高低于120cm，可以免费游玩")

print("祝您游玩愉快")
