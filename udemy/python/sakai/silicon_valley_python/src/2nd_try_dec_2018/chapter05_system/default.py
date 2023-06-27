def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)


def test_func(x, l=None):
    if l is None:
    	l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)
