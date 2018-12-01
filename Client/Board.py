import pygame

class Board:

        def __init__(self):
                self.BACKGROUND_IMAGE = pygame.image.load("images/board.png")

        def drawBoard(self, screen):
            # background
            screen.fill([255, 255, 255])
            screen.blit(self.BACKGROUND_IMAGE, self.BACKGROUND_IMAGE.get_rect())
    
