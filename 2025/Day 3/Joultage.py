PATH =  "2025/Day 3/"
FILE = PATH + "input.txt"

count = []

# Functions
def printSeparator():
    print("+--------------+")

# Main
with open(FILE, "r") as f:
    file = f.readlines()

for line in file:
    line = line.strip("\n")
    print(line)
    
    length = len(line)
    numbers = [int(x) for x in line]
    higher = 0
    high = 0
    
    for i in numbers[:-1]:
        if i > higher:
            higher = i
        
    index = numbers.index(higher)
    for i in numbers[index+1:]:
        if i > high:
            high = i
            
    count.append(int(str(higher) + str(high)))
            
    print("numbers " + str(higher) + str(high))
    printSeparator()

sum = 0
for i in count:
    print("n: " + str(i))
    sum += i
    
print("SUM: " + str(sum))