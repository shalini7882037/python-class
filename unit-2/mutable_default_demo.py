def add_waypoint(wp, route=None): #here we use initialise None to route, so that we will be able to create separate list for each parameters passed
    if route is None: # since we've used None, the parameters passed will not be merged
        route = []
    route.append(wp)
    return route
 
r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)
