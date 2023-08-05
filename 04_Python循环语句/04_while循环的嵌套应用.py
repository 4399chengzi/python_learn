"""
演示while循环的嵌套应用
"""

i = 1
while i <= 100:
    print('第%d天' % i)
    j = 1
    while j <= 10:
        print(f'送第{j}支玫瑰')
        j += 1
    i += 1
print(f"坚持到第{i-1}天，表白成功")
