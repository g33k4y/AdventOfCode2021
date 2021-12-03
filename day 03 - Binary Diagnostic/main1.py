with open('input.txt') as f:
    lines = f.readlines()

for a in range(0,len(lines)):
    lines[a]=lines[a].strip()


gamma_rate=""           #the horizontal position
epsilon_rate=""             #the depth position
bit_0_count=0
bit_1_count=0


for i in range(0,len(lines[0])):
    for x in lines:
        if int(x[i]) == 0:
            bit_0_count+=1
        else:
            bit_1_count+=1
    if bit_0_count>bit_1_count:
        gamma_rate+="0"
        epsilon_rate+="1"
    else:
        gamma_rate+="1"
        epsilon_rate+="0"
    bit_0_count=0
    bit_1_count=0



print("Gamma Rate in Binary: {}         in Decimal: {}".format(gamma_rate, int(gamma_rate, 2)))
print("Epsilon Rate in Binary: {}       in Decimal: {}".format(epsilon_rate, int(epsilon_rate, 2)))
print("Power Consumption in Decimal: {}".format(int(gamma_rate, 2)*int(epsilon_rate, 2)))
