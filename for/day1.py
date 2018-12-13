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
        for i in range(5):
            print(i)
    elif choice == "E2":
        name = input("What's your name? ")
        for i in range(5):
            print(name)
    elif choice == "E3":
        sum = 0
        for i in range(3):
            num = int(input("Number: "))
            sum = sum + num
        print("Sum:",sum)
    elif choice == "E4":
        print("Number\tSquared")
        for i in range(11):
            print(i,"\t",i**2)
    elif choice == "Q":
        print("Quitting!!")
        done = True
