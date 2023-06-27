t = (1,2,3,4,5)
print(t)

type(t)
t[0] = 1000
print(t[0])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.count(1))
print(help(t))


 t = ([1,2,3],[4,5,6])
 t[0] = [1]
 t[0][0]  = 100
 print(t)


 num_tuple = (10, 20)
 print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200

a, b = b, a
print(a, b)
