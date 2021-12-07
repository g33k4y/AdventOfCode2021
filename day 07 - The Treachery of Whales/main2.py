with open('input.txt') as f:
    line = f.readlines()

crabs_pos = line[0].split(",")
for a in range(0,len(crabs_pos)):
    crabs_pos[a]=int(crabs_pos[a])


def calculate_fuel(num):
    total=0
    for x in range(1,num+1):
        total+=x
    return total

least_fuel=[]

for x in range(min(crabs_pos),max(crabs_pos)+1):
    fuels=0
    for crab in range(0,len(crabs_pos)):
        fuels+=calculate_fuel(abs(crabs_pos[crab]-x))
    least_fuel.append(fuels)

print("least fuel: {}".format(min(least_fuel)))

