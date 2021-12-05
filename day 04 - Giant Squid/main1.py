board=[]
boards=[]

with open('input.txt') as f:
    line = f.readline()
    calling_nums = line.split(",")
    f.readline()

    lines=f.readlines()
    board_row_count=0
    for line in lines:
        if board_row_count == 5:
            boards.append(list(board))
            board.clear()
            board_row_count=0
        else:
            items=line.split()
            for item in items:
                board.append(int(item))
            board_row_count+=1

def check_bingo(boards):
    winning_board=[]
    index=0
    for board in boards:
        if (board[0]=="x") and (board[1]=="x") and (board[2]=="x") and (board[3]=="x") and (board[4]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[5]=="x") and (board[6]=="x") and (board[7]=="x") and (board[8]=="x") and (board[9]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[10]=="x") and (board[11]=="x") and (board[12]=="x") and (board[13]=="x") and (board[14]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[15]=="x") and (board[16]=="x") and (board[17]=="x") and (board[18]=="x") and (board[19]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[20]=="x") and (board[21]=="x") and (board[22]=="x") and (board[23]=="x") and (board[24]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[0]=="x") and (board[5]=="x") and (board[10]=="x") and (board[15]=="x") and (board[20]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[1]=="x") and (board[6]=="x") and (board[11]=="x") and (board[16]=="x") and (board[21]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[2]=="x") and (board[7]=="x") and (board[12]=="x") and (board[17]=="x") and (board[22]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[3]=="x") and (board[8]=="x") and (board[13]=="x") and (board[18]=="x") and (board[23]=="x"):
            winning_board=list(boards[index])
            return winning_board
        elif (board[4]=="x") and (board[9]=="x") and (board[14]=="x") and (board[19]=="x") and (board[24]=="x"):
            winning_board=list(boards[index])
            return winning_board
        index+=1
    return []

for x in calling_nums:
    num=int(x)
    for board in boards:
        if board.count(num)==1:
            board[board.index(num)]="x"

    winning_board = check_bingo(boards)
    
    if (len(winning_board)!=0):
        board_sum=0
        for item in winning_board:
            if (item == "x"):
                continue
            else:
                board_sum+=item
        final_score=board_sum*num
        print("Winning Bingo List: {}".format(winning_board))
        print("Sum of unmarked numbers on bingo board: {}".format(board_sum))
        print("last called bingo number: {}".format(num))
        print("Final Score: {}".format(final_score))
        exit()
