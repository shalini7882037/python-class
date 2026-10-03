def factorial(n):
    if n <= 1:              
        return 1
    return n * factorial(n - 1)   
 
print(factorial(5))
print(factorial(0), factorial(1))
print("")
print("")
def factorial(n, depth=0):
    pad = "  " * depth
    print(f"{pad}factorial({n}) called")
    if n <= 1:
        print(f"{pad}-> base case returns 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(f"{pad}-> returns {result}")
    return result
 
factorial(4)
print("")
print("")
def countdown(n):
    if n <= 0:              # base case
        print("liftoff")
        return
    print(n)
    countdown(n - 1)
 
countdown(3)
