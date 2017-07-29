# Basic Python program
x = 1
while x == 1: # allows the user to input a number for c and d
    c = int(input("enter a number: ")) 
    d = int(input("enter a number: "))
#conditionals for the numbers that the user chooses
    if (c * d < 10):
        print("Too small to print")
    elif (c * d > 100000):
        print ("Too large to print")
    else:
        print("The value of c and d being multiplied together is " + str(c * d))

#independent from the code above
#Prints fibonacci numbers below 100
    a, b = 0, 1
    while b < 1000:
        print (b)
        a, b = b, a+b
    y = input("type x to exit")
    if (y == "x"):
        x = 0
print("Hasta luego")



