def decorator1(func):
    def decorator_content(name, age):
        print('我是装饰器内容1')
        print('我是装饰器内容2')
        func(name,age)
    return decorator_content


@decorator1
def test(name, age):
    print(name, age)

test('wanli','28')
