done = False
while not done:
    print("Menu")
    print("E1 - Example 1")
    print("E2 - Example 2")
    print("E3 - Example 3")
    print("E4 - Example 4")
    print("Q - Quit")
    choice = input("Choose: ")
    if choice == "E1":
        for x in range(1,7):
            print(x)
    elif choice == "E2":
        print("Number\tSquared")
        for x in range(-5,6):
            print(x,"\t",x**2)
    elif choice == "E3":
        count = 0
        min = int(input("Min: "))
        max = int(input("Max: "))
        divisible = int(input("Divisible: "))
        for x in range(min,max):
            if x % divisible == 0:
                count = count + 1
        print("Count:",count)
    elif choice == "E4":
        for x in range(5):
            num = int(input("Number: "))
            if x == 2:
                third = num
        print("Third Number:",third)
    elif choice == "Q":
        print("Quitting!!")
        done = True
