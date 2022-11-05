listex = []
for i in range(10):
    listex.append(i)
print(listex)

listcomp = [i for i in range(10)]
print(listcomp)

a = ["a", "b", "c", "d"]
b = [1, 2, 3, 4]

dictexample = {}
for i in range(4):
    key = a[i]
    value = b[i]
    dictexample[key] = value
print(dictexample)

dictcomp = {a[i]:b[i] for i in range(4)}
print(dictcomp)
