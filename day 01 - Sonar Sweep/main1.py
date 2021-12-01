with open('input.txt') as f:
    lines = f.readlines()

increases_count=0           #count the number of increased measurements

for i in range(1,len(lines)):
    if int(lines[i]) - int(lines[i-1]) > 0:
        increases_count+=1

print("No of increased measurements: {}".format(increases_count))