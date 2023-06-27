s = """\
AAA
BBB
CCC
DDD"""

with open("text.txt", "w+") as f:
    f.write(s)
    f.seek(0)
    print(f.read())

with open("text.txt", "r+") as f:
    f.write(s)
    f.seek(0)
    print(f.read())
