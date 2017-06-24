import math
x = 1
while x == 1:
    def add(x,y):
        return x + y;
    def subtract(x,y):
        return x - y;
    def times(x,y):
        return x * y;
    def divide(x,y):
        return x / y;
    def exponent(x,y):
        return x**y;
    def root_squared(x):
        return math.sqrt(x);
    def returnsValidResponse():
        returnsValidResponse == False
        while returnsValidResponse == False:
            pass
                        
    print("Choose the operator you want: + - * / ** sqrt")
    choice = input()
    returnsValidResponse()
    if (choice == "sqrt"):
        print("Input the number you would like to square root.")
        xNum = int(input())
        print("The square root of", xNum , "is ", root_squared(xNum))
    else: 
        print("Enter in the first number")
        fNum = int(input())
        print("Enter in the second number")
        lNum = int(input())
    

        if (choice == "+"):
            print(fNum, " + ", lNum, " = ", add(fNum,lNum))
        if (choice == "-"):
            print(fNum, " - ", lNum, " = ", subtract(fNum,lNum))
        if (choice == "*"):
            print(fNum, " * ", lNum, " = ", times(fNum,lNum))
        if (choice == "/"):
            print(fNum, " / ", lNum, " = ", divide(fNum,lNum))
        if (choice == "**"):
            print(fNum, " ** ", lNum, " = ", exponent(fNum,lNum))
    
    print()
    print("The program has terminated. Do you wish to reboot the program, or abort? Press enter to continue, or type 'N' and hit enter to abort.")
    descision = input()
    if (descision.title().strip() == "Y" or descision.title().strip() == "Yes"):
        print("The program will continue.")
        x = 1
    elif (descision.title().strip() == "N" or descision.title().strip() == "No"):
        print("Aborted")
        x = 0
        print()
