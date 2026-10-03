temp = float(input("Enclosure temperature: "))
if temp < 0:
    mode = "HEATER ON"
elif temp <= 40:
    mode = "NORMAL"
elif temp <= 60:
    mode = "COOLING"
else:
    mode = "SHUTDOWN"
print("Operating mode:", mode)
