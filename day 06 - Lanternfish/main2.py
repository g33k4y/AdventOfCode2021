lanternfishes=[]
total=0

with open('input.txt') as f:
    line = f.readlines()
lines = line[0].split(",")
for a in range(0,len(lines)):
    lines[a]=int(lines[a])
lines.sort()

#store number of lanternfishes in a list based on days to breed new lanternfish from day 0 to day 8
# so lanternfishes[0] contains number of lanternfish that is on day 0
# lanternfishes[1] contains number of lanternfish that is on day 1, etc up to lanternfishes[8]
for x in range(0,9):
    lanternfishes.append(lines.count(x))

print("Initial state: {}".format(lanternfishes))

#for each day that has passed, fishes at lanternfishes[0] will be added to day 6, then popped and appended to lanternfishes list
for day in range(0,256):
    fishes=lanternfishes[0]
    lanternfishes[7]+=fishes
    lanternfishes.pop(0)
    lanternfishes.append(fishes)
    print(lanternfishes)

for index in range(0,len(lanternfishes)):
    total+=lanternfishes[index]

print("total number of Lanternfishes after 256 days: {}".format(total))