from sklearn.cross_validation import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np



"""
Section1
"""
num = 1
name = "Mike"
new_name = "1"
is_ok = True

# type()で変数の型を出力する
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# numをint型からstr型に変更
num = name
print(num, type(num))

# str型の1をint()でキャストして型を検証
new_num = int(new_name)
print(new_num, type(new_num))



"""
Section2
"""

# print()の際にsep=","を引数に渡すと,[,]で区切ってくれる
print("Hi", "Mike", sep=',', end='\n')
print("Hi", "Mike", sep=',', end='.\n')

"""
Section3
"""

# //小数点以下を省く、**でべき乗
print(17 / 3, 17 // 3, 5 * 5 * 5 * 5 * 5, 5**5)

# round関数の使い方
pie = 3.14151515151515
round(pie, 2

import math
# 平方根
result = math.sqrt(25)
print(result)

#log
y = math.log2(10)
print(y)

print(help(math))


"""
Section4
"""

# \の使い方
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

# 改行時の注意点,\nameなどは前半の\nが改行と判断されてしますので、頭にrを付け足す
print('Hello.\nHow are you')
print('C:\name/\name')
print(r'C:\name\name')


# """の使い方
print("##############")
print("""\
line1
line2
line3\
""")
print("##############")


# str型の演算子
print("Hi." * 3 + "Mike")
print("Py""thon")
prefix = "py"
print(prefix + "thon")



"""
Section5
"""

# str型を配列で文字を出力する
word = "python"
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print("###############################")
print(word[0:2])
print(word[:2])
print("###############################")
print(word[2:])
print("###############################")
word = "j" + word[1:]
print(word)
n = len(word)
print(n)



"""
Section6
"""
# 特定の文字列があるかどうか
s = "My name is Mike. Hi Mike"
print(s)
is_start = s.startswith("My")
print(is_start)


# 最初のMikeがあるかどうか調べる
print(s.find("Mike"))
# 最後のMikeがあるかどうか調べる
print(s.rfind("Mike"))
# Mikeの数をカウントする
print(s.count("Mike"))
# 文頭の文字を大文字にする
print(s.capitalize())
# 全部の文字を大文字にする
print(s.upper())
# 全部の文字を小文字にする
print(s.lower())
# MikeをNuncyに変更する
print(s.replace("Mike", "Nuncy"))


# 文字の代入
print("a is {}".format("a"))
print("a is {} {} {}".format(1, 2, 3))
print("a is {0} {1} {2}".format(1, 2, 3))
print("a is {2} {1} {0}".format(1, 2, 3))
print("My name is {name} {family}".format(name="Jun", family="Sakai"))



print(help(list))


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_train, x_test = tts(x, test_size=0.3, random_state=1)

print(x_train)
print(x_test)

x = [2, 4, 6]


x = np.linspace(0, 3, 100)
x = np.arange(0.1, 10, 0.1)
print(x.shape)
y = x ** 2
plt.plot(x, y)
plt.show()


x = np.arange(0.1, 10, 0.1)
print(x)


while True:
    word = input()
    if word == "OK":
        break
    print("next")

# 小数点以下20桁までの出力
x = np.linspace(0, 10, 100)
print(x)
for n in x:
    print("{0:.20f}".format(n))


x = range(0, 10, 3)
print(x)


list = range(5)
print(list)  # [0, 1, 2, 3, 4]


# デコレーター
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print("result", result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


@print_info
@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)


# ラムダ式
l = ["Mon", "tue", "wed", "Thu", "fri", "sat", "Sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


change_words(l, lambda word: word.capitalize())

matplotlib.pyplot.plot()
plt.show()


l = ["Good morning", "Good afternoon", "Good night"]
for i in l:
    print(i)


def greeting():
    yield "Good morning"
    for i in range(10):
        print(i)
    yield "Good afternoon"
    for i in range(10, 20):
        print(i)
    yield "Good night"


for g in greeting():
    print(g)


def coounter(num=10):
    for _ in range(num):
        yield 'run'


c = coounter()
g = greeting()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print("hoge")
print(next(g))
print("hoge")
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))


# リスト内包表記
t = (1, 2, 3, 4, 5)
r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

# 辞書包括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}

for x, y in zip(w, f):
    d[x] = y
print(d)


d = {x: y for x, y in zip(w, f)}
print(d)


# 集合内包表記
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)


x, y = numpy.arange(-30, 30, 1), numpy.arange(-30, 30, 1)
n = []
m = []
for i in range(-100, 100):
    n += [0]
print(x.shape)


plt.xlim(-30, 30)
plt.ylim(-30, 30)
plt.plot(x, y)
plt.plot(n)


plt.grid(color='r')
plt.plot(n)
plt.show()

print(y)

print(globals())


# 例外
l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Don't worry", ex)
except Exception as ex:
    print(ex)
else:
    print("done")
finally:
    print("clean up")
print("last")


# 独自例外
raise IndexError('test error')


# from,import,asなど
import lesson_package.utils
from lesson_package import utils
from lesson_package.utils import say_twice

x = np.arange(-10, 10, 0.02)
y = np.arange(-10, 10, 0.02)
print(x.shape)
print(y.shape)
print(x)
x_axis, y_axis = np.meshgrid(x, y)


print(x_axis.shape)
print(x_axis)

sum = np.concatenate([x_axis, y_axis])
print(sum.shape)


from lesson_package.talk import human as hum
from lesson_package.tools import sample as sam
print(hum.sing())
print(sam.hogehoge())

import builtins
print(help(builtins))


ranking = {
    'A': 100,
    'B': 85,
    'C': 95}
print(sorted(ranking, key=ranking.get, reverse=True))


# 適当な文字列に同じ文字がいくつ入っているかを計算する
s = "jsarkngkklkvfoizhlfslkefd,mdfd/.kfmdkflkeeflsjdfnndnvs"
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

print(colored("test", "red"))

import collections
print(collections.__file__)
print(plt.__file__)

import sys
print(sys.path)
