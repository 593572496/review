import re
from collections import defaultdict
s = 'wanlinameage'
print(re.match('name', s))
result = re.findall('a', s)
print(result)

ss = 'https://www.baidu.com/s?wd=python正则中的group和groups&rsv_spt=1&rsv_iqid=0xaa4311a100001ac9&issp=1&'
ss1 = 'python'
result = re.search(r'(?:www).(\w+).(\w+)', ss)
print(result.group())
print(result.groups())
result = re.findall(r'py\b', ss1)
print(result)
dict1 = defaultdict(int)
dict1['wanli'] =+1
print(dict1['wanli'])