print("Example 1")
ride = 0
sum = 0
while ride >= 0:
    ride = int(input("How long? "))
    if ride > 0:
        sum = sum + ride
print("Sum:",sum)

print("Example 2")
ride = 0
sum = 0
x = 0
while ride >= 0:
    ride = int(input("How long? "))
    if ride > 0:
        sum = sum + ride
        x = x + 1
print("Average:",sum/x)

print("Example 3")
ride = 0
max = 0
x = 0
while ride >= 0:
    ride = int(input("How long? "))
    if ride > 0 and x == 0:
        max = ride
    else:
        if ride > max:
            max = ride
    x = x + 1
print("Max:",max)
