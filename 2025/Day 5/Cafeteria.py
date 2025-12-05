PATH =  "2025/Day 5/"
FILE = PATH + "input.txt"

# Main
with open(FILE, "r") as f:
    file = f.readlines()

ranges = []
numbers = []
part = 1  # 1 = range, 2 = numeri singoli
count = 0

result = 0

for line in file:
    line = line.strip()
    if line == "":
        part = 2
        continue

    if part == 1:
        # split range
        ranges.append([int(x) for x in line.split("-")])
    else:
        # singolo numero
        numbers.append(int(line))
        
for num in numbers:
    count = 0
    print("\t\tResult", result)
    for i in ranges:
        print("Number:", num, ", ranges:", i)
        if i[0] <= num <= i[1]:
            result += 1
            break

print("Result:", result)