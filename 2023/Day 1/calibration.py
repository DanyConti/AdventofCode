PATH =  "2023/Day 1/"
FILE = PATH + "input.txt"

numbers = []
firstNumber = 0
lastNumber = 0
box = 0

# Main
with open(FILE, "r") as f:
    file = f.readlines()
    
for line in file:
    line = line.strip()
    index = 0
    numeric = 0
    for char in line:
        if char.isnumeric():
            numeric += 1
            if index == 0:
                firstNumber = char
                index += 1
            else:
                box = char
    if numeric > 1:
        lastNumber = box
    else:
        lastNumber = firstNumber
    numbers.append(int(firstNumber + lastNumber))
    print(firstNumber + lastNumber)

result = 0
for i in numbers:
    result += i
    
print(result)