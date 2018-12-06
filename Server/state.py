class State:

    def __init__(self,
    redInitials,
    greenInitials,
    blueInitials,
    yellowInitials,
    turn):

        self.redPositions = redInitials
        self.greenPositions = greenInitials
        self.bluePositions = blueInitials
        self.yellowPositions = yellowInitials
        self.currentTurn = turn
        # Still has to define players colors

    def updatePosition(self, color, piece, (x, y)):
        if  color == 'red':
            self.redPositions[piece] = [x, y]
        elif color == 'green':
            self.greenPositions[piece] = [x, y]
        elif color == 'blue':
            self.bluePositions[piece] = [x, y]
        elif color == 'yellow':
            self.yellowPositions[piece] = [x, y]

    def nextPlayer(self, player_num):
        if self.currentTurn == player_num - 1:
            self.currentTurn = 1
        else:
            self.currentTurn += 1