a = [1, 2, 3]
try:
    print(a[4])
except IndexError:
    print(len(a))
    print("debug")
except KeyError:
    print("debug")

print("new code block")
b = iter(a)
print("string stop")