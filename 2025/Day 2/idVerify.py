PATH =  "2025/Day 2/"
FILE = PATH + "input.txt"

numbers = []

# Main
with open(FILE, "r") as f:
    file = f.read()
    file = file.replace(",", "\n").splitlines()

for line in file: # prende il range
    line = line.strip(",")
    first, last = map(int, line.split("-"))    
    for i in range(first, last+1): # ruota il range per ogni numero
        i = str(i)
        
        for lap in range(2, len(i) + 1): # ruotare il controllo e il controllato  
            #print("lap: " + str(lap))  
            if len(i) % lap != 0:
                pass
            else:
                length = len(i) // lap
                
                #print(length)
                
                before = i[:length]
                after = i[length:]
                #print(before, after, len(after))
                
                check = 0
                for every in range(0, len(after), length):
                    #print("every: " + str(every))
                    if before == after[every : every + length]:
                        check += 1
                    #print("prova: " + after[every : every + length])
                
                if check + 1 == lap:
                    numbers.append(int(i))
                    break

sum = 0        
for i in numbers:
    sum += i
    print("i: " + str(i))
    
print("SUM: " + str(sum))