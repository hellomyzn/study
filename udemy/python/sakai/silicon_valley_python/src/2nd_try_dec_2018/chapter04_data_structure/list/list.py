l = [1, 20, 4, 50, 2, 1, 2,]

print(l)

print(l[1])

print(l[-1])

print(l[-2])

print(l[0:2])

print(l[:2])

print(l[2:5])

print(l[2:])

print(l[:])




l = list("hogefugapiyo")
print(type(l))
print(l)




n = [1,2,3,4,5,6,7,8,9,10]
print(n)
print(n[::2])
print(n[::-1])

# 2次元配列
a = ['a','b','c']
n = [1,2,3]
x = [a, n]

print(x)
print(x[0])
print(x[1])
print(x[0][1])


s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(s[0])
s[0] = 'X'
print(s)

s[2:5] = ["C", "D", "E"]
print(s)

s[2:5] = []
print(s)


s[:] = []
print(s)


n = [1,2,3,4,5,6,7,8,9,10]
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

del n
# ここでエラーが起こる
# print(n)


n = [1,2,2,2,3]
n.remove(2)
print(n)

n.remove(2)
print(n)

n.remove(2)
print(n)

n.insert(2, 90)
print(n)


a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(a)
print(b)


x = a + b
print(x)
a += b
print(a)


x = [1,2,3,4,5]
y = [6,7,8,9,10]

x.extend(y)
print(x)








































