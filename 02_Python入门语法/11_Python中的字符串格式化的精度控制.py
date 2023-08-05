# 通过占位的形式，完成拼接
name = "周鹏程"
message = "学IT来：%s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "第%s期,平均工资%s元" % (class_num, avg_salary)
print(message)

name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s%d%f" % (name, setup_year, stock_price)
print(message)

num1 = 11
num2 = 11.345
print('%5d' % num1)
print('%1d' % num1)
print('%7.2f' % num2)
print('%.2f' % num2)
