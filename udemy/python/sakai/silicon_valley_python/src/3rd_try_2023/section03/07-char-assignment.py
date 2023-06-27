print('a is {}'.format('test'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))
print('My name is {0} {1}'.format('Jun', 'Sakai'))
print('My name is {0} {1}. Watashi ha {1} {0}'.format('Jun', 'Sakai'))
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name='Jun', family='Sakai'))

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
