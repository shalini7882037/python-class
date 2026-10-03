bt_capacity=float(input("Battery capacity(mah): "))
current_draw=float(input("Current drawn: "))
est_rt=bt_capacity/current_draw
print(f"Estimated run-time: {est_rt:.2f} hours")