class chess_board():
    def __init__(self):
        #2D array for chess board:
        self.board = [0] * 8 #[[0],[0],...,[0]] CSP
        for i in range(8):
            self.board[i] = [0] * 8
        #an array for final place of queens:
        self.queens = []  #assignment
        self.variable = ['q0','q1','q2','q3','q4','q5','q6','q7']

    def show(self):
        for i in range (8):
            temp = ''
            for j in range (8):
                if ((i,j) in self.queens):
                    temp += 'q   '
                else:
                    #temp += str(self.board[i][j]) + '   '
                    temp += '-   '
            print (temp)

    def order_domain_value(self,var):
        arr = []
        if var == 'q0': 
            for i in range(8):
                if self.board[i][0] == 0:
                    arr.append((i,0))
        elif var == 'q1': 
            for i in range(8):
                if self.board[i][1] == 0:
                    arr.append((i,1))
        elif var == 'q2': 
            for i in range(8):
                if self.board[i][2] == 0:
                    arr.append((i,2))
        elif var == 'q3': 
            for i in range(8):
                if self.board[i][3] == 0:
                    arr.append((i,3))
        elif var == 'q4': 
            for i in range(8):
                if self.board[i][4] == 0:
                    arr.append((i,4))
        elif var == 'q5': 
            for i in range(8):
                if self.board[i][5] == 0:
                    arr.append((i,5))
        elif var == 'q6': 
            for i in range(8):
                if self.board[i][6] == 0:
                    arr.append((i,6))
        elif var == 'q7':
            for i in range(8):
                if self.board[i][7] == 0:
                    arr.append((i,7))    
        return arr

    def move (self,position):#pos(x,y)
        counter_for_degree = 0
        self.queens.append(position)
        #row,col,/dig,\dig of a move should be +1
        row, col = position
        #/
        rSTRow = row+col
        #\
        lSTRow = row-col

        #row:
        for i in range(8):
            #x cns , y var
            self.board[row][i] += 1
            if (row,i) != position:
                counter_for_degree += 1
        #col
        for i in range(8):
            #x var , y cns
            self.board[i][col] += 1
            if (i,col) != position:
                counter_for_degree += 1
        #/ dig
        for i in range(8):
            if rSTRow >= 0:
                if rSTRow < 8:
                    self.board[rSTRow][i] += 1
                    if (rSTRow,i) != position:
                        counter_for_degree += 1
                rSTRow -= 1
        #\ dig
        for i in range(8):
            if lSTRow < 8:
                if lSTRow >= 0:
                    self.board[lSTRow][i] += 1
                    if (lSTRow,i) != position:      
                        counter_for_degree += 1
                lSTRow +=1
        return counter_for_degree        

    def re_move (self,position):#pos(x,y)
        self.queens.remove(position)
        #row,col,/dig,\dig of a move should be -1
        row, col = position
        #/
        rSTRow = row+col
        #\
        lSTRow = row-col

        #row:
        for i in range(8):
            #x cns , y var
            self.board[row][i] -= 1
        #col
        for i in range(8):
            #x var , y cns
            self.board[i][col] -= 1
        #/ dig
        for i in range(8):
            if rSTRow >= 0:
                if rSTRow < 8:
                    self.board[rSTRow][i] -= 1
                rSTRow -= 1
        #\ dig
        for i in range(8):
            if lSTRow < 8:
                if lSTRow >= 0:
                    self.board[lSTRow][i] -= 1
                lSTRow +=1

def degree(board):
    valid_Col = []
    for var in board.variable:
        if var == 'q0': 
            valid_Col.append(0)  
        elif var == 'q1': 
            valid_Col.append(1)  
        elif var == 'q2': 
            valid_Col.append(2)  
        elif var == 'q3': 
            valid_Col.append(3)  
        elif var == 'q4':
            valid_Col.append(4)  
        elif var == 'q5': 
            valid_Col.append(5)  
        elif var == 'q6': 
            valid_Col.append(6)  
        elif var == 'q7':        
            valid_Col.append(7)  

    x = 0 #if x is max than return a position of a queen
    pos = (0,0)
    var = ''
    for i in range(8): #row
        for j in valid_Col: #col
            newMax = board.move((i,j))
            board.re_move((i,j))
            if x < newMax:
                x = newMax
                pos = (i,j)
    r , c = pos
    if c == 0:
        var = 'q0'
    elif c == 1:
        var = 'q1'
    elif c == 2:
        var = 'q2' 
    elif c == 3:
        var = 'q3' 
    elif c == 4:
        var = 'q4' 
    elif c == 5:
        var = 'q5' 
    elif c == 6:
        var = 'q6'
    elif c == 7:
        var = 'q7'  
    return var

#min remaing value //moteghayery ba kamtarin maghadir mojaz
def mrv(board):
    flag = False
    reVar = ''
    minRV = 8
    for var in board.variable:
        x = len(board.order_domain_value(var))
        if x < minRV:
            minRV = x
            reVar = var
            flag =True
    if flag:
        return var

    else:
        #mrv is not helpful, we should using degree :
        reVar = degree(board)
        return reVar    

def lcv(board,cur_queen): #lcv(b,var)
    arr = board.variable
    arr.remove(cur_queen) #list of unplaced queens
    valid_Col = []
    for var in arr:
        if var == 'q0': 
            valid_Col.append(0)  
        elif var == 'q1': 
            valid_Col.append(1)  
        elif var == 'q2': 
            valid_Col.append(2)  
        elif var == 'q3': 
            valid_Col.append(3)  
        elif var == 'q4':
            valid_Col.append(4)  
        elif var == 'q5': 
            valid_Col.append(5)  
        elif var == 'q6': 
            valid_Col.append(6)  
        elif var == 'q7':        
            valid_Col.append(7)
    global_min = 8  
    posOFglobal_min = (-1,-1)      
    domain_cur_q = board.order_domain_value(cur_queen)
    for position in domain_cur_q:
        board.move(position)
        local_min = 0
        for j in  valid_Col:
            for i in range(8):
                if board[i][j] == 1:
                    local_min += 1
        if local_min < global_min:
            global_min = local_min
            posOFglobal_min = position
        board.re_move(position)
    return posOFglobal_min
    

def select_unassigned_var (b):
    var = mrv(b)
    return var

def recursive_backtracking(b) :                 
    #####GOAL test
    if len(b.queens) == 8:
        return True
    #####SELECT:
    var = select_unassigned_var(b) 
    #####ASSIGNMENT:
    arr = b.order_domain_value(var)    
    for a in arr:
        b.move(a)
        print('this queen placed: '+var)
        b.variable.remove(var) #var should be pop if asiignment completed 
        ##################forward checking:
        if len(b.variable) > 1: 
            print('FC:')
            forwVar = select_unassigned_var(b) #with next var
            forwArr = b.order_domain_value(forwVar)
            if len(forwArr) == 0:
                b.re_move(a)
                print('FC done and this var is not valid ' + var)
                continue
            print ('FC done')            
        ###################################  
        Result= recursive_backtracking(b)
        if Result == True:
            return Result
        b.variable.append(var) #var should be push if backtrack happend
        b.re_move(a)
        print('this queen unplaced: '+var)
    return False
      
def main():
    bo = chess_board()
    #b.show()
    recursive_backtracking(bo)
    bo.show()

if __name__ == '__main__':
    main()