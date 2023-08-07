"""
演示文件操作综合案例
"""

with open('bill.txt', 'r', encoding='utf-8') as f:
    with open('bill.txt.bak', 'w', encoding='utf-8') as fw:
        for line in f:
            line = line.strip()
            if line.split(',')[4] == '测试':
                continue
            fw.write(line)
            fw.write('\n')

