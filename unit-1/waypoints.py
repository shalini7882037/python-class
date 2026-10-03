errors = ["E2", "E7"]
print(errors)

errors.append("E2")
print("after append: ", errors)

errors.insert(0, "E1")
print("after insert: ", errors)

errors.remove("E7")
print("after remove:", errors)
print("")
print("")

readings = [10, -1, -1, 20, 30]
for r in readings:
    if r == -1:
        readings.remove(r)
print(readings)
print("")
print("")
readings = [12, 45, 7, 61, 33]
doubled = [r *2 for r in readings]
big = [r for r in readings if r > 30]
print(doubled)
print(big)  