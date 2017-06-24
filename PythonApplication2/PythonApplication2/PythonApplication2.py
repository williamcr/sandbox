food = ["dumplings","burger","ice cream"]
print("The first item in this list is:")
for foods1 in food[:1]:
    print(foods1)
print("The second item in my list is:")
for foods1 in food[1:2]:
    print(foods1)
print("The last item in my list is:")
for foods1 in food[2:]:
    print(foods1)
friend_food = food[:]
friend_food.append("berries")
food.append("toast")

print("My favorite foodsa are:")
for foods in food:
    print(foods)
print("My friends favorite foods are:")
for morefoods in friend_food:
    print(morefoods)






"""
newlist = []
print(newlist)
newlist.append("Guy")
newlist.append("Engineer")
newlist.append("Person")
newlist.sort(reverse=True)
print(newlist)

for people in newlist:
    print(people + ", say hello to the world" + "!\n")

pizzas = ["Pepperoni pizza", "Combo pizza", "Five-cheese pizza"]
for pizza in pizzas:
    print("I really do like meself a delicious " + pizza.title() + ".\n")
print("I really like all kinds of pizza!")

input()

pets = ["tiger", "dog", "cat"]
pets.sort()
for animals in pets:
    print("I think a " + animals.title() + " would be a good pet" + ".\n")
print("I really think any of these animals are great pets.")

input()

cubed = []
for values in range(1,101):
    cubed.append(values**3)
print(cubed)

"""
mylist = [values for values in range(1,22,2)]
print(mylist)
    