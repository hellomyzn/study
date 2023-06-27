some_list = [1,2,3,4,5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

for i in some_list:
    print(i)

for s in 'abcds':
    print(s)

for w in ['My', 'name', 'is', 'Mike']:
    if w == 'name':
        continue
    if w == 'Mike':
        break
    print(w)
