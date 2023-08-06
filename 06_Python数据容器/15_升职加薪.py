"""
演示升职加薪
"""

stu_dict = {
    'a': {
        'a': 1,
        'b': 2,
        'c': 1
    }, 'b': {
        'a': 1,
        'b': 2,
        'c': 2
    }, 'c': {
        'a': 1,
        'b': 2,
        'c': 3
    }, 'd': {
        'a': 1,
        'b': 2,
        'c': 1
    }, 'e': {
        'a': 1,
        'b': 2,
        'c': 2
    }
}

for key in stu_dict:
    if stu_dict[key]['c'] == 1:
        temp = stu_dict[key]
        temp['c'] = 2
        temp['b'] += 1000
        stu_dict[key] = temp
print(stu_dict)
