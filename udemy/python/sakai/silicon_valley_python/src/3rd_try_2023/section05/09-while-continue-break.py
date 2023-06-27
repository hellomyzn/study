count = 0
while count < 5:
    print(count)
    count += 1

c = 0
while True:
    if c >= 5:
        break
    if c == 2:
        c += 1
        continue

    print(c)
    c += 1
