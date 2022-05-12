def test(i):
    if i == 10:
        return 10
    else:
        return i + test(i + 1)


print(test(1))

func1 = lambda x, y: x + y
print(func1(1, 2))
