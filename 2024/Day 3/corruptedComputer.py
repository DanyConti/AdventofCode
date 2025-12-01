# File management
PATH = "/home/dany/Documents/Coding/AdventOfCode/2024/3/"
INPUT = "input.txt"

FILE = PATH + INPUT

# Constants
MULKIND = "mul("
MULKIND_SIZE = len(MULKIND)
SEPERATOR = ","
CLOSING = ")"
DIGITS = 3

DONT = "don't()"
DO = "do()"
LEFT_BRACKET = "("
RIGHT_BRACKET = CLOSING
DONT_SIZE = len(DONT)
DO_SIZE = len(DO)

# List of mull
global firstNumbers
global secondNumbers

row = 0
col = 0
firstNumbers = 0
secondNumbers = 0

rows = 100000
cols = 2
mulList = [[0 for _ in range(cols)] for _ in range(rows)]

cycleI = 0
isDo = True

# Functions
def checkDigits(where, what):
    global breakIdea
    
    digitsReal = 0
    breakIdea = False
    
    for i in range(DIGITS):
        if breakIdea == False:
            if box[where+i].isnumeric():
                digitsReal += 1
            elif box[where+i] != what:
                breakIdea = True

            else:
                breakIdea = True
        
    return digitsReal

def checkDigitsValidity(digitsReal): 
    out = False
    if digitsReal > 0 and digitsReal <= DIGITS:
        out = True
    else:
        out = False
    
    return out

def setMullNumbers(digitsReal, where):
    global col
    global row
    
    line=''
    for j in range(digitsReal):
        line += box[where+j]
    
    mulList[col][row] = int(line)
    if row == 1:
        row = 0
    else:
        row = 1
        
def checkDo():
    global isDo
    isIt = 0
    for j in range(DONT_SIZE):
        if box[cycleI+j] == DONT[j]:
            isIt += 1
        elif box[cycleI+j] == LEFT_BRACKET:
            if isIt == (DO_SIZE - 2):
                if box[cycleI+j+1] == RIGHT_BRACKET:
                    isDo = True
        else:
            break
    
    if isIt == DONT_SIZE:
        isDo = False

    return isDo

# Scripting
with open(FILE, "r") as f:
    cycleI = 0
    
    row = 0
    for x in f:
        box = x.strip() # Stripping the line
        cycleI = 0
        for i in box:            
            isIt = 0
            isDo = checkDo()
            if isDo:
                if i == MULKIND[0]:
                    for j in range(MULKIND_SIZE):
                        if box[cycleI+j] == MULKIND[j]:
                            isIt += 1
                        if isIt == MULKIND_SIZE:
                        
                            starting = cycleI + MULKIND_SIZE
                            firstNumbers = 0
                            firstNumbers = checkDigits(starting, SEPERATOR)

                            if checkDigitsValidity(firstNumbers):
                                setMullNumbers(firstNumbers, starting)
                                beforeSeparator = starting + firstNumbers
                                
                                if box[beforeSeparator] == SEPERATOR:
                                    duringSeparator = beforeSeparator + 1
                                    secondNumbers = checkDigits(duringSeparator, CLOSING)

                                    if checkDigitsValidity(secondNumbers):
                                        afterSeparator = duringSeparator + secondNumbers
                                        closingBracket = afterSeparator + 1
                                        if box[afterSeparator] == CLOSING:
                                            setMullNumbers(secondNumbers, duringSeparator)
                                            col += 1
                                            #! print("----------------------------------")
                                            print("->", box[cycleI:closingBracket])
                                            print("----------------------------------")
            cycleI += 1
    
result = 0        
for i in range(col):
    result += mulList[i][0] * mulList[i][1]
    print(f"mul({mulList[i][0]},{mulList[i][1]}) = {result}")