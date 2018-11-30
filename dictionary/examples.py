print("Example 1")
friends = {}
friends = {"Sasha":"West Milford", "Jonathan":"Paterson", "Izzy":"Paterson","Sofia":"Little Falls","Nate":"Clifton"}
print(friends)

print("Example 2")
print("Key\tValue")
for key in friends:
    print(key,"\t",friends[key])

print("Example 3")
friends['Rita'] = "Passaic"
friends['Karla'] = "Wayne"
print("Key\tValue")
for key in friends:
    print(key,"\t",friends[key])

print("Example 4")
friends.pop("Rita")
print(len(friends), "friends left!")

print("Example 5")
print("Friends Quiz!!")
for key in friends:
    print("What town does",key,"live in: ")
    town = input(":: ")
    if town == friends[key]:
        print("correct!")
    else:
        print("incorrect!")
