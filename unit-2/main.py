import sensors

readings = [62, 84, 71]

print("threshold:", sensors.THRESHOLD)
print("average :", sensors.average(readings))

for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")    