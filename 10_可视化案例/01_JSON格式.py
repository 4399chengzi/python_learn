"""
演示JSON格式
"""

import json

# my_list = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]
#
# json_dict = json.dumps(my_list)
#
# print(json_dict, type(json_dict))
#
# my_dict = {"a": 1, "b": 2}
# json_dict = json.dumps(my_dict)
# print(json_dict, type(json_dict))

s = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]'
s1 = "[{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]"
l = json.loads(s)
# l1 = json.loads(s1)
print(l, type(l))
