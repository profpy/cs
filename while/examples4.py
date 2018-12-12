done = False
while not done:
    print("Menu")
    print("S - Start")
    print("B - Bus Ride")
    print("Q - Quit")
    choice = input(":: ")
    if choice == "S":
        print("Starting Game!")
    elif choice == "Q":
        print("Exiting Game!")
        done = True
    elif choice == "B":
        bus = int(input("How long? "))
        if bus <= 30:
            print("not long")
        else:
            print("too long")
