i = [1, 2, 3, 4, 5]
j = i
j[0] = 100

print("j" ,j)
print("i", i)


x = [1,2,3,4,5]
y = x.copy()
z = x[:]
y[0] = 100
print("x", x)
print("y", y)
print("z", z)


X = 20
Y = X
Y = 5


print(id(X))
print(id(Y))
print(X)
print(Y)

X = ["a", "b"]
Y = X
Y[0] = "p"

print(id(X))
print(id(Y))
print(X)
print(Y)

