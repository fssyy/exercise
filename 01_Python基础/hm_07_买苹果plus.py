# 1.输入苹果的单价
price_str = input('苹果的单价：')
# 2.输入苹果的重量
weight_str = input('苹果的重量：')
# 3.计算支付的总金额
# 注意：两个字符串变量之间不能直接用乘法
price = float(price_str)
weight = float(weight_str)
money = price * weight
print(money)
