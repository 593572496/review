test_str = 'https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_from=-1'
print(test_str[0:5])
print(test_str[-1])
print(test_str[::-1])
print(test_str.find('*'))  # 找不到返回-1
# print(test_str.index('*')) #找不到报错
print(test_str.find('baidu'))

list1 = ['1', '2']
list2 = ['3', '4']
list3 = list2 + list1
list1.extend(list2)
print(list1)
print(list3)
list3.insert(1, '10')
tuple1 = (1, 2, 3)
dict1 = {'name': 'wanli', 'age': '18'}
dict1.setdefault('name1', 'xiaoming')
dict2 = {'name': 'wanli', 'hhh': 'kkk'}
dict1.update(dict2)
print(dict1)
set1 = {'1', '2', '3'}
set2 = {'3','4','5'}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
set1.update(set2)
print(set1)

