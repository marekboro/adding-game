import sys
import random
import languageConverter as lc
from graphics import *
import equationGenerator as eqGen

runAgain = True
questionsAsked = 0
equations = []
argsProvided = False
maxRounds: int
textSelected = False
languageSelected= "English"

def main(input: list[str]):
    checkArgs(input)
    runGames()
    logOutAllGames()


def checkArgs(input: list[str]):
    global argsProvided
    global maxRounds
    global textSelected
    global languageSelected
    input.remove(input[0])
    if int(input.__len__()) > 0:
        argsProvided = True
        textSelected = False
        try:
            maxRounds = int(input[0])
        except ValueError:
            print("max runs for game cannot be a string")
            sys.exit()
        if maxRounds < 1:
            print("max runs cannot be 0 or less")
            sys.exit()
    if int(input.__len__()) > 1:
        textSelected = True
        languageSelected = lc.verifiedLanguage(input[1])

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

def runOnce():
    global textSelected
    global languageSelected
    number = eqGen.generateRandomNumber()
    if textSelected==True:
        textEquation = eqGen.generateTextEquationForNumber(number,languageSelected)
        runQuestion(textEquation, number)
    else:
        equation = eqGen.generateEquationForNumber(number)
        runQuestion(equation, number)
         
def runTimes(maxRounds: int):
    global questionsAsked
    global runAgain
    roundsleft = maxRounds
    while runAgain and roundsleft >0:
        runOnce()
        roundsleft -=1
        if roundsleft >0:
            runAgain = checkIfRunAgain()
            
def runInfinite():
    global questionsAsked
    global runAgain
    while runAgain:
        runOnce()
        runAgain = checkIfRunAgain()




def checkIfRunAgain():
    choice = get_choice('play again? ')
    return choice != 'n' and choice != 'no'

def get_choice(prompt):
    while (True):
        try:
            return input(prompt)
        except ValueError:
            pass
    

def runQuestion(equarion: str, number: int):
    global equations
    global questionsAsked

    # ##
    # maxFontSize = 36
    # equationWidth = (equarion.__len__()*maxFontSize)
    # entryWidth = maxFontSize*2
    # windowWidth = equationWidth + entryWidth + maxFontSize
    # windowHeight= 2*maxFontSize

    # gameWindow = GraphWin("Adding Game",windowWidth,windowHeight)
    # gameWindow.setBackground("white")

    # point = Point(int(equationWidth),int(maxFontSize))
    # textToDraw = Text(point,equarion)
   
    # circle = Circle(  Point(int(equationWidth),int(maxFontSize)),10  )##.setFill("red")
    # # circle = Circle(Point(50,50), 10)
    # # c.draw(gameWindow)
    # textToDraw.setSize(maxFontSize)
    # entry = Entry(Point(windowWidth+maxFontSize,maxFontSize),4).setSize(maxFontSize)
    # # gamescreen = [textToDraw,entry]
    # gamescreen = [textToDraw,circle]
    # for element in gamescreen:
    #     element.draw(gameWindow)
    
    ##
    while (True):
        try:
            result = get_int(equarion)
        except ValueError:
            pass

        if result == number:
            questionsAsked = questionsAsked+1
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

def logOutAllGames():
    global equations
    for index, equation in enumerate(equations):
        print(f"{index+1} =>    {equation}")

if __name__ == "__main__":
    main(sys.argv)
