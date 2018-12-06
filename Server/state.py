class state:
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


    def updatePosition(self, color, piece, (x, y)):
        if  color == 'red':
            self.redPositions[piece] = [x, y]
        elif color == 'green':     
            self.greenPositions[piece] = [x, y]
        elif color == 'blue':
            self.bluePositions[piece] = [x, y]
        elif color == 'yellow':
            self.yellowPositions[piece] = [x, y]