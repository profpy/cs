friends = {"Sophia":"green", "Sandy":"brown", "Izzy": "brown", "Nate":"brown","Joshua":"brown"}
done = False
score = 0
while not done:
    print("Menu")
    print("D - Do Now")
    print("E1 - Example 1")
    print("E2 - Example 2")
    print("E3 - Example 3")
    print("Q - Quit")
    choice = input("Choice: ")
    if choice == "D":
        print("Do Now")
    elif choice == "Q":
        print("Quit!")
        done = True
    elif choice == "E1":
        friends["Chaya"] = "brown"
        print(len("Friends: ", friends))
    elif choice == "E2":
        score = 0
        for key in friends:
            print("What is",key,"eye color")
            eyeball = input(":: ")
            if eyeball == friends[key]:
                print("correct!")
                score = score + 1
            else:
                print("incorrect!")
    elif choice == "E3":
        print("Score:",score)
