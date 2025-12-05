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


# To understand
ranges.sort(key=lambda x: x[0])

merged = []

for start, end in ranges:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

count = 0
for i in merged:
    count += i[1] - i[0] + 1

print("Result", count)