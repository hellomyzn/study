f = open("text.txt", "w")
f.write("test\n")
    print("My","name","is","Mike", sep="#", end="!", file=f)
f.close()

with open("text.txt", "a") as f:
    f.write("Test\n")
