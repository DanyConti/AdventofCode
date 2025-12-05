PATH =  "2025/Day 4/"
FILE = PATH + "input.txt"

PRINTER = '@'
POINTER = '.'

directions = [
    (-1,-1), (-1,0), (-1,1),
    ( 0,-1),         ( 0,1),
    ( 1,-1), ( 1,0), ( 1,1)
]

# Functions
def printSeparator():
    print("+-------------------------+")
    
def ranging(dim):
    return range(len(dim))

# Main
with open(FILE, "r") as f:
    file = f.read().splitlines()
    
rows, cols = len(file), len(file[0])
number = 0

for line in range(rows):
    print("\t" + file[line])
    printSeparator()
    
    for col in range(cols):
        print("char: " + file[line][col])
        
        count = 0
        if file[line][col] == PRINTER:
            
            for dr, dc in directions:
                nextY = line + dr
                nextX = col + dc
                
                print("🔳 " + str(count))
                
                print("Direction (" + str(dr) + ", " + str(dc) + "):", end=" ")
                if 0 <= nextY < rows and 0 <= nextX < cols:
                    print("✅", end=" ")
                    if file[nextY][nextX] == PRINTER:
                        print("🖨️")
                        count += 1
                    else:
                        print("⚠️")
                else:
                    print("❌")
            
            if count < 4:
                number += 1
            print("💲 " + str(number) + " " + str(count))
            
print("\n")
print("-> Number: " + str(number))             
    