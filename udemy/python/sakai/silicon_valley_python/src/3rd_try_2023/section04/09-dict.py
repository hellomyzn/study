d = {'x': 10, 'y': 20}
print(d)
print(type(d))

print(d['x'])
print(d['y'])

d['x'] = 100
print(d)
d['x'] = 'XXX'
print(d)
d['z'] = 30
print(d)

d[1] = 100000
print(d)

d = dict(a=10, b=20)
print(d)
