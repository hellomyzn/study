"""
import as
"""
import sys
# import lesson_package.utils
# from lesson_package import utils
# import modulesAndPackages
from modulesAndPackages.lesson_package.utils import say_twice

r = say_twice("hoge")
print(r)


"""
バージョンによるエラーを避けるためのインポート
"""

try:
    from lesson_package import human
except ImportError:
    from lesson_package.talk import human



"""
アスタリスクインポート
"""

from lesson_package.talk import animal

# __init__.pyに__all__に定義されているライブラリを読み込む
from lesson_package.talk import *
print("test")



"""
コマンドライン引数
"""
print(sys.argv)

r = say_twice("hello")
print(r)



print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())
