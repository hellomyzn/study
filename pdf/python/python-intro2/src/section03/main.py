# セッターメソッド / ゲッターメソッド
# pra3

class Neko:

    def __init__(self):
        self.__name = 'キティ'

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

# q3
class Neco2:
    ''' Neco '''

    def __init__(self):
        self.__name = 'キティ'
        self.__age = 0
        self.__type = '三毛'

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

kitty = Neco2()
print(kitty.get_name())
print(kitty.get_age())
print(kitty.get_type())
yuzu = Neco2()
yuzu.set_name('ゆず')
yuzu.set_age(3)
yuzu.set_type('雑種')
print(yuzu.get_name())
print(yuzu.get_age())
print(yuzu.get_type())
