# Welcome to my Trivia program!
done = False
while not done:
    print("My Menu")
    print("S - Start Game")
    print("Q - Quit Game")
    choice = input("Choice: ")
    if choice == "S":
        print("Starting Game!")
    elif choice == "Q":
        print("Thanks for playing!")
        done = True
    else:
        print("Invalid, try again!")
