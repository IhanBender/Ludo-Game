import pygame

class Dice:

    def __init__(self):
        self.faces = []
        self.faces.append(pygame.image.load("images/dice0.png"))
        self.faces.append(pygame.image.load("images/dice1.png"))
        self.faces.append(pygame.image.load("images/dice2.png"))
        self.faces.append(pygame.image.load("images/dice3.png"))
        self.faces.append(pygame.image.load("images/dice4.png"))
        self.faces.append(pygame.image.load("images/dice5.png"))
        self.faces.append(pygame.image.load("images/dice6.png"))

        self.rfaces = []
        self.rfaces.append(pygame.image.load("images/Rdice0.png"))
        self.rfaces.append(pygame.image.load("images/Rdice1.png"))
        self.rfaces.append(pygame.image.load("images/Rdice2.png"))
        self.rfaces.append(pygame.image.load("images/Rdice3.png"))
        self.rfaces.append(pygame.image.load("images/Rdice4.png"))
        self.rfaces.append(pygame.image.load("images/Rdice5.png"))
        self.rfaces.append(pygame.image.load("images/Rdice6.png"))
        self.rfaces.append(pygame.image.load("images/RdiceRoll.png"))

        self.gfaces = []
        self.gfaces.append(pygame.image.load("images/Gdice0.png"))
        self.gfaces.append(pygame.image.load("images/Gdice1.png"))
        self.gfaces.append(pygame.image.load("images/Gdice2.png"))
        self.gfaces.append(pygame.image.load("images/Gdice3.png"))
        self.gfaces.append(pygame.image.load("images/Gdice4.png"))
        self.gfaces.append(pygame.image.load("images/Gdice5.png"))
        self.gfaces.append(pygame.image.load("images/Gdice6.png"))
        self.gfaces.append(pygame.image.load("images/GdiceRoll.png"))

        self.bfaces = []
        self.bfaces.append(pygame.image.load("images/Bdice0.png"))
        self.bfaces.append(pygame.image.load("images/Bdice1.png"))
        self.bfaces.append(pygame.image.load("images/Bdice2.png"))
        self.bfaces.append(pygame.image.load("images/Bdice3.png"))
        self.bfaces.append(pygame.image.load("images/Bdice4.png"))
        self.bfaces.append(pygame.image.load("images/Bdice5.png"))
        self.bfaces.append(pygame.image.load("images/Bdice6.png"))
        self.bfaces.append(pygame.image.load("images/BdiceRoll.png"))

        self.yfaces = []
        self.yfaces.append(pygame.image.load("images/Ydice0.png"))
        self.yfaces.append(pygame.image.load("images/Ydice1.png"))
        self.yfaces.append(pygame.image.load("images/Ydice2.png"))
        self.yfaces.append(pygame.image.load("images/Ydice3.png"))
        self.yfaces.append(pygame.image.load("images/Ydice4.png"))
        self.yfaces.append(pygame.image.load("images/Ydice5.png"))
        self.yfaces.append(pygame.image.load("images/Ydice6.png"))
        self.yfaces.append(pygame.image.load("images/YdiceRoll.png"))

    def drawDice(self, screen, face, color='-1'):
        if color == '-1':
            screen.blit(self.faces[face], (0, 0))
        elif color == '0':
            screen.blit(self.rfaces[face], (0, 0))
        elif color == '1':
            screen.blit(self.gfaces[face], (0, 0))
        elif color == '2':
            screen.blit(self.bfaces[face], (0, 0))
        elif color == '3':
            screen.blit(self.yfaces[face], (0, 0))

    def hitbox(self):
        return {"x": range(700, 780), "y": range(500, 580)}