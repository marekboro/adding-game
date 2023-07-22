import random

runAgain = True

def main():
   
    # print(createNumberAsStringInEnglish(33))
    print(createNumberAsStringInLanguage("English",174))
    print(createNumberAsStringInLanguage("Polish",199))
    # print(createNumberAsStringInLanguage("Error",22))
    # runOnce()
    # runInfinite()


def runOnce():
    number = generateRandomNumner()
    equation = generateEquationForNumber(number)
    # textEquation = generateTextEquationForNumber(number)
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

numbersAsStringEnglish = {0:"Zero",1:"One",2:"Two",3:"Tree",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thir-teen",14:"Four-teen",15:"Fif-teen",16:"Six-teen",17:"Seven-teen",18:"Eigh-teen",19:"Nine-teen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixrty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred"}
numbersAsStringPolish = {0:"Zero",1:"Jeden",2:"Dwa",3:"Trzy",4:"Cztery",5:"Pięć",6:"Sześć",7:"Siedem",8:"Osiem",9:"Dziewięć",10:"Dziesięć",11:"Jedenaście",12:"Dwanaście",13:"Trzynaście",14:"Czternaście",15:"Piętnaście",16:"Szesnaście",17:"Siedemnaście",18:"Osiemnaście",19:"Dziewiętnaście",20:"DWAdzieścia",30:"TRZYdzieści",40:"Czterdzieści",50:"PIĘĆdziesiąt",60:"SZEŚĆdziesiąt",70:"SIEDEMdziesiąt",80:"OSIEMdziesiąt",90:"DZIEWIĘĆdziesiąt",100:"Sto"}
joiningStatementPolish = {"and":""}
joiningStatementEnglish = {"and":"and"}
numbersAsStrings = {"Polish":numbersAsStringPolish,"English":numbersAsStringEnglish}
joiningStrings = {"Polish":joiningStatementPolish,"English":joiningStatementEnglish}

def getLanguageJoinString(language:str):
    return joiningStrings[language]

def getLanguageString(language:str):
    keys = numbersAsStrings.keys()
    if keys.__contains__(language):
        return numbersAsStrings[language]
    else:
        
        return numbersAsStrings["English"]
                                
    # if language == "Polish":
    #     return numbersAsStringPolish
    # else:
    #     return numbersAsStringEnglish

def createNumberAsStringInLanguage(language:str,number:int):
    language = verifiedLanguage(language)
    numberLength = number.__str__().__len__()
    if(numberLength==3):
        leadingDigit = (int)(number.__str__()[0])
        if language=="Polish":
            return f"{getLanguageString(language)[100]} {getLanguageJoinString(language)['and']}{create2DigitNumberAsStringInLanguage(language,number-(100*leadingDigit))}"
        else:
            return f"{getLanguageString(language)[leadingDigit]} {getLanguageString(language)[100]} {getLanguageJoinString(language)['and']} {create2DigitNumberAsStringInLanguage(language,number-(100*leadingDigit))}"
    else: 
        return create2DigitNumberAsStringInLanguage(language,number)
    
    # if number>20:
    #     return f"{getLanguageString(language)[20]} {getLanguageString(language)[number-20]}"
    # return f"{getLanguageString(language)[number]}"

def create2DigitNumberAsStringInLanguage(language:str,number:int):
    leadingDigit = (int)(number.__str__()[0])
    if number>20:
        return f"{getLanguageString(language)[10*leadingDigit]} {getLanguageString(language)[number-(10*leadingDigit)]}"
    else:
        return f"{getLanguageString(language)[number]}"


def verifiedLanguage(languageRequested:str):
    if numbersAsStrings.keys().__contains__(languageRequested):
        return languageRequested
    else:
         defaultLanguage = "English"
         print(f"{languageRequested} not supported, {defaultLanguage} used")
         return defaultLanguage


# def createNumberAsStringInEnglish(number:int):
#     if number>20:
#         return f"{numbersAsStringEnglish[20]} {numbersAsStringEnglish[number-20]}"
#     return f"{numbersAsStringEnglish[number]}"

main()