# File management
PATH = "/home/dany/Documents/Coding/AdventOfCode/2024/2/"
INPUT = "input.txt"

FILE = PATH + INPUT

rows = 10

row = 0

def actalChecking(matrix):
    lenght = len(matrix)
    MAX = 3
    
    up = 0
    down = 0
    
    for i in range(lenght-1):
        if matrix[i] > matrix[i+1]:
            if matrix[i] - matrix[i+1] <= MAX:
                    down += 1

        elif matrix[i] < matrix[i+1]:
                if matrix[i+1] - matrix[i] <= MAX:
                    up += 1
                    
    out = isSafe(up, down, lenght)
    return out

def isSafe(up, down, columnNumber):
    out = False
    
    if up > down:
        if up == columnNumber - 1:
            out = True
    elif down > up:
        if down == columnNumber - 1:
            out = True
        
    return out

def checking(matrix):
    lenght = len(matrix)
    cycleJ = 0
    
    out = actalChecking(matrix)
    if out == False:
        secondary = [x for x in range(lenght-1)]
        for i in range(lenght): #Ciclo per ogni elemento di matrix
            
            cycleJ = 0
            for j in range(lenght):
                if i != j:
                    secondary[cycleJ] = matrix[j]
                    cycleJ += 1

            out = actalChecking(secondary)
            if out != False:
                print("lorem")
                break

    return out

with open(FILE, "r", ) as f:
    cols = len(f.readlines())
    f.seek(0)
    
    number = []
    
    for line in f:
        elements = [int(x) for x in line.split()]
        number.append(elements)
        row += 1

result = 0
for i in range(row):
    if checking(number[i]):
        print(number[i])
        result += 1
        
print("Result:", result)