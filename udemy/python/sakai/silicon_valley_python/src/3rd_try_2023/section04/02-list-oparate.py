s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'X'
print(s)

s[2:5] = []
print(s)

s[:] = []
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n)

n.append(100)
print(n)

n.insert(0, 200)
print(n)

n.pop()
print(n)

n.pop(0)
print(n)

del n[0]
print(n)

n.remove(2)
print(n)


a = [1,2,3,4,5]
b = [6,7,8,9,10]
x = a + b
print(a)
print(b)
print(x)

a += b
print(a)

a.extend(b)
print(a)

