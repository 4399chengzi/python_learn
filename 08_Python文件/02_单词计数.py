"""
演示单词计数
"""

# with open('测试.txt', 'r', encoding='utf-8') as f:
#     print(f.read().count('a'))

with open('测试.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        words = line.strip().split(' ')
        for word in words:
            if word == 'a':
                count += 1
    print(count)
