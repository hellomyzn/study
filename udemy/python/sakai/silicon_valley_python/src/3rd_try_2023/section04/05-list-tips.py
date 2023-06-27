seat = []
min = 0
max = 5
print(min <= len(seat) < max)

seat.append('p')
print(len(seat))
print(min <= len(seat) < max)

seat.append('p')
print(len(seat))
print(min <= len(seat) < max)


seat.append('p')
seat.append('p')
print(len(seat))
print(min <= len(seat) < max)

seat.append('p')
print(len(seat))
print(min <= len(seat) < max)

seat.pop(0)
print(len(seat))
print(min <= len(seat) < max)
