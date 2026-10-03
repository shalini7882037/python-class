robot_name ="Alpha"
battery_pct=78.5
waypoints =12
is_docked=True
print(robot_name, battery_pct, is_docked,waypoints)
print(type(robot_name), type(battery_pct),type(is_docked), type (waypoints))
if(battery_pct<30):
    print("Low Battery, plug in asap")