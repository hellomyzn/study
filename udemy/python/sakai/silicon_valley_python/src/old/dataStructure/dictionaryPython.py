d = {'x' : 10, 'y' : 20}
print(d)

print(type(d))
d['x']
d['y'] = 100
d['z'] = 200
d[1] = 300
print(d)

dd = dict(a=10, b=20)
print(dd)


print(help(dict))

d.keys()
d.values()
d2 = {'a':1000, 'b':2000}
d.update(d2)
print(d)
d.get('x')

del d['b']
print(d)
d.clear()
print(d)


x = {'a' : 1}
y = x
y['a'] = 1000
print(x)
print(y)


x = {'a' : 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
