"""
リスト内包表記
"""


t = [1, 2, 3, 4, 5]
t2 = [5, 6, 7, 8, 9]

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)
 r = [i * j for i in t for j in t2]
 print(r)


 """
 辞書内包表記
 """

 w = ["mon", "tue", "wed"]
 f = ["coffe", "milk", "water"]

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)


d = {x: y for x, y in zip(w, f)}
print(d)


"""
集合内包表記
"""

s = set()
for i in range(10):
    if i % 2 == 0:
        s.add(i)
print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)



"""
ジェネレーター内包表記
"""


def g():
    for i in range(10):
        yield i
g = g()

g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)


"""
スコープ
"""

animal = "cat"
def f():
    print(animal)

f()
print(animal)




"""
例外
"""


l = [1, 2, 3]
i = 5

try: #実行しようとする処理
    l[i]
except IndexError as ex: #インデックスエラーが起きたらexにエラー内容を返す
    print("Don't worry", ex)
except Exception as ex: #その他のエラーが起きたらexにエラー内容を返す
    print(ex)
except SyntaxError as ex:
    print(ex)
else: #try処理が行われたら処理される
    print("done")
finally: #エラーが起きても起きなくても処理される
    print("clean up")
print("last")
