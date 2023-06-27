def say_something(word, *args):
    print("word =", word)
    for arg in args:
        print(arg)


say_something("HI!", "Mike", "Nance")


t = ("Mike", "Nancy")
say_something("HI!", *t)



def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


d = {
        'entree': 'beef',
        'drink': 'ice coffee',
        'desseert': 'ice'
        }


menu(**d)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu("banana", 'apple', 'orange', entree="beef", drink='coffee')

