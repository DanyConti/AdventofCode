PATH =  "2025/Day 2/"
FILE = PATH + "input.txt"

numbers = []

# Main
with open(FILE, "r") as f:
    file = f.read()
    file = file.replace(",", "\n").splitlines()

for line in file:
    line = line.strip(",")
    first, last = map(int, line.split("-"))
    
    check = 0
    for i in range(first, last+1):
        i = str(i)
        
        length = len(i) // 2
        before = i[:length]
        after = i[length:]
        
        if before == after:
            numbers.append(int(i))

sum = 0        
for i in numbers:
    sum += i
    print("i: " + str(i))
    
print("SUM: " + str(sum))