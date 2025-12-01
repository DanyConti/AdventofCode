PATH =  "1/"
FILE = PATH + "try.txt"

MAX = 99
MIN = 0

RIGHT = "R"
LEFT = "L"

REST = 1
LETTER = 0

index = 50
count = 0

# Functions
def forward(value):
    global index
    index += value
    
def back(value):
    global index
    index -= value

prova = 0

# Main
with open(FILE, "r") as f:
    file = f.readlines()

for line in file:
    line = line.strip()
    
    if line[LETTER] == RIGHT:
        forward(int(line[REST:]))
    elif line[LETTER] == LEFT:
        back(int(line[REST:]))
        
    index = index % (MAX + 1)
    
    if index == MIN:
        count += 1
        
print("count " + str(count))