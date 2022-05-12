import os

list1 = [1, 4, 3, 2]
list2 = ['a', 'b', 'c', 'd']
result = zip(list1, list2)
# print(dict(result))
# print(list(result))
dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
l1, l2 = zip(*dict1.items())
print(l1, l2)

test_list = list(result)
print(sorted(test_list, key=lambda x: x[0], reverse=True))
print(max(test_list, key=lambda x: x[0]))
print(list(map(lambda x: x[0] + 1, test_list)))
print(list(filter(lambda x: x[0] > 2, test_list)))
print(os.getcwd())
