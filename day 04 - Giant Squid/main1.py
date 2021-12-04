board=[]
boards=[]
board_index=0
with open('test.txt') as f:
    line = f.readline()
    calling_nums = line.split(",")
    f.readline()
    lines=f.readlines()
    for line in lines:
        if line == "\n":
            print(board)
            # boards.append(board)
            board.clear()
        else:
            board.append(line.split())

# print(boards)
            

        
        


# for a in range(0,len(lines)):
#     lines[a]=lines[a].strip()


# gamma_rate=""           #the horizontal position
# epsilon_rate=""             #the depth position
# bit_0_count=0
# bit_1_count=0


# for i in range(0,len(lines[0])):
#     for x in lines:
#         if int(x[i]) == 0:
#             bit_0_count+=1