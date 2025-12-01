# File management
PATH = "/home/dany/Documents/Coding/AdventOfCode/2024/4/"
INPUT = "tryInput2.txt"
FILE = PATH + INPUT

# Costants
ZERO = 0
WORD = ['M', 'A', 'S']
FOCUS = WORD[1]
DIRECTION = [
    (-1, -1), (-1, 1),   # high-left, high-right
    (1, -1), (1, 1)   # down-left, down-right
]

# Functions
def readingFile():
    with open(FILE, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        
    return lines

# Main
lines = readingFile()

# Variables
rowLenght = len(lines[0])
colLenght = len(lines)

result = 0

for vertical in range(colLenght):
    print(vertical+1, ":")
    for horizontal in range(rowLenght):
        if lines[vertical][horizontal] == FOCUS:
            print(vertical, horizontal)
            for i in DIRECTION:
                dy, dx = i
                
                cycle = 0
                for j in range(len(WORD)):
                    print(j, "-lettura:")
                    x = j*dx + horizontal
                    y = j*dy + vertical
                    
                    if x >= ZERO and x < rowLenght and y >= ZERO and y < colLenght:
                        if lines[y-1][x-1] == WORD[j]:
                            print("lettura parola:", y-1, x-1)
                            cycle += 1
                
                if (cycle == len(WORD)):
                    result += 1
    print("-------------")
    
print("Result:", result)