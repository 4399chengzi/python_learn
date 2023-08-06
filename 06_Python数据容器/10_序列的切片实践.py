"""
演示序列的切片实践
"""

my_str = "万过薪月，员序程马黑来，nohtyP学"

print(my_str[9:4:-1])
print(my_str[5:10][::-1])
print(my_str.split("，")[1].replace("来",'')[::-1])
print(my_str[-10:-15:-1])
print(my_str[::-1][9:14])

