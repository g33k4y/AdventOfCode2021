vents=[]                    #list of all vent lines
line_vents=[]               #only count horizontal and vertical vent lines
vent_diagram=[]             #vent field simulating a field 1000 by1000 wide
horizontal=[]               #to populate vent_diagram
points=0                    #final score counting points with at least 2 lines overlaps

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        pair=line.split(" -> ")
        vent=pair[0].split(",")+pair[1].split(",")
        for x in range(0,len(vent)):
            vent[x] = int(vent[x].strip())
        vents.append(list(vent))

#only consider horizontal or vertical or diagonal lines
for x in range(0,len(vents)):
    if (vents[x][0] == vents[x][2]) or (vents[x][1] == vents[x][3]):        #consider horizontal or vertical lines
        line_vents.append(list(vents[x]))
    elif (abs(vents[x][0]-vents[x][2])==abs(vents[x][1]-vents[x][3])):      #consider diagonal lines
        line_vents.append(list(vents[x]))

#create a vent diagram of 1000x1000, assuming x and y coordinate do not go beyond 1000
for x in range(0,1000):
    horizontal.append(0)
for y in range(0,1000):
    vent_diagram.append(list(horizontal))

for vent in line_vents:
    index=0
    if (vent[0] == vent[2]):                                #draw horizontal lines on diagram
        if (vent[1] < vent[3]):
            for y in range(vent[1],vent[3]+1):
                vent_diagram[vent[0]][y]+=1
        else:
            for y in range(vent[3],vent[1]+1):
                vent_diagram[vent[0]][y]+=1
    elif (vent[1] == vent[3]):                              #draw vertical lines on diagram
        if (vent[0] < vent[2]):
            for x in range(vent[0],vent[2]+1):
                vent_diagram[x][vent[1]]+=1
        else:
            for x in range(vent[2],vent[0]+1):
                vent_diagram[x][vent[1]]+=1
    elif (vent[0] < vent[2]):                               #draw diagonal lines from first pair to second pair
        if (vent[1]<vent[3]):                               #draw diagonal from top left to bottom right
            for x in range(vent[0],vent[2]+1):
                vent_diagram[x][vent[1]+index]+=1
                index+=1
        else:                                               #draw diagonal from top right to bottom left
            for x in range(vent[0],vent[2]+1):
                vent_diagram[x][vent[1]+index]+=1
                index-=1
    else:                                                   #draw diagonal lines from second pair to first pair
        if (vent[1]<vent[3]):                               #draw diagonal from top right to bottom left
            for x in range(vent[2],vent[0]+1):
                vent_diagram[x][vent[3]+index]+=1
                index-=1
        else:                                               #draw diagonal from top left to bottom right
            for x in range(vent[2],vent[0]+1):
                vent_diagram[x][vent[3]+index]+=1
                index+=1

for vent in vent_diagram:
    for point in range(0,len(vent)):
        if vent[point]>1:
            points+=1

print("Points with at least 2 lines overlap: {}".format(points))