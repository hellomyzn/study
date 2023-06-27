d = {'x': 10, 'y': 20}
print(d)

# print(help(dict))

print(d.keys())
print(d.values())
d2 = {'x': 1000, 'j': 500}
print(d)
print(d2)

d.update(d2)
print(d)

print(d.get('x'))
# None
print(d.get('z'))

d.pop('x')
print(d)

del d['y']
print(d)

d.clear()
print(d)


d = {'a': 100, 'b': 200}
print('a' in d)
print('j' in d)
