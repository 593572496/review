# 数据类型的转换
a = float(2.4444)
print(int(a))
# bool
list1 = []
print(bool(list))

print('1', '2', '3', sep='#')
print('1', '2', '3', end='\n')
# 格式化输出
name = 'WANLI'
age = '25'
city = '重庆'
print('name:%s,age:%s,city:%s' % (name, age, city))
print('name:{},age:{},city:{}'.format(name, age, city))
print('name:{name},age:{age},city:{city}'.format(name=name, age=age, city=city))
print('name:{0},age:{0},city:{1}'.format(name, age))
