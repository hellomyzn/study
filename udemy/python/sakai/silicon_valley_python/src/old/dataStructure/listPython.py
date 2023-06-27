"""
Section1
List
"""


l = [ 1,2,3,4,5,6,6,7]
print(l)
print(l[1])
print(l[-1])
print(l[2:5])
len(l)
type(l)

print(l[::2])
print(l[::-1])


"""
section2
ListOperation
"""

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s[0])
s[0] = 'X'
s[2:5] = ['C', 'D', 'E']
print(s)
s[2:5] = []
print(s)
s[:] = []
print(s)
s.append("a")
s.append("z")
print(s)
s.insert(0, "0")
print(s)

s.pop()
print(s)
s.pop(0)
print(s)


del s[0]
print(s)


n = [1,2,3,4,5,6]
n.remove(2)
print(n)



a = [1,2,3,4,5]
b = [6,7,8,9,10]
x = a + b
print(x)


"""
section3
List Method
"""

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)


 s = "My name is Mike."
 to_split = s.split(' ')
 print(to_split)

x = ' '.join(to_split)
print(x)


print(help(list))

"""
section4
copy of list
"""


i = [1,2,3,4,5,6]
j = i

j[0] = 100
print('j =', j)
print('i =', i)


x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print("y = ", y)
print("x = ", x)


X = 20
Y  = X

Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)
