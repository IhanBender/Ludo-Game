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