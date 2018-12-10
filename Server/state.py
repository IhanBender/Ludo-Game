class State:

    def __init__(self,
        redInitials,
        greenInitials,
        blueInitials,
        yellowInitials
    ):
        self.redPositions = []
        self.greenPositions = []
        self.bluePositions = []
        self.yellowPositions = []

        for i in range(0,4):
            self.redPositions.append(redInitials[i])
            self.greenPositions.append(greenInitials[i])
            self.bluePositions.append(blueInitials[i])
            self.yellowPositions.append(yellowInitials[i])

        
    def updatePosition(self, color, piece, x, y):
        if  color == 'red':
            self.redPositions[piece] = [x, y]
        elif color == 'green':
            self.greenPositions[piece] = [x, y]
        elif color == 'blue':
            self.bluePositions[piece] = [x, y]
        elif color == 'yellow':
            self.yellowPositions[piece] = [x, y]
