class chess_board():
    def __init__(self):
        #2D array for chess board:
        self.board = [0] * 8 #[[0],[0],...,[0]] CSP
        for i in range(8):
            self.board[i] = [0] * 8
        #an array for final place of queens:
        self.queens = []  #assignment
        self.variable = ['q1','q2','q3','q4','q5','q6','q7','q8']


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
        if var == 'q1': 
            for i in range(8):
                if self.board[i][0] == 0:
                    arr.append((i,0))
        elif var == 'q2': 
            for i in range(8):
                if self.board[i][1] == 0:
                    arr.append((i,1))
        elif var == 'q3': 
            for i in range(8):
                if self.board[i][2] == 0:
                    arr.append((i,2))
        elif var == 'q4': 
            for i in range(8):
                if self.board[i][3] == 0:
                    arr.append((i,3))
        elif var == 'q5': 
            for i in range(8):
                if self.board[i][4] == 0:
                    arr.append((i,4))
        elif var == 'q6': 
            for i in range(8):
                if self.board[i][5] == 0:
                    arr.append((i,5))
        elif var == 'q7': 
            for i in range(8):
                if self.board[i][6] == 0:
                    arr.append((i,6))
        elif var == 'q8':
            for i in range(8):
                if self.board[i][7] == 0:
                    arr.append((i,7))    


        return arr

    def move (self,position):#pos(x,y)
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
        #col
        for i in range(8):
            #x var , y cns
            self.board[i][col] += 1
        #/ dig
        for i in range(8):
            if rSTRow >= 0:
                if rSTRow < 8:
                    self.board[rSTRow][i] += 1
                rSTRow -= 1
        #\ dig
        for i in range(8):
            if lSTRow < 8:
                if lSTRow >= 0:
                    self.board[lSTRow][i] += 1
                lSTRow +=1

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

def selectUnassignedVar (b,i):
    try:
        var = b.variable[i]
        return var  
    except:
        print('empty')  
         
                    


def recursive_backtracking(b,c) :                 
    #goal test
    if len(b.queens) == 8:
        return True
    var = selectUnassignedVar(b,c)    
    arr = b.order_domain_value(var)    
    for a in arr:
        b.move(a)
        ##################forward checking:
        if (c+1) != 8:       
            forwVar = selectUnassignedVar(b, c+1)
            #print(forwVar)
            forwArr = b.order_domain_value(forwVar)
            #print(forwArr)
            if len(forwArr) == 0:
                b.re_move(a)
                continue            
        ###################################    )
        c += 1
        Result= recursive_backtracking(b,c)
        if Result == True:
            return Result
        c -= 1
        b.re_move(a)
        #print(b.queens)
    return False

        
def main():
    bo = chess_board()
    #b.show()
    i = 0 
    recursive_backtracking(bo, i)
    bo.show()
   
if __name__ == '__main__':
    main()