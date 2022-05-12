"""
测试局部变量和全局变量，测试可变类型和不可变类型
"""
import sys

cc = 2


def out_func():
    wanli = 'wanli'
    a = 1
    list1 = ['2']

    def in_func():
        b = 2
        nonlocal a
        a += b  # 修改不可变变量需要使用global获取权限
        list1.append('3')  # 修改可变变量不需要获取权限
        print('内部函数', a, list1, locals())

    return in_func


r1 = out_func()
print(r1)
r1()
print(globals())