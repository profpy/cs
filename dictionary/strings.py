d = {} # empty dictionary
for x in range(3):
    friend = input("Name: ")
    town = input("Town: ")
    d[friend] = town
print(d)

d = {"Kaci":"Paterson", "Jonathan":"Paterson", "Grant":"Haledon"}
for key in d:
    print("Where does",key,"live?")
    town = input(":: ")
    if town.lower().strip() == d[key].lower():
        print("Correct!")
    else:
        print("Incorrect!")
friend = input("Name: ").title()
town = input("Town: ").title()
d[friend] = town
print(d)
