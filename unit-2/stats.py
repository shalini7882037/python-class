def stats(values):
    """Return mean, minimum and maximum of a list."""
    return sum(values) / len(values), min(values), max(values)
 
readings = [22.5, 23.1, 21.8, 24.0, 22.9]
mean, lo, hi = stats(readings)
print(f"mean={mean:.2f}  min={lo}  max={hi}")
 
packed = stats(readings)
print("as a tuple:", packed, type(packed))
print("")
print("")
def greet(name):
    print("Hello", name)
 
result = greet("Alpha")
print("returned:", result)
print("type    :", type(result))
print("")
print("")
def safe_divide(a, b):
    if b == 0:
        return None            
    return a / b
 
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print("")
print("")
def add_reading(data, value):
    data.append(value)          
readings = [10, 20]
add_reading(readings, 30)
print("caller list is now:", readings)
 
def rebind(data):
    data = [99]                 
    return data
 
readings2 = [10, 20]
rebind(readings2)
print("caller list unchanged:", readings2)
