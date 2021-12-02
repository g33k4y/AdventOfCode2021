with open('input.txt') as f:
    lines = f.readlines()

horizon=0           #the horizontal position
depth=0             #the depth position

for x in lines:
    word=x.split()
    if word[0] == "forward":
        horizon+=int(word[1])
    elif word[0] == "up":
        depth-=int(word[1])
    else:
        depth+=int(word[1])

print("Horizontal position: {}".format(horizon))
print("Depth position: {}".format(depth))
print("Horizontal*Depth measurement: {}".format(horizon*depth))