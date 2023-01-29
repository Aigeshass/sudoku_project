board=[ [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 8],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

def print_board(board):


    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        for j in range(len(board)):
            if j%3==0 and j!=0:
                print("|", end=" ")
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end=" ")

def check_valid(board, pos, num):
    #Check row first
    for i in range(len(board)):
        if board[pos[0]][i]==num and pos[1]!=i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check the box
    x_dim=pos[1]//3
    y_dim=pos[0]//3
    for i in range(y_dim*3, y_dim*3+3):
        for j in range(x_dim*3, x_dim*3+3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                return i, j
    return None

def recurse(board):
    finding= find_empty(board)
    if not finding:
        return True
    else:
        row, col= finding
        for i in range(1, 10):
            if(check_valid(board, (row, col), i)):
                board[row][col]=i
                if recurse(board):
                    return True
                board[row][col]=0
    return False

print_board(board)
recurse(board)
print_board(board)