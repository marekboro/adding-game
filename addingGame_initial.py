import random

runAgain = True

def main():
    runOnce()
    runInfinite()


def runOnce():
    number = generateRandomNumner()
    equation = generateEquationForNumber(number)
    runQuestion(equation,number)


def runInfinite():
    global runAgain
    while runAgain:
        choice = get_choice('play again? ')
        if choice=="n" or choice=="no":
            runAgain = False
        else:
            runOnce()
      
            
def generateRandomNumner():
    return random.randrange(16,35)

def generateEquationForNumber(number:int):
    if(number>20):
       return generateThreePartEquation(number)
    return generateTwoPartEquation(number)

def generateThreePartEquation(number:int):
    first = random.randrange(5,12)
    second = random.randrange(5,number-first)
    third = number-first-second
    return f"{first} + {second} + {third} = "

def generateTwoPartEquation(number:int):
    first = random.randrange(7,14)
    second = number-first
    return f"{first} + {second} = "

def runQuestion(equarion:str,number:int):
    while(True):
        try:
            result = get_int(equarion)
            if result==number:
                print("Correct!")
                return "next"
        except:
            pass


def get_int(prompt):
    while(True):
        try:
            return int(input(prompt))
        except ValueError:
            pass

def get_choice(prompt):
    while(True):
        try:
            return input(prompt)
        except ValueError:
            pass

main()