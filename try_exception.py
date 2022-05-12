class MyException(Exception):
    def __init__(self, error):
        super().__init__(self)
        self.error_info = error

    def __str__(self):
        return self.error_info

    def __repr__(self):
        return self.error_info


def test_func(a, b):
    if a > b:
        raise MyException('a>b 产生异常')
    else:
        print('程序正常')


try:
    test_func(4, 3)
except MyException as err:
    print(err)
    print('success')
