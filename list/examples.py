print("Example 1")
# youtube = []

youtube = [10, 23, 13, 15, 11, 32, 78]
print(youtube)

print("Example 2")
x = 0
print("Index\tElement")
for i in youtube:
    print(x,"\t",i)
    x = x + 1

print("Example 3")
num = int(input("Number: "))
if num in youtube:
    print(num, "is in the list")
else:
    print(num, "is not in the list")

print("Example 4")
print("Min:",min(youtube))
print("Max:",max(youtube))

print("Example 5")
youtube.pop(2)
x = 0
print("Index\tElement")
for i in youtube:
    print(x,"\t",i)
    x = x + 1

youtube.insert(2,20)
print("Index\tElement")
x = 0
for i in youtube:
    print(x,"\t",i)
    x = x + 1

print("Example 6")
youtube.sort()
print(youtube)
