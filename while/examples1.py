print("Example 1")
x = 0
name = input("What is your name? ")
while x < 5:
    print(name)
    x = x + 1

print("Example 2")
x = 1
while x <= 5:
    print(x)
    x = x + 1

print("Example 3")
x = 1
while x < 100:
    print(x)
    x = x + 2

print("Example 4")
x = 1
sum = 0
while x <= 10:
    sum = sum + x
    x = x + 1
print(sum)

print("Example 5")
x = 0
sum = 0
while x < 3:
    num = int(input("Number: "))
    sum = sum + num
    x = x + 1
print("Sum:", sum)
