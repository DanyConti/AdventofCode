# File management
PATH = "/home/dany/Documents/Coding/AdventOfCode/2024/4/"
INPUT = "input.txt"
FILE = PATH + INPUT

# Costants
WORD = ['X', 'M', 'A', 'S']
STARTING = WORD[0]
DIRECTION = [
    (-1, -1), (-1, 0), (-1, 1),   # high-left, high, high-right
    (0, -1),          (0, 1),      # left, right
    (1, -1),  (1, 0), (1, 1)       # down-left, down, down-right
]

# Functions
def readingFile():
    with open(FILE, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        
    return lines

# Main
lines = readingFile()

# Variables
rowLenght = len(lines)
colLenght = len(lines[0])

result = 0

for vertical in range(colLenght):
    print(vertical+1, ":")
    for horizontal in range(rowLenght):
        if lines[vertical][horizontal] == STARTING:
            for i in DIRECTION:
                dy, dx = i
                
                cycle = 0
                for j in range(len(WORD)):
                    x = j*dx + horizontal
                    y = j*dy + vertical
                    
                    if x >= 0 and x < rowLenght and y >= 0 and y < colLenght:
                        if lines[y][x] == WORD[j]:
                            cycle += 1
                
                if (cycle == len(WORD)):
                    print("found:", dy, dx)
                    result += 1
    print("-------------")
    
print("Result:", result)