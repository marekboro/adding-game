import sys
import _thread
import random
import languageConverter as lc

runAgain = True
questionsAsked = 0
equations = []
argsProvided = False
maxRounds: int

def main(input: list[str]):
    checkArgs(input)
    runGames()
    logOutAllGames()

def checkArgs(input: list[str]):
    global argsProvided
    global maxRounds
    input.remove(input[0])
    if int(input.__len__()) > 0:
        argsProvided = True
        try:
            maxRounds = int(input[0])
        except ValueError:
            print("max runs for game cannot be a string")
            sys.exit()
        if maxRounds < 1:
            print("max runs cannot be 0 or less")
            sys.exit()

def runGames():
    global argsProvided
    global maxRounds
    if argsProvided:
        if maxRounds == 1:
            runOnce()
        else:
            runTimes(maxRounds)
    else:
        runInfinite()

def runTimes(maxRounds: int):
    global questionsAsked
    global runAgain

    while runAgain and questionsAsked <= maxRounds:
        if questionsAsked == 0:
            runOnce()
        choice = get_choice('play again? ')
        if choice == "n" or choice == "no":
            runAgain = False
        else:
            runOnce()

def runOnce():
    global questionsAsked
    number = generateRandomNumber()
    # equation = generateEquationForNumber(number)
    # runQuestion(equation, number)
    textEquation = generateTextEquationForNumber(number)
    runQuestion(textEquation, number)

    questionsAsked = questionsAsked+1

def runInfinite():
    global questionsAsked
    global runAgain
    while runAgain:
        if questionsAsked == 0:
            runOnce()
        choice = get_choice('play again? ')
        checkExit(choice)
        if choice == "n" or choice == "no":
            runAgain = False
        else:
            runOnce()

def logOutAllGames():
    global equations
    for index, equation in enumerate(equations):
        print(f"{index+1} =>    {equation}")


def generateRandomNumber():
    return random.randrange(16, 39)


def generateRandomNumberMaxedAt(max: int):
    if (max > 50):
        print("He is only a child you monster, changing max to 40")
        max = 40
    min = round((0.25*max), 0)
    return random.randrange(min, max)

def generateTextEquationForNumber(number):
    if number > 30:
        return createFourSegmentEquation(number)
    elif number > 22:
        return createThreeSegmentEquation(number)
    else:
        return createTwoSegmentEquation(number)


def generateEquationForNumber(number: int):
    if (number > 20):
        return generateThreePartEquation(number)
    return generateTwoPartEquation(number)


def createFourSegmentEquation(number: int):
    language = "English"
    first, second, third, fourth = splitNumberInFour(number)
    return f"{lc.convertIntToLanguage(first,language)} + {lc.convertIntToLanguage(second,language)} + {lc.convertIntToLanguage(third,language)} + {lc.convertIntToLanguage(fourth,language)} = "

def createThreeSegmentEquation(number: int):
    language = "English"
    first, second, third = splitNumberInThree(number)
    return f"{lc.convertIntToLanguage(first,language)} + {lc.convertIntToLanguage(second,language)} + {lc.convertIntToLanguage(third,language)} = "

def createTwoSegmentEquation(number: int):
    language = "English"
    first, second = splitNumberInTwo(number)
    return f"{lc.convertIntToLanguage(first,language)} + {lc.convertIntToLanguage(second,language)} = "

def splitNumberInTwo(number:int):
    radical = random.randrange(1,int(number/5)+1)
    first = int(number/2)+radical
    second = number-first
    return first, second

def splitNumberInThree(number:int):
    radical = random.randrange(1,int(number/4))
    first = int(number/2)-radical
    second, third = splitNumberInTwo(number-first)
    return first, second, third

def splitNumberInFour(number:int):
    radical = random.randrange(1,int(number/4))
    first = int(number/2)-radical
    second, third, fourth = splitNumberInThree(number-first)
    return first, second, third, fourth


def generateThreePartEquation(number: int):
    first = random.randrange(5, 12)
    second = random.randrange(5, number-first)
    third = number-first-second
    return f"{first} + {second} + {third} = "


def generateTwoPartEquation(number: int):
    first = random.randrange(7, 14)
    second = number-first
    return f"{first} + {second} = "


def runQuestion(equarion: str, number: int):
    global equations

    while (True):
        try:
            result = get_int(equarion)
        except ValueError:
            pass

        if result == number:
            equations.append(f"{equarion}{result}")
            print("Correct!")
            return "next"
        
def get_int(prompt):
    while (True):
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            checkExit(userInput)
            pass

def checkExit(someString: str):
    if someString == "q" or someString == "quit":
        sys.exit()  
    else:
        return someString


def get_choice(prompt):
    while (True):
        try:
            return input(prompt)
        except ValueError:
            pass


if __name__ == "__main__":
    main(sys.argv)
