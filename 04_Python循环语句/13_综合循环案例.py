"""
综合循环案例
"""

import random

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f'员工{i}绩效分{score}，不满足，不发工资')
        continue
    if money >= 1000:
        money -= 1000
        print(f'员工{i}绩效分{score}，满足，发工资1000元，公司账户余额：{money}')
    else:
        print(f'公司余额不足，不发了')
        break
