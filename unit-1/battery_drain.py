battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
    print(f"minute {minutes:2d} -> battery {battery}%")
print("ALERT")
