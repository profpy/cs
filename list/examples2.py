youtube = [10, 23, 13, 15, 11]
done = False
while not done:
    print("Menu")
    print("E1 - Example 1")
    print("E2 - Example 2")
    print("E3 - Example 3")
    print("E4 - Example 4")
    print("E5 - Example 5")
    print("Q - Quit")
    choice = input("Choose: ")
    if choice == "E1":
        print("Index\tElement")
        for i in range(len(youtube)):
            print(i,"\t",youtube[i])
    elif choice == "E2":
        print("Max:",max(youtube))
        print("Min:",min(youtube))
        print("Sum:",sum(youtube))
    elif choice == "E3":
        num = int(input("Number: "))
        if num in youtube:
            print("Number is in list")
        else:
            print("Number is not in list")
    elif choice == "E4":
        youtube.insert(0,20)
        youtube.pop()
        youtube.insert(2,30)
        youtube.append(50)
        print("Index\tElement")
        for i in range(len(youtube)):
            print(i,"\t",youtube[i])
    elif choice == "E5":
        youtube.sort()
        print("Index\tElement")
        for i in range(len(youtube)):
            print(i,"\t",youtube[i])
    elif choice == "Q":
        print("Quitting!!")
        done = True
