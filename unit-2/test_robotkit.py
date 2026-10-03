from robotkit import sensors, control

d = sensors.read_ultrasonic()

print("distance:", d, "->", control.decide(d))
print("package contents:", [n for n in dir(control) if not n.startswith("_")])
