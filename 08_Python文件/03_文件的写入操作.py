"""
演示文件的写入操作
"""

with open('测试.txt', 'w', encoding='utf-8') as f:
    f.write('a a a a a')

# 直接open，要flush和close
