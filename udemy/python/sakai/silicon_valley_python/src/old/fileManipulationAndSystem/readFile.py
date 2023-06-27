s = """\
AAA
BBB
CCC
DDD"""

# with open("text.txt", "w") as f:
#     f.write(s)

with open("text.txt", "r") as f:
    # print(f.read())

    chunk = 2
    while True:
        line = f.read(chunk)
        print(line)
        if not line:
            break

with open("text.txt", "r") as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
