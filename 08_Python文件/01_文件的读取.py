"""
演示文件的读取
"""

f = open('测试.txt', 'r', encoding='utf-8')

print(f)

# print(f.read())
# print(f.read(10))
# print(f.read(10))
# 123
# 456
# 78
# 9

# print(f.readlines())  # ['123\n', '456\n', '789']

# print(f.readline())

for lin in f:
    print(lin)

f.close()

with open('测试.txt','r',encoding='utf-8') as f:
    print(f.read())
