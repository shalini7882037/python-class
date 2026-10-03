import random
random.seed(42)                      
print(random.randint(1, 100))
print(round(random.uniform(20.0, 30.0), 2))
print(random.choice(["Alpha", "Beta", "Gamma"]))
noisy = [round(25 + random.gauss(0, 0.5), 2) for _ in range(5)]
print("simulated sensor:", noisy)
