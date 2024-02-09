class Board:
    def __init__(self , p1 , p2 , id):
        #  init board segment
        self.board = ['0','1','2','3','4','5','6','7','8']
        self.win_state = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        self.p1 = p1
        self.p2 = p2
        self.id = id 
        self.turn = p1
        self.waiting = p2
        
    def drawBoard(self):
        """drowing board as
        1|2|3
        4|5|6
        7|8|9
        """
        txt = "\n" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "\n" + self.board[3] + "|" + self.board[4] + "|" + self.board[5]   + "\n" + self.board[6] + "|" + self.board[7] + "|" + self.board[8] 
        return txt
    #change board cell abnd check that moccve is legal 
    def makeMove(self, move):
        move = int(move)
        if self.turn == self.p1:
            self.board[move] = 'X'
        else:
            self.board[move] = 'O'

        done = True
        winner = False
        #check cell is empty
        for cell in self.board:
            if cell!= 'X' or cell != 'O':
                done = False
        #check game isn't  in win state              
        for a,b,c in self.win_state:
            if self.board[a] == self.board[b] == self.board[c]:
                winner = True
        #send appropriate respond to client
        if winner:
            return "300 WIN"
        
        elif done:
            return "300 FIN"
        else:
            return "301 NPT"
    #changing players turn .
    def changeTurn(self):
        if self.turn == self.p2:
            self.turn = self.p1
            self.waiting = self.p2
        else:
            self.turn = self.p2
            self.waiting = self.p1
        
