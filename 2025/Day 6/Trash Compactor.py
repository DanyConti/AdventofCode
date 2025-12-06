import operator

PATH =  "2025/Day 6/"
FILE = PATH + "input.txt"

operations = {
    "+": operator.add,
    "*": operator.mul
}

def printingSeparator():
    print("+----------------------+")

# Main
with open(FILE, "r") as f:
    file = f.readlines()
    
numbers = [line.split() for line in file[:-1]]
operators = file[-1].split()

lenRows = len(numbers)
lenCols = len(numbers[0])

result = 0

for i in range(lenCols):
    
    count = int(numbers[0][i])
    
    for z in range(1, lenRows):
        count = operations[operators[i]](count, int(numbers[z][i]))
        
    result += count 
    
print("Result:", result)