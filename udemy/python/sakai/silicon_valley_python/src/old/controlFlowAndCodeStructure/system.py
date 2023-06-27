"""
1行が長くなる場合
"""
# 横が80文字以内にする
x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 +\
    + 1 + 1 + 1 + 1

print(x)


"""
if文
"""
x = -10

if x < 0:
    print("negative")
elif == 0:
    print("zero")
else
    print("positive")


"""
論理演算子
"""

a = 2
b = 2

a == b
a != b
a < b
a > b
a <= b
a >= b
a > 0 and b > 0
a > 0 or b > 0
a is b



"""
in と not
"""


y = [1,2,3]
x = 1

if x in y:
    print("in")

if 100 not in y:
    print("not in")


is_ok = True
if not is_ok:
    print("hello")


"""
Noneの判定
"""

is_empty = None
if is_empty is not None:
    print("None")



"""
While
"""

count = 0
while count < 5:
    print(count)
    count += 1


while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue
    print(count)
    count += 1


while count < 5:
    print(count)
    count += 1
else:
    print("done")


"""
input
"""

while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break

    print("next")




"""
for
"""

some_list = [1,2,3,4,5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1


# for文で書く
for i in some_list:
    print(i)

# for else
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print("stop eating")
        break
    print(fruit)
else:
    print("i ate all")


# range関数
for i in range(2,10, 3):
    print(i)

for i in range(10):
    print(i , "hello")

for _ in range(10):
    pritn("good bye")


"""
enumerate
"""

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


"""
zip
"""

days = ["Mon", "Tue", "Wed"]
fruits = ["apple", "banana", "orange"]
drinks = ["coffee", "tea", "beer"]

for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])


for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)



"""
dictのfor文
"""

d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k , v)
    
