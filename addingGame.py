import random
import languageConverter as lc

runAgain = True
questionsAsked = 0
equations = []

def main():
    runInfinite()
    logOutAllGames()

def runOnce():
    global questionsAsked
    number = generateRandomNumner()
    equation = generateEquationForNumber(number)
    # textEquation = generateTextEquationForNumber(number)

    
    runQuestion(equation,number)
    questionsAsked = questionsAsked+1

def runOnceOld():
    number = generateRandomNumner()
    equation = generateEquationForNumber(number)
    # textEquation = generateTextEquationForNumber(number)
    runQuestion(equation,number)

def runInfinite():
    global questionsAsked
    global runAgain
    while runAgain:
        if questionsAsked==0:
            runOnce()
        choice = get_choice('play again? ')
        if choice=="n" or choice=="no":
            runAgain = False
        else:
            runOnce()


def logOutAllGames():
    global equations
    for index,equation in enumerate(equations):
        print(f"{index+1} =>    {equation}")

def runInfiniteOld():
    global runAgain
    while runAgain:
        choice = get_choice('play again? ')
        if choice=="n" or choice=="no":
            runAgain = False
        else:
            runOnce()
      
            
def generateRandomNumner():
    return random.randrange(16,35)

# def generateTextEquationForNumber(number):
#     if number > 28:
#         return createFourSegmentEquation(number)
#     if number > 28:
#         return createthreeSegmentEquation(number)
#     return createTwoSegmentEquation(number)
def generateEquationForNumber(number:int):
    if(number>20):
       return generateThreePartEquation(number)
    return generateTwoPartEquation(number)

def createFourSegmentEquation(number:int):
    first = random.randrange(5,12)
    second = random.randrange(5,number-first)
    third = random.randrange(5,number-second-first)
    fourth = number-first-second-third

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
    global equations
   
    while(True):
        try:
            result = get_int(equarion)
            if result==number:
                equations.append(f"{equarion}{result}")
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