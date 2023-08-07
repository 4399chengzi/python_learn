"""
演示文件的追加操作
"""

with open('bill.txt', 'a', encoding='utf-8') as f:
    f.write('a a a a a')

# 直接open，要flush和close
