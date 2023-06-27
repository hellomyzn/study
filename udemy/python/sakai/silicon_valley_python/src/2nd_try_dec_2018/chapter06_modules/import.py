# import lesson_package.utils
# from lesson_package import utils
# from lesson_package.utils import say_twice
# r = lesson_package.utils.say_twice("hoge")
# r = utils.say_twice("hoge")
# r = say_twice("hello")

# print(r)

# from lesson_package.talk import human
# from lesson_package.talk import animal
from lesson_package.talk import *

print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())
