"""
讲解字符串格式化的课后练习题
"""
# 定义需要的变量
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司{name},{stock_code},{stock_price}")
print("%f%d%.2f" % (stock_price, growth_days, finally_stock_price))
