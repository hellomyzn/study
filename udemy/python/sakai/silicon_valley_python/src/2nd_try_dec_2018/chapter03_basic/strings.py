print('hello')
print("hello")
print("I don't know")
print('I don\'t konw')
print('say "Idon\'t know"')


print("hello. \n How are you?")
print("#############")
print("""\
        line1
        line2
        line3\
        """)
print("#############")

print('Hi' *2 + 'Mike')

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])

print("#############")
print(word[0:2])
print(word[:2])
print("#############")
print(word[2:])

print("#############")
word = 'j' + word[1:]
print(word)

print(word[:])
n = len(word)
print(n)


s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("############################")


print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))





































