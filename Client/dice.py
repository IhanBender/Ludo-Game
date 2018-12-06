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

    def drawDice(self, screen, face):
        screen.blit(self.faces[face], (700, 500))

    def hitbox(self):
        return {"x": range(700, 780), "y": range(500, 580)}