d = {'x':10, 'y':20}
print(d)

help(d)


print(d.keys())
print(d.values())

d2 = dict(x=1000, j=5000)
print(d2)

d.update(d2)
print(d)

print(d['x'])
print(d.get('x'))

print(d.get('z'))
print(type(d.get('z')))

print(d)
d.pop('x')

print(d)
del d['y']

print(d)
del d

d = {'a': 100, 'b':200}
print(d)

d.clear()
print(d)

d = {'a': 100, 'b':200}
print('a' in d)

print('s' in d)



