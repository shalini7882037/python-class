robot = {"name": "Alpha", "battery": 78, "mode": "auto"}
print(robot)
print(robot["name"])
robot["battery"] -= 5
robot["speed"] = 0.4
print(robot)
print("keys  :", list(robot.keys()))
print("values:", list(robot.values()))
print("")
print("")
robot = {"name": "Alpha", "battery": 78}
print(robot.get("speed"))
print(robot.get("speed", 0.0))
print("speed" in robot)
print("")
print("")
log = ["E2", "E7", "E2", "E1", "E7", "E2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)
for code in sorted(freq, key=freq.get, reverse=True):
    print(f"{code} occurred {freq[code]} time(s)")
print("")
print("")
robot = {"name": "Alpha", "battery": 73, "mode": "auto"}
for key, value in robot.items():
    print(f"{key:<8} {value}")