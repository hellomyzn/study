"""
関数定義
"""

def say_something():
    s = print("hi")
    return s

say_something()
print(type(say_something ))

f = say_something
f()

def say_something():
    s = "hi"
    return s

result = say_something()
print(result)


def what_is_this(color):
    if color == "red":
        return "Tomato"
    elif color == "green":
        return "green pepper"
    else:
        return "I dont know"
    print(color)

result = what_is_this("red")
print(result)


num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b

f = add_num(10, 20)
print(f)



"""
デフォルト引数
"""

def menu(entree, drink, dessert):
    print("entree : ", entree, "\ndrink : ", drink, "\ndessert : ", dessert)

menu(entree="beef", dessert="ice", drink="drink")



def menu(entree='beef', drink='wine', dessert='ice'):
    print(entree, drink, dessert)

menu()
menu("chiken", "coffee")




"""
デフォルト引数で気をつけること
"""

def test_func(x, l=[]):
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)

# リストは参照渡しだから、デフォルト引数にリストや、dictを宣言すると、前のインスタンスの
# リストを参照してしまう。


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func(100)
print(r)

r = test_func(100)
print(r)



"""
位置引数
"""

def say_something(word, *args):
    print("word : ", word)
    for arg in args:
        print(arg)


say_something("Hi", "Mike", "Nance")

t = ["Mike", "Nancy"]
say_something("Hi", *t)



"""
キーワード引数
"""


def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

menu(entree="beef", drink="coffee")


d = {
     "entree": "beef",
     "drink": "ice coffee",
     "desert": "ice"
     }

menu(**d)



def menu(food, *args, **kwargs):
    print(food), #banana
    print(args), #("apple","orange")
    print(kwargs) #{"entree":"beef", "drink":"coffee"}
menu("banana", "apple", "orange", entree="beef", drink="coffee")


"""
docstring
"""


def example_func(param1, param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int) : The first parameter.
        param2 (str) : The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    print(param1)
    print(param2)

    return True


print(example_func.__doc__)
print(help(example_func))




"""
関数内関数
"""

def outer(a, b):
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)



"""
クロージャー
"""

def outer(a, b):
    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)



def circle_area_funk(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

cal1 = circle_area_funk(3.14)
cal2 = circle_area_funk(3.141592)
print(cal1(10))
print(cal2(10))



"""
デコレーター
"""

def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args:", args)
        print("kwargs", kwargs)
        result = func(*args, **kwargs)
        print("result", result)
        return result

    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_more
@print_info
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)



"""
ラムダ
"""


l = ['Mon', 'Tue', 'Wed', 'Thu', 'fri', 'std', 'Sun',]

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)


sample_func2 = lambda word: word.capitalize()
change_words(l, lambda word: word.capitalize())



"""
ジェネレーター
"""


l = ['Good morning','Good afternoon','Good night']
for i in l:
    print(i)


def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"

for g in greeting():
    print(g)

def counter(num=10):
    for _ in range(num):
        yield "run"

g = greeting()
c = counter()

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
