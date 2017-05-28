x = 1
while x == 1:
    name  = input("Hello! What is your name?")

    response = input("Hello, " + name.title() + ". How are you today? (Please respond good or bad)")

    if (response.strip()== "good" or response.strip() == "Good"):
        print ("Good for you!")
    elif (response.strip() == "bad" or response.strip() == "Bad"):
        print ("I hope you get better soon, " + name.title())
    else:
        print ("Your feelings confuse me.")

    response2 = int(input("When were you born?"))

    if (response2 > 2018):
        print ("You don't exist...or do you?")
    elif (response2 >= 2000):
        print ("You are quite young!")
    elif (response2 >= 1980):
        print ("You are semi-middle aged!")
    elif (response2 <= 1950):
        print ("You are an old fart!")
   
    print("If my calculations are right, then currently you are this many years old:")
    print(2017 - response2)

    response3 = str(input("Am I right? (Yes or no)"))
    
    if(response3.strip().title() == "yes"):
        print ("Cool.")
    elif(response3.strip().title() == "no"):
        print("But...But...It cannot be!")   
    else: 
        print("I don't know what you mean.")
    
