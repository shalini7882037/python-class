while True:
    text = input("Enter battery % (0-100): ")
    value = float(text)
    if 0 <= value <= 100:
        break
    print("Out of range, enter value within range and try again")
print("Value accepted:", value)
