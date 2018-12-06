class Coordinates:

    def __init__(self):
        self.redInitials = [
            [215, 415],
            [255, 415],
            [215, 455],
            [255, 455]
        ]
        self.greenInitials = [
            [215, 115],
            [255, 115],
            [215, 155],
            [255, 155]
        ]
        self.blueInitials = [
            [515, 115],
            [555, 115],
            [515, 155],
            [555, 155]
        ]
        self.yellowInitials = [
            [515, 415],
            [555, 415],
            [515, 455],
            [555, 455]
        ]

        self.redFinals = [
            [375, 327],
            [395, 327],
            [415, 327],
            [395, 310]
        ]
        self.greenFinals = [
            [360, 272],
            [360, 292],
            [360, 312],
            [375, 292]
        ]
        self.blueFinals = [
            [430, 272],
            [430, 292],
            [430, 312],
            [412, 292]
        ]
        self.yellowFinals = [
            [375, 257],
            [395, 257],
            [415, 257],
            [4395, 275]
        ]

        self.SQUARE_SIDE = 30
        self.initialX = 387 - self.SQUARE_SIDE
        self.xValues = [
            self.initialX, self.initialX, self.initialX, self.initialX, self.initialX, self.initialX,     # Column with 6 squares
            self.initialX - self.SQUARE_SIDE,
            self.initialX - self.SQUARE_SIDE,
            self.initialX - self.SQUARE_SIDE * 2,
            self.initialX - self.SQUARE_SIDE * 3,
            self.initialX - self.SQUARE_SIDE * 4,
            self.initialX - self.SQUARE_SIDE * 5,
            self.initialX - self.SQUARE_SIDE * 6,
            self.initialX - self.SQUARE_SIDE * 6,
            self.initialX - self.SQUARE_SIDE * 6,
            self.initialX - self.SQUARE_SIDE * 5,
            self.initialX - self.SQUARE_SIDE * 4,
            self.initialX - self.SQUARE_SIDE * 3,
            self.initialX - self.SQUARE_SIDE * 2,
            self.initialX - self.SQUARE_SIDE,
            self.initialX - self.SQUARE_SIDE,
            self.initialX, self.initialX, self.initialX, self.initialX, self.initialX, self.initialX,     # Column with 6 squares
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 3,
            self.initialX + self.SQUARE_SIDE * 3,
            self.initialX + self.SQUARE_SIDE * 4,
            self.initialX + self.SQUARE_SIDE * 5,
            self.initialX + self.SQUARE_SIDE * 6,
            self.initialX + self.SQUARE_SIDE * 7,
            self.initialX + self.SQUARE_SIDE * 8,
            self.initialX + self.SQUARE_SIDE * 8,
            self.initialX + self.SQUARE_SIDE * 8,
            self.initialX + self.SQUARE_SIDE * 7,
            self.initialX + self.SQUARE_SIDE * 6,
            self.initialX + self.SQUARE_SIDE * 5,
            self.initialX + self.SQUARE_SIDE * 4,
            self.initialX + self.SQUARE_SIDE * 3,
            self.initialX + self.SQUARE_SIDE * 3,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE * 2,
            self.initialX + self.SQUARE_SIDE,
            # Reds
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            # Greens
            self.initialX - self.SQUARE_SIDE * 5,
            self.initialX - self.SQUARE_SIDE * 4,
            self.initialX - self.SQUARE_SIDE * 3,
            self.initialX - self.SQUARE_SIDE * 2,
            self.initialX - self.SQUARE_SIDE,
            # Blues
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            self.initialX + self.SQUARE_SIDE,
            # Yellows
            self.initialX + self.SQUARE_SIDE * 7,
            self.initialX + self.SQUARE_SIDE * 6,
            self.initialX + self.SQUARE_SIDE * 5,
            self.initialX + self.SQUARE_SIDE * 4,
            self.initialX + self.SQUARE_SIDE * 3
        ]
        self.initialY = 600 - 75 - self.SQUARE_SIDE
        self.yValues = [
            self.initialY,
            self.initialY - self.SQUARE_SIDE,
            self.initialY - self.SQUARE_SIDE * 2,
            self.initialY - self.SQUARE_SIDE * 3,
            self.initialY - self.SQUARE_SIDE * 4,
            self.initialY - self.SQUARE_SIDE * 5,
            self.initialY - self.SQUARE_SIDE * 5,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 9,
            self.initialY - self.SQUARE_SIDE * 9,
            self.initialY - self.SQUARE_SIDE * 10,
            self.initialY - self.SQUARE_SIDE * 11,
            self.initialY - self.SQUARE_SIDE * 12,
            self.initialY - self.SQUARE_SIDE * 13,
            self.initialY - self.SQUARE_SIDE * 14,
            self.initialY - self.SQUARE_SIDE * 14,
            self.initialY - self.SQUARE_SIDE * 14,
            self.initialY - self.SQUARE_SIDE * 13,
            self.initialY - self.SQUARE_SIDE * 12,
            self.initialY - self.SQUARE_SIDE * 11,
            self.initialY - self.SQUARE_SIDE * 10,
            self.initialY - self.SQUARE_SIDE * 9,
            self.initialY - self.SQUARE_SIDE * 9,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 8,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 6,
            self.initialY - self.SQUARE_SIDE * 5,
            self.initialY - self.SQUARE_SIDE * 5,
            self.initialY - self.SQUARE_SIDE * 4,
            self.initialY - self.SQUARE_SIDE * 3,
            self.initialY - self.SQUARE_SIDE * 2,
            self.initialY - self.SQUARE_SIDE,
            self.initialY,
            self.initialY,
            # Reds
            self.initialY - self.SQUARE_SIDE,
            self.initialY - self.SQUARE_SIDE * 2,
            self.initialY - self.SQUARE_SIDE * 3,
            self.initialY - self.SQUARE_SIDE * 4,
            self.initialY - self.SQUARE_SIDE * 5,
            # Greens
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            # Blues
            self.initialY - self.SQUARE_SIDE * 13,
            self.initialY - self.SQUARE_SIDE * 12,
            self.initialY - self.SQUARE_SIDE * 11,
            self.initialY - self.SQUARE_SIDE * 10,
            self.initialY - self.SQUARE_SIDE * 9,
            # Yellows
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
            self.initialY - self.SQUARE_SIDE * 7,
        ]