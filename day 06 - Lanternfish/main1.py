with open('input.txt') as f:
    line = f.readlines()

lanternfishes = line[0].split(",")
for a in range(0,len(lanternfishes)):
    lanternfishes[a]=int(lanternfishes[a])

print ("Initial Day 0: {}".format(lanternfishes))

for day in range(1,81):
    for index in range(0,len(lanternfishes)):
        lanternfishes[index]-=1
        if lanternfishes[index] < 0:
            lanternfishes[index] = 6
            lanternfishes.append(8)
    # print ("After Day {}: {}".format(day,lanternfishes))

print("Total no of Lanternfishes after 80 days: {}".format(len(lanternfishes)))