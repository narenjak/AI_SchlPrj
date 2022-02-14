class chess_board():
    def __init__(self):#constructor
        #2D array for chess board:
        self.board = [0] * 8 #[[0],[0],...,[0]] CSP
        for i in range(8):
            self.board[i] = [0] * 8
        #an array for final place of queens:
        self.queens = []  #assignment
        self.variable = ['q0','q1','q2','q3','q4','q5','q6','q7']

    def show(self): #show chess board 
        for i in range (8):
            temp = ''
            for j in range (8):
                if ((i,j) in self.queens):
                    temp += 'q   '
                else:
                    #temp += str(self.board[i][j]) + '   '
                    temp += '-   '
            print (temp)

    def order_domain_value(self,var): #//mohasebe majmoee az khane hay motabar baray har queen
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

    def move (self,position):#input a pos(x,y) and apply constrints
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

#degree // makzimom az khane hay mahdod shode
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
        #print('this queen placed: '+var)
        b.variable.remove(var) #var should be pop if asiignment completed 
        ##################forward checking:
        if len(b.variable) > 1: 
            #print('FC:')
            forwVar = select_unassigned_var(b) #with next var
            forwArr = b.order_domain_value(forwVar)
            if len(forwArr) == 0:
                b.re_move(a)
                print('FC done and this var is not valid ' + var)
                continue
            #print ('FC done')            
        ###################################  
        Result= recursive_backtracking(b)
        if Result == True:
            return Result
        b.variable.append(var) #var should be push if backtrack happend
        b.re_move(a)
        #print('this queen unplaced: '+var)
    return False


#//sa`i shod peyade sazi va estefade shavad likan natavanestim motasefane

#least constrainting value //meghdari ke kamtarin mahdodit ro ijad kond
#dar 2 hakghe for roy board harekat kardim va 0->1 ha va khneh hay != 0  ra shomordim
def lcv(board,cur_queen): #lcv(b,var)
    board.variable.remove(cur_queen)
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
    global_min = 64  
    posOFglobal_min = (-1,-1)      
    domain_cur_q = board.order_domain_value(cur_queen)
    for position in domain_cur_q:
        board.move(position)
        local_min = 0
        for j in  valid_Col:
            for i in range(8):
                if board.board[i][j] == 1:
                    local_min += 1
        if local_min < global_min:
            global_min = local_min
            posOFglobal_min = position
        board.re_move(position)
    board.variable.append(cur_queen)
    return posOFglobal_min
def remove_inconsistent_value(b,var1,var2):
    removed = False
    domain_var1 = b.order_domain_value(var1)
    #for each x in Domain[X i ] do
    for x in domain_var1:
        b.move(x) 
        domain_var2 = b.order_domain_value(var2)
        if len(domain_var2) == 0: #if no value y in Domain[X j ] allows (x,y) to satisfy constraint(X i , X j )
            #then delete x from Domain[X i ]; removed <- true:
            r, c =x
            b.board[r][c] += 1
            domain_var1.remove(x)
            removed = True
        b.re_move(x)
    return removed
def AC (b):
    #select:        
    var = select_unassigned_var (b)
    b.variable.remove(var)
    #arc start:
    #local variables: queue, a queue of arcs, initially all the arcs in csp
    queue_arc = []
    for x in b.variable:
        for y in b.variable:
            queue_arc.append((x,y))
    for i in b.variable:
        queue_arc.remove((i,i))
    
    #assignment
    arr = b.order_domain_value(var)
    for pos in arr:
        #//hazf maghadir nasazegar
        b.move(pos)
        for i in range (8):
            for j in range(8):
                b.board[i][j] = 0
        #completed graph has (n*n-1)/2 edge and we have 2-way edge so we most *2 -->  there is n*(n-1)=8*7 vaiable
        while len(queue_arc) != 0:
            var1 , var2= queue_arc.pop(0)
            print(str(var1)+ ','+str(var2))
            if remove_inconsistent_value(b,var1,var2):
                b.variable.remove(var1)
                for var in b.variable:
                    queue_arc.append((var,var1))
                b.variable.append(var1) 
                
        b.show()   
        b.re_move(pos)

      
def main():
    bo = chess_board()
    #b.show()
    recursive_backtracking(bo)
    bo.show()

if __name__ == '__main__':
    main()