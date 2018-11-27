robux = int(input("Starting Robux: "))
x = int(input("How many items: "))
for i in range(0,x):
    cost = int(input("How much is item? " ))
    robux = robux - cost
print("Robux remaining:",robux)
