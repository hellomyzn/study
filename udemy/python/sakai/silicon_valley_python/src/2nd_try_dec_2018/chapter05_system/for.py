for word in ["My", "name", "is", "Mike"]:
    if word == 'name':
        break
    print(word)

for word in ["My", "name", "is", "Mike"]:
    if word == 'name':
        continue
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print("I ate all")
