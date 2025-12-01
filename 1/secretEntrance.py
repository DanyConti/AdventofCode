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
lap = 0

enough = 0

# Functions
def forward(value):
    global index
    index += value
    
def back(value):
    global index
    index -= value

def calc():
    global count
    
    value = int(line[REST:])
    lap = abs(int(value / (MAX + 1)))
    value = value % (MAX + 1)
    if lap > MIN:
        count += lap
        
    return value

# Main
with open(FILE, "r") as f:
    file = f.readlines()

print("index: " + str(index))
for line in file:
    line = line.strip()
    
    if line[LETTER] == RIGHT:
        enough = (MAX + 1) - index
        value = calc()
        if value >= enough:
            count += 1
            
        forward(value)
    
    elif line[LETTER] == LEFT:
        if index != 0:
            enough = index

        value = calc()        
        
        if index != 0:
            if value >= enough:
                count += 1
        
        back(value)
        
    print("index\t" + str(index) + "\t-lap: " + str(lap) + " \t-count: " + str(count))    
        
    index = index % (MAX + 1)
        
print("count " + str(count))