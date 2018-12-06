print("Example 1")
youtuber = input("What Youtuber is this? ")
if youtuber == "VanossGaming":
    print("correct!")
else:
    print("incorrect!")

print("Example 2")
members = int(input("How many members are there in FGTeev? "))
if members == 6:
    print("Correct")
elif members > 6:
    print("Too high")
elif members < 6:
    print("Too low")

print("Example 3")
games = input("What games does Audrey play the most? ")
if games == "Fortnite":
    print("Incorrect!")
elif games == "Minecraft":
    print("mostly")
elif games == "Roblox":
    print("Mr Cheng's daughter watches Roblox too")
else:
    print("not sure")

print("Example 4")
gas = input("What type of gas do you want? ")
if gas == "regular":
    print("Regular",15*3.899)
elif gas == "plus":
    print("Plus",15*4.099)
elif gas == "premium":
    print("Premium",15*4.199)
elif gas == "diesel":
    print("Diesel",15*4.599)
else:
    print("invalid gas type")

print("Example 5")
num = int(input("Give me a number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
elif num == 0:
    print("is 0")

