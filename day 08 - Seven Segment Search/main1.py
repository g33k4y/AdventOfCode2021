outputs=[]
count_1478=0                    #count no of digit 1, 4, 7 or 8
with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line=line.strip()
    line=line.split(" | ")
    outputs.append(line[1])

for digits in outputs:
    digits = digits.split(" ")
    for x in range(0, len(digits)):
        if len(digits[x]) == 2 or len(digits[x]) == 3 or len(digits[x]) == 4 or len(digits[x]) == 7:
            count_1478+=1
            continue 

print("Total number of digit 1, 4, 7 or 8: {}".format(count_1478))
