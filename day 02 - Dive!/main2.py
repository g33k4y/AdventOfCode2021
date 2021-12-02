with open('input.txt') as f:
    lines = f.readlines()

horizon=0           #the horizontal position
depth=0             #the depth position
aim=0               #the aim value

for x in lines:
    word=x.split()
    if word[0] == "forward":
        horizon+=int(word[1])
        depth+=(int(word[1])*aim)
    elif word[0] == "up":
        aim-=int(word[1])
    else:
        aim+=int(word[1])

print("Horizontal position: {}".format(horizon))
print("Depth position: {}".format(depth))
print("Aim value: {}".format(aim))
print("Horizontal*Depth measurement: {}".format(horizon*depth))