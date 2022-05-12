def func_test_Default_parameters(a, b, c=2, d=None):
    print(a, b, c, d, sep='#', end='\n\n')


func_test_Default_parameters(0, 1, d='rr')


def func_test_args(a, b, *args):

    print(a, b)
    for i in args:
        print(i)


func_test_args('wanli', 'xiaoming', "gggg", 'kkkk')


def test_return():
    return '1', '2', '3'


result = test_return()
print(result)
a, b, c = test_return()
print(a, b, c)
