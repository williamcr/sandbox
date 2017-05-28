"""
places = ["Sydney","New Zealand","Manila","Taipei","Hong Kong"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
"""

mylist = ["No", "God", "Please", "NO"]
print(len(mylist))
print(sorted(mylist))
print(sorted(mylist, reverse=True))
print(mylist)
mylist.sort(reverse = True)
print(mylist)



people = ["Guy", "Puy", "Eevee"]
for items in people:
    print(items)
print (str(len(people)) + " people are coming to dinner tonight")


input()

print (people[0] + ", you are invited to a dinner at my place at 6:00 p.m.")
print (people[1] + ", you are invited to a dinner at my place at 6:00 p.m.")
print (people[2] + ", you are invited to a dinner at my place at 6:00 p.m.")

input()

print ("I heard that, unfortunately, Puy will not be arriving to dinner tonight.")
del people[1]
print (people)
input()

print (people[0] + ": As you may have heard, Puy will not be coming. It will only be you and Eevee. I hope you will still enjoy your dinner!")
print (people [1] + ": As you may have heard, Puy will not be coming. It will only be you and Guy. I hope you will still enjoy your dinner!")

input()

print ("I have found a bigger table to accodomate more guests!")
people.insert(0, "Scout")
people.insert(1, "Heavy")
people.append("Engi")
print(people) 

print(people[0] + ": You are invited to my dinner at 6:00 p.m.!")
print(people[1] + ": You are invited to my dinner at 6:00 p.m.!")
print(people[4] + ": You are invited to my dinner at 6:00 p.m.!")

print("Since the new dinner table will not be arriving in time (thanks UPS for 'losing' that table) I can only accomadate 2 guests for my dinner.")
print(people)
input()

popped_guy = people.pop(0)
print(popped_guy + ", I am sorry, but you cannot come to my dinner")
popped_guy1 = people.pop(0)
print(popped_guy1 + ", I am sorry, but you cannot come to my dinner")
popped_guy2 = people.pop()
print(popped_guy2 + ", I am sorry, but you cannot come to my dinner")

input()

print(people[0] + ", you are still invited to my dinner at 6:00 p.m")
print(people[1] + ", you are still invited to my dinner at 6:00 p.m")

del people[0]
del people[0]
print(people)

input()

print(".")
input()
print(".")
input()
print(".")
input()

x = 1
while x == 1:
    response = input("Hello! I am a random computer program that will put a virus on your computer if you do not talk to me! What is your name?")
    print ("Nice to meet you, " + response.strip() + "!")

    response1 = input("How are you, " + response + "?")

    if (response1.strip() == "good" or response1.strip() == "ok"):
        print("Good for you!")
    elif(response1.strip() == "bad" or response1.strip() == "not good" or response1.strip() == "not great"):
        print("I hope you get better soon, " + response1.strip())
    else:
        print("...your feelings confuse me.")
    
    response2 = input("Do you want a virus on your computer? (Yes/No)")
    
    if (response2.lower() == "yes"):
        print("Ok, here you go!")
        
        print(".")
        
        print(".")
        
        print("It failed. Dang it.")
        x = 0
    elif (response2.lower() == "no"):
        print("ok")
        x = 0


