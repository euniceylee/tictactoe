class TTTBoard:
    def __init__(self):
        #method 1
        # self.board = ['*','*','*','*','*','*','*','*','*']
        #method 2
        self.board = 9*['*']
        #method 3
        # self.board = []
        # for i in range(9): #for loop that runs 9 times
        #     self.board.append('*')
        #method 4
        # self.board = ['*' for i in range(9)]

    def __str__(self):
        #method 1
        # s = self.board[0] + " " + self.board[1] + " " + self.board[2] + "\n"
        # s += self.board[3] + " " + self.board[4] + " " + self.board[5] + "\n"
        # s += self.board[6] + " " + self.board[7] + " " + self.board[8] + "\n"
        #method 2
        s = ""
        for x in [0,3,6]: #positions in the list of 9 that start a new row
            s += self.board[x] + " " + self.board[x+1] + " " + self.board[x+2] + "\n"
        return s
    
    def makeMove(self, player, pos):
        pass
        #player is "X" or "O"
        #pos is a number (hopefully 0 - 8)
        #if statement
        #first ask, is the number out of bounds?
        if pos > 8 or pos < 0:
            return False
        elif self.board[pos] != "*":
            return False 
        else:
            self.board[pos] = player
            return True
    
    def hasWon(self, player):
        for x in [0,3,6]:
            if self.board[x] == self.board[x+1] == self.board[x+2] == player:
                return True 
        for x in [0, 1, 2]:
            if self.board[x] == self.board[x+3] == self.board[x+6] == player:
                return True 
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True 
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        else:
            return False
    
    def gameOver(self):
        if self.hasWon("X") or self.hasWon("O"):
            return True
        elif not ("*" in self.board): 
            return True
        else:
            return False
    
    def clear(self):
        self.board = 9*["*"]

#test by doing myb.makeMove("X", 4)

def playTicTacToe():
    """uses our TTTBoard class to play tic tac toe with two players"""
    myB = TTTBoard()
    players = ["X", "O"]
    playerTurn = 0
    while not myB.gameOver():
        print myB
        iMove = input("Player " + players[playerTurn] + " what is your move? ")
        res = myB.makeMove(players[playerTurn], iMove)
        if res == False:
            print "Invalid move. Try again!"
            continue 
        if playerTurn == 0:
            playerTurn = 1
        else:
            playerTurn = 0

    print "\nGame over!!!\n"
    print myB
    for i in [0,1]:
        if myB.hasWon(players[i]):
            print players[i] + " wins!"

# #Here are some tests. These are not at all exhaustive tests. You will DEFINITELY need
# #    to write some more tests to make sure that your TTTBoard class is behaving properly. 

myB = TTTBoard()
myB.makeMove("X", 8)
myB.makeMove("O", 7)

assert myB.gameOver() == False 

myB.makeMove("X", 5)
myB.makeMove("O", 6)
myB.makeMove("X", 2)

assert myB.hasWon("X") == True
assert myB.hasWon("O") == False
assert myB.gameOver() == True

myB.clear()

assert myB.gameOver() == False

myB.makeMove("O", 3)
myB.makeMove("O", 4)
myB.makeMove("O", 5)

assert myB.hasWon("X") == False
assert myB.hasWon("O") == True
assert myB.gameOver() == True
