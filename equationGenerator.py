import random
import languageConverter as lc

def generateRandomNumber():
    return random.randrange(16, 39)

def generateEquationForNumber(number: int):
    if (number > 20):
        return generateThreePartEquation(number)
    return generateTwoPartEquation(number)


def generateTextEquationForNumber(number,language):
    if number > 30:
        return createFourSegmentEquation(number,language)
    elif number > 22:
        return createThreeSegmentEquation(number,language)
    else:
        return createTwoSegmentEquation(number,language)
    
def createFourSegmentEquation(number: int,language:str):
    first, second, third, fourth = splitNumberInFour(number)
    return f"{lc.convertIntToLanguage(first,language)} + {lc.convertIntToLanguage(second,language)} + {lc.convertIntToLanguage(third,language)} + {lc.convertIntToLanguage(fourth,language)} = "

def createThreeSegmentEquation(number: int,language:str):
    first, second, third = splitNumberInThree(number)
    return f"{lc.convertIntToLanguage(first,language)} + {lc.convertIntToLanguage(second,language)} + {lc.convertIntToLanguage(third,language)} = "

def createTwoSegmentEquation(number: int,language:str):
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

def generateRandomNumberMaxedAt(max: int):
    if (max > 50):
        print("He is only a child you monster, changing max to 40")
        max = 40
    min = round((0.25*max), 0)
    return random.randrange(min, max)

def generateEquation(textSelected, languageSelected):
    number = generateRandomNumber()
    equation = ""
    if textSelected:
        equation = generateTextEquationForNumber(number,languageSelected)
    else:
        equation = generateEquationForNumber(number)
    return equation, number
    ...