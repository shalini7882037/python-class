obstacles = [(1, 2), (3, 3), (0, 4)]
for row in range(5):
    for col in range(5):
        if (row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end="")
    print()
print("")
print("")
readings = [12, -1, 34, 78, 15]
for r in readings:
    if r < 0:
        continue
    if r > 70:
        print("DANGER at", r)
        break
else:
    print("all readings safe")
