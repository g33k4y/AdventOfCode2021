with open('input.txt') as f:
    lines = f.readlines()

increases_count=0           #count the number of increased measurements
sumA=int(lines[0])+int(lines[1])+int(lines[2])

try:
    for i in range(3,len(lines)):
        sumB=int(lines[i])+int(lines[i-1])+int(lines[i-2])
        if sumB - sumA > 0:
            increases_count+=1
        sumA=sumB
except:
    print("Array out of bounds error")

print("No of increased measurements: {}".format(increases_count))