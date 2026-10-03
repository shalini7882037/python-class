a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print("a =", a)
print("b =", b)
print("c =", c)
print("b is a:", b is a, "| c is a:", c is a)
