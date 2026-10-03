def move_robot(x, y, speed=1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")
 
move_robot(3, 4)                    
move_robot(3, 4, 0.5)               
move_robot(y=4, x=3)                
move_robot(3, speed=2.0, y=4) 
print("")
print("")    

def log(*values, **options):
    print("values :", values)
    print("options:", options)
 
log("start")
log("waypoint", 3, 4.5)
log("alert", level="high", retries=2)
log()