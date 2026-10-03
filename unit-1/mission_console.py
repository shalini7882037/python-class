THRESHOLD = 70.0
readings = []
 
while True:
    print("\n1-add reading  2-report  3-quit")
    choice = input("choice: ")
    if choice == "1":
        value = float(input("sensor value: "))
        readings.append(value)
    elif choice == "2":
        if not readings:
            print("no data yet")
            continue
        alerts = 0
        for r in readings:
            if r > THRESHOLD:
                alerts += 1
        avg = sum(readings) / len(readings)
        print(f"count={len(readings)}  avg={avg:.1f}  alerts={alerts}")
    elif choice == "3":
        print("mission console closed")
        break
    else:
        print("invalid choice")