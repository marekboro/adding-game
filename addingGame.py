import sys
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
    while runAgain and questionsAsked < maxRounds:
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
    equation = generateEquationForNumber(number)
    # textEquation = generateTextEquationForNumber(number)

    runQuestion(equation, number)
    questionsAsked = questionsAsked+1


def runOnceOld():
    number = generateRandomNumber()
    equation = generateEquationForNumber(number)
    # textEquation = generateTextEquationForNumber(number)
    runQuestion(equation, number)


def runInfinite():
    global questionsAsked
    global runAgain
    while runAgain:
        if questionsAsked == 0:
            runOnce()
        choice = get_choice('play again? ')
        if choice == "n" or choice == "no":
            runAgain = False
        else:
            runOnce()


def logOutAllGames():
    global equations
    for index, equation in enumerate(equations):
        print(f"{index+1} =>    {equation}")


def runInfiniteOld():
    global runAgain
    while runAgain:
        choice = get_choice('play again? ')
        if choice == "n" or choice == "no":
            runAgain = False
        else:
            runOnce()


def generateRandomNumber():
    return random.randrange(16, 35)


def generateRandomNumberMaxedAt(max: int):
    if (max > 50):
        print("He is only a child you monster, changing max to 40")
        max = 40
    min = round((0.25*max), 0)
    return random.randrange(min, max)
# def generateTextEquationForNumber(number):
#     if number > 28:
#         return createFourSegmentEquation(number)
#     if number > 28:
#         return createthreeSegmentEquation(number)
#     return createTwoSegmentEquation(number)


def generateEquationForNumber(number: int):
    if (number > 20):
        return generateThreePartEquation(number)
    return generateTwoPartEquation(number)


def createFourSegmentEquation(number: int):
    first = random.randrange(5, 12)
    second = random.randrange(5, number-first)
    third = random.randrange(5, number-second-first)
    fourth = number-first-second-third


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
            if result == number:
                equations.append(f"{equarion}{result}")
                print("Correct!")
                return "next"
        except:
            pass


def get_int(prompt):
    while (True):
        try:
            # return int(checkExit(input(prompt)))
            return int(input(prompt))
        except ValueError:
            pass


def checkExit(someString: str):
    if someString == "q" or "quit":
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
