"""
演示Python中
if else的组合判断语句
"""

# 获取键盘输入
age = int(input("请输入你的年龄："))

# 通过if判断是否成年人
if age >= 18:
    print("您已成年，游玩需要买票，10元")
else:
    print("你未成年，可以免费游玩")

print("祝您游玩愉快")
