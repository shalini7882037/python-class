a = [1, 2, 3]
b = a #b copies the list a, and they're aliases 
c = a[:] #c creates a new list, that contains same elements as a
b.append(4) # since a and b are aliases of each other, any change made in b is reflected in a too
c.append(99) #since c is not an alias of a, it is unaffected and simply adds an element 99 to its end
print("a =", a)
print("b =", b)
print("c =", c)
print("b is a:", b is a, "| c is a:", c is a)
