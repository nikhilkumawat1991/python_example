

st = "aabbbccde"


lst = list(st)
distinct = set(lst)


dt = {}
for letter in distinct:
    dt[letter] = lst.count(letter)

print(dt)
