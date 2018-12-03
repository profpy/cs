# Example 1
d = {"Kaci":"Paterson", "Jonathan":"Paterson", "Grant":"Haledon"}
for key in d:
    print("Where does",key,"live?")
    town = input(":: ")
    if town == d[key]:
        print("Correct!")
    else:
        print("Incorrect!")

# Example 2
d = {"Kaci":"Paterson", "Jonathan":"Paterson", "Grant":"Haledon"}
for key in d:
    print("Where does",key,"live?")
    town = input(":: ")
    if town.lower() == d[key].lower():
        print("Correct!")
    else:
        print("Incorrect!")

# Example 3
d = {"Kaci":"Paterson", "Jonathan":"Paterson", "Grant":"Haledon"}
for key in d:
    print("Where does",key,"live?")
    town = input(":: ")
    if town.lower.strip() == d[key].lower():
        print("Correct!")
    else:
        print("Incorrect!")

# Example 4
d = {"Kaci":"Paterson", "Jonathan":"Paterson", "Grant":"Haledon"}
for key in d:
    print("Where does",key,"live?")
    town = input(":: ")
    if town.lower.strip() == d[key].lower():
        print("Correct!")
    else:
        print("Incorrect!")
friend = input("Name: ").title()
town = input("Town: ").title()
d[friend] = town
print(d)
