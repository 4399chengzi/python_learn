"""
演示异常的捕获
"""

# try:
#     f = open('1.txt', 'r', encoding='utf-8')
# except:
#     print('bug')
#     f = open('1.txt', 'w', encoding='utf-8')


# 捕获指定异常
# try:
#     # print(name)
#     i = 1 / 0
# except NameError as e:
#     print('bug')
#     print(e)

# # 捕获多个异常
# try:
#     print(name)
#     i = 1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print('bug')
#     print(e)

# 捕获所有异常
# try:
#     print(name)
#     i = 1 / 0
# except Exception as e:
#     print('bug')
#     print(e)

# # else
# try:
#     # print(name)
#     # i = 1 / 0
#     i = 1 / 1
# except Exception as e:
#     print('bug')
#     print(e)
# else:
#     print('ok')

# finally
try:
    # print(name)
    i = 1 / 0
    a = 1 / 1
except Exception as e:
    print('bug')
    print(e)
else:
    print('ok')
finally:
    print('OK')
