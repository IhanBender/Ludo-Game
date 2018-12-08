import pygame

class PieceDrawer:

    def __init__(self):
        self.red30 = pygame.image.load("images/red30.png")
        self.red15 = pygame.image.load("images/red15.png")
        self.blue30 = pygame.image.load("images/blue30.png")
        self.blue15 = pygame.image.load("images/blue15.png")
        self.green30 = pygame.image.load("images/green30.png")
        self.green15 = pygame.image.load("images/green15.png")
        self.yellow30 = pygame.image.load("images/yellow30.png")
        self.yellow15 = pygame.image.load("images/yellow15.png")

    def drawRedPiece(self, screen, (x, y), size):
        x,y = int(x), int(y)
        if size == 15:
            screen.blit(self.red15,(x,y))
        else:
            screen.blit(self.red30,(x,y))

    def drawBluePiece(self, screen, (x, y), size):
        x,y = int(x), int(y)
        if size == 15:
            screen.blit(self.blue15,(x,y))
        else:
            screen.blit(self.blue30,(x,y))

    def drawGreenPiece(self, screen, (x, y), size):
        x,y = int(x), int(y)
        if size == 15:
            screen.blit(self.green15,(x,y))
        else:
            screen.blit(self.green30,(x,y))

    def drawYellowPiece(self, screen, (x, y), size):
        x,y = int(x), int(y)
        if size == 15:
            screen.blit(self.yellow15,(x,y))
        else:
            screen.blit(self.yellow30,(x,y))