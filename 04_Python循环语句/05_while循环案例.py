"""
99乘法表
"""

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}×{i}={i*j}\t', end='')
        j += 1
    print()
    i += 1
