"""
for循环的嵌套使用
"""

for i in range(1, 101):
    print('第%d天' % i)
    for j in range(1, 11):
        print(f'送第{j}支玫瑰')
print(f"坚持到第{i}天，表白成功")
