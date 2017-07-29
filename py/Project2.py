# Q&A-type program
x = 1
# Tells the program to run as long as x is equal to 1
while x == 1:

# Program asks user a question. The user can respond with anything.

    print ("Hello. What is your name?")
    response = input()

# Program responds using the user's input and asks the user how they are.

    
    print ("Hello, " + response + ". How are you today? (good or bad)")
    response1 = input()
    
# Conditionals for the user response.

    
    if (response1 == "good"):
        print ("Good for you!")
    elif (response1 == "bad"):
        print ("I hope you get better soon, " + response)
    else:
        print ("Your feelings confuse me :)")

# Program asks the user how old they are.
# (Bug) The user can only respond using a number; otherwise, it will cause
# an error and the program will terminate.
       
    print ("How old are you? (Please enter a number).")
    response2 = int(input())

# Conditionals for the User response.   
    
    if (response2 < 0):
        print ("You are too young to even exist!")
    elif (response2 < 5):
        print ("You are very young. But guess what? You will be ")
        print (response2 + 1)
        print ("in a year or less!") 
    elif (response2 > 40):
        print ("You are an old fart!")
    
    else:
        print ("That's nice")
        

# Program asks the user when they were born.
        
    print ("What year were you born in?")
    response3 = int(input())
    
# Condiitonals for the user response
    
    if (response3 < 1960):
        print("You must be an old-fashioned type of guy!")
    elif (response3 > 2000):
        print("You are a modern-er person, " + response + ".")
    else:
        print("cool.")

# As of now, this is where the program ends. The user
# can press x and hit enter in order to terminate the
# program. To restart it, the user just has to hit enter,
# and the program will restart.
        
    y = str(input("The program has terminated.Press x and hit enter to exit. If you want to restart the program, hit enter. "))
    if (y == "x"):
        x = 0
        
print ("Bye, " + response)
