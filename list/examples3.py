bus = [30,15,10,20,25]
food = ["hamburgers","empanadas","broccoli"]
prices = [1.25,2.40,4.30]
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
        bus.append(31)
        bus.append(35)
        bus.append(40)
        print("Index\tElement")
        for i in range(len(bus)):
            print(i,"\t",bus[i])
    elif choice == "E2":
        print("Index\tElement")
        for i in range(len(food)):
            print(i,"\t",food[i])
    elif choice == "E3":
        for i in range(len(prices)):
            print(i,"\t",prices[i])
    elif choice == "E4":
        prices[1] = 3.00
        prices[2] = 4.50
        print("Index\tElement")
        for i in range(len(prices)):
            print(i,"\t",prices[i])
    elif choice == "Q":
        print("Quitting!!")
        done = True
