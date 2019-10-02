'''
Spyder Editor

This is a temporary script file.
'''


def getNumberFromUser():
    '''
    User will enter a validated number
    input: none
    output: a valid number
    we need to do two things:
        1. don't crash
        2. loop until valid input
    '''
    # loop with a flag
    validInput = False
    while validInput == False:
        num = int(input())
        if num > 0:
            validInput = True
        else:
            print("Please input a positive number")
    return num

def main():
    '''test user input with addition'''
    print("Enter a number: ")
    num1 = getNumberFromUser()
    
    print("Enter another number: ")
    num2 = getNumberFromUser()
    
    print("This sum is: ", num1+num2)
    
main()