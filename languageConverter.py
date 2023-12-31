englishNumbers = {0: "Zero", 1: "One", 2: "Two", 3: "Tree", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
                  30: "Thirty", 40: "Fourty", 50: "Fifty", 60: "Sixrty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "One Hundred", 200: "Two Hundred", 300: "Three Hundred", 400: "Four Hundred", 500: "Five Hundred", 600: "Six Hundred", 700: "Seven Hundred", 800: "Eight Hundred", 900: "Nine Hundred", }
polishNumbers = {0: "Zero", 1: "Jeden", 2: "Dwa", 3: "Trzy", 4: "Cztery", 5: "Pięć", 6: "Sześć", 7: "Siedem", 8: "Osiem", 9: "Dziewięć", 10: "Dziesięć", 11: "Jedenaście", 12: "Dwanaście", 13: "Trzynaście", 14: "Czternaście", 15: "Piętnaście", 16: "Szesnaście", 17: "Siedemnaście", 18: "Osiemnaście", 19: "Dziewiętnaście",
                 20: "Dwadzieścia", 30: "Trzydzieści", 40: "Czterdzieści", 50: "Pięćdziesiąt", 60: "Sześćdziesiąt", 70: "Siedemdziesiąt", 80: "Osiemdziesiąt", 90: "Dziewięćdziesiąt", 100: "Sto", 200: "Dwieście", 300: "Trzysta", 400: "Czterysta", 500: "Pięćset", 600: "Sześćset", 700: "Siedemset", 800: "Osiemset", 900: "Dziewięćset"}
polishStatements = {"and": ""}
englishStatements = {"and": " and"}

library = {
    "Polish": {"numbers": polishNumbers, "statements": polishStatements},
    "English": {"numbers": englishNumbers, "statements": englishStatements}}


def getLanguages():
    return list(library.keys())


defaultLanguage = list(library.keys())[1]
polish = list(library.keys())[0]


def getLanguageStatements(language: str):
    return library[language]["statements"]

# provides the language specific mapping value for numbers up to 199


def getNumbersForLanguage(language: str):
    keys = library.keys()
    if keys.__contains__(language):
        return library[language]["numbers"]
    else:
        return library["English"]["numbers"]


def convertIntToLanguage(number: int, language: str):
    language = verifiedLanguage(language)
    symbol, absoluteNumber = getSignAndAbsoluteOfInt(number)
    intLength = absoluteNumber.__str__().__len__()

    if (absoluteNumber > 999):
        return (f"numbers above 999 not currently supperted in {getLanguages()}")
    if (intLength == 3):
        return f"{symbol}{convert3DigitIntToLanguage(absoluteNumber,language)}"
    else:
        return f"{symbol}{convert2DigitIntToLanguage(absoluteNumber,language)}"


def getSignAndAbsoluteOfInt(number: int):
    symbol = ""
    stringNumber = number.__str__()
    if stringNumber[0] == "-":
        symbol = "Minus"
    absoluteNumber = (int)(stringNumber.lstrip("-"))
    return symbol, absoluteNumber


def verifiedLanguage(languageRequested: str):
    if library.keys().__contains__(languageRequested):
        return languageRequested
    else:
        defaultLanguage = "English"
        print(f"{languageRequested} not supported, {defaultLanguage} used")
        return defaultLanguage


def convert3DigitIntToLanguage(number: int, language: str):
    leadingDigit = (int)(number.__str__()[0])
    return f'{getNumbersForLanguage(language)[leadingDigit*100]}{getLanguageStatements(language)["and"]} {convert2DigitIntToLanguage(number-(100*leadingDigit),language)}'


def convert2DigitIntToLanguage(number: int, language: str):
    leadingDigit = (int)(number.__str__()[0])
    if number > 20:
        return f"{getNumbersForLanguage(language)[10*leadingDigit]} {getNumbersForLanguage(language)[number-(10*leadingDigit)]}"
    else:
        return f"{getNumbersForLanguage(language)[number]}"
