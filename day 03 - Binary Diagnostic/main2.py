with open('input.txt') as f:
    lines = f.readlines()

for a in range(0,len(lines)):
    lines[a]=lines[a].strip()


def oxygen_gen(binary_list, index):
    bit_0_count=0
    bit_1_count=0
    new_list0=[]
    new_list1=[]
    if len(binary_list) == 1:
        return binary_list[0]
    else:
        for x in binary_list:
            if int(x[index]) == 0:
                bit_0_count+=1
                new_list0.append(x)
            else:
                bit_1_count+=1
                new_list1.append(x)
        if bit_0_count>bit_1_count:
            return oxygen_gen(new_list0,index+1)
        else:
            return oxygen_gen(new_list1,index+1)

def co2_gen(binary_list, index):
    bit_0_count=0
    bit_1_count=0
    new_list0=[]
    new_list1=[]
    if len(binary_list) == 1:
        return binary_list[0]
    else:
        for x in binary_list:
            if int(x[index]) == 0:
                bit_0_count+=1
                new_list0.append(x)
            else:
                bit_1_count+=1
                new_list1.append(x)
        if bit_0_count<=bit_1_count:
            return co2_gen(new_list0,index+1)
        else:
            return co2_gen(new_list1,index+1)


oxy_rating=oxygen_gen(lines,0)           #the horizontal position
co2_rating=co2_gen(lines,0)             #the depth position

print("Oxygen Generator Rating in Binary: {}            in Decimal: {}".format(oxy_rating, int(oxy_rating,2)))
print("Epsilon Rate in Binary: {}                       in Decimal: {}".format(co2_rating, int(co2_rating, 2)))
print("Life Support rating in Decimal: {}".format(int(oxy_rating, 2)*int(co2_rating, 2)))
