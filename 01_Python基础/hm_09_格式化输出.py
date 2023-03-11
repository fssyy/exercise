# 定义字符串变量name，输出：我的名字叫小明，请多多关照！
name = '小明'
print('我的名字叫%s，请多多关照！' % name)
# 定义整数变量student_no，输出：我的学号是000001
student_01 = 1
print('我的学号是%06d' % student_01)
# 定义小数price、weight、money，输出:苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print('苹果单价%.02f元/斤，购买了%.02f斤，需要支付%.02f元' % (price, weight, money))
# 定义一个小数scale，输出的数据比例是10.00%
scale = 0.25 * 100
print('数据的比例是%.02f%%' % scale)

# 输出python中的关键字
import keyword

print(keyword.kwlist)


# 使用format（）函数进行格式化
string = "我是学{0}呢，还是学{1}呢"
print(string.format("python","java"))