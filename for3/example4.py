done = False
while not done:
    print("Menu")
    print("E1 - Example 1")
    print("E2 - Example 2")
    print("E3 - Example 3")
    print("Q - Quit")
    choice = input("Choose: ")
    if choice == "E1":
        for x in range(2,10+1,2):
            print(x)
    elif choice == "E2":
        for x in range(10,-1,-1):
            print(x)
    elif choice == "E3":
        print("Year\tIncrease in mm")
        rise = 0
        for x in range(2018,2044,5):
            print(x,"\t",rise*8.5)
            rise = rise + 1
    elif choice == "Q":
        print("Quitting!!")
        done = True
