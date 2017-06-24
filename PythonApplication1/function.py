def getValidInput():
    isValid = False
    while isValid == False:
        print('Enter as many expressions as you want, followed by a {space}: +, -, /, *, **, or sqrt')
        answer = input()
        items = answer.split(' ')
        for a in items:
            if (a != '+') and (a != '-') and (a != '*') and (a != '**') and (a != '/') and (a != 'sqrt'):
                print("Invalid input (" + a + "), type again...")
                isValid = False
                break
            else:
                isValid = True
    return answer

print ("The answer is: " + getValidInput())