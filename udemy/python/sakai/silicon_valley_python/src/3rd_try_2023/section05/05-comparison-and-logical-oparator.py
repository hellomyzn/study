a = 1
b = 1


print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

if a > 0:
    if b > 0:
        print('a and b are positive')

if a > 0 and b > 0:
    print('a and b are positive')


a = -1
b = 1

if a > 0:
    print('a or b is positive')
elif b > 0:
    print('a or b is positive')

if a > 0 or b > 0:
    print('a or b are positive')



