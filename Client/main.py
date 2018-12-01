import pygame
import Board
import Piece
import time

# Green Circle
#pygame.draw.circle(screen, GREEN, (250, 150), 500/8)
#pygame.draw.circle(screen, (BORDER_BLUE), (250, 150), 500/8, 5)
#pygame.draw.circle(screen, WHITE, (230, 130), 500/32)
#pygame.draw.circle(screen, WHITE, (270, 170), 500/32)
#pygame.draw.circle(screen, WHITE, (230, 170), 500/32)
#pygame.draw.circle(screen, WHITE, (270, 130), 500/32)
# Blue Circle
#pygame.draw.circle(screen, BLUE, (550, 150), 500/8)
#pygame.draw.circle(screen, (BORDER_BLUE), (550, 150), 500/8, 5)
#pygame.draw.circle(screen, WHITE, (800-230, 130), 500/32)
#pygame.draw.circle(screen, WHITE, (800-270, 170), 500/32)
#pygame.draw.circle(screen, WHITE, (800-230, 170), 500/32)
#pygame.draw.circle(screen, WHITE, (800-270, 130), 500/32)
# Red Circle
#pygame.draw.circle(screen, RED, (250, 450), 500/8)
#pygame.draw.circle(screen, (BORDER_BLUE), (250, 450), 500/8, 5)
#pygame.draw.circle(screen, WHITE, (230, 600-130), 500/32)
#pygame.draw.circle(screen, WHITE, (270, 600-170), 500/32)
#pygame.draw.circle(screen, WHITE, (230, 600-170), 500/32)
#pygame.draw.circle(screen, WHITE, (270, 600-130), 500/32)
# Yellow Circle
#pygame.draw.circle(screen, (255,255, 0), (550, 450), 500/8)
#pygame.draw.circle(screen, (BORDER_BLUE), (550, 450), 500/8, 5)
#pygame.draw.circle(screen, WHITE, (800-230, 600-130), 500/32)
#pygame.draw.circle(screen, WHITE, (800-270, 600-170), 500/32)
#pygame.draw.circle(screen, WHITE, (800-230, 600-170), 500/32)
#pygame.draw.circle(screen, WHITE, (800-270, 600-130), 500/32)
# Central Area
#DOT1 = [175 + SQUARE_SIDE * 6 + 2, 75 + SQUARE_SIDE * 6]
#DOT2 = [175 + SQUARE_SIDE * 9 + 2, 75 + SQUARE_SIDE * 6]
#DOT3 = [175 + SQUARE_SIDE * 6 + 2, 75 + SQUARE_SIDE * 9]
#DOT4 = [175 + SQUARE_SIDE * 9 + 2, 75 + SQUARE_SIDE * 9]
#CENTER = [400, 300]

pygame.init()
screen = pygame.display.set_mode((800, 600))
SQUARE_SIDE = 30

initialX = 387 - SQUARE_SIDE
xValues = [
        initialX, initialX, initialX, initialX, initialX, initialX,     # Column with 6 squares
        initialX - SQUARE_SIDE,
        initialX - SQUARE_SIDE,
        initialX - SQUARE_SIDE * 2,
        initialX - SQUARE_SIDE * 3,
        initialX - SQUARE_SIDE * 4,
        initialX - SQUARE_SIDE * 5,
        initialX - SQUARE_SIDE * 6,
        initialX - SQUARE_SIDE * 6,
        initialX - SQUARE_SIDE * 6,
        initialX - SQUARE_SIDE * 5,
        initialX - SQUARE_SIDE * 4,
        initialX - SQUARE_SIDE * 3,
        initialX - SQUARE_SIDE * 2,
        initialX - SQUARE_SIDE,
        initialX - SQUARE_SIDE,
        initialX, initialX, initialX, initialX, initialX, initialX,     # Column with 6 squares
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 3,
        initialX + SQUARE_SIDE * 3,
        initialX + SQUARE_SIDE * 4,
        initialX + SQUARE_SIDE * 5,
        initialX + SQUARE_SIDE * 6,
        initialX + SQUARE_SIDE * 7,
        initialX + SQUARE_SIDE * 8,
        initialX + SQUARE_SIDE * 8,
        initialX + SQUARE_SIDE * 8,
        initialX + SQUARE_SIDE * 7,
        initialX + SQUARE_SIDE * 6,
        initialX + SQUARE_SIDE * 5,
        initialX + SQUARE_SIDE * 4,
        initialX + SQUARE_SIDE * 3,
        initialX + SQUARE_SIDE * 3,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE * 2,
        initialX + SQUARE_SIDE,
        # Reds
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        # Greens
        initialX - SQUARE_SIDE * 5,
        initialX - SQUARE_SIDE * 4,
        initialX - SQUARE_SIDE * 3,
        initialX - SQUARE_SIDE * 2,
        initialX - SQUARE_SIDE,
        # Blues
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        initialX + SQUARE_SIDE,
        # Yellows
        initialX + SQUARE_SIDE * 7,
        initialX + SQUARE_SIDE * 6,
        initialX + SQUARE_SIDE * 5,
        initialX + SQUARE_SIDE * 4,
        initialX + SQUARE_SIDE * 3
]
initialY = 600 - 75 - SQUARE_SIDE
yValues = [
        initialY,
        initialY - SQUARE_SIDE,
        initialY - SQUARE_SIDE * 2,
        initialY - SQUARE_SIDE * 3,
        initialY - SQUARE_SIDE * 4,
        initialY - SQUARE_SIDE * 5,
        initialY - SQUARE_SIDE * 5,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 9,
        initialY - SQUARE_SIDE * 9,
        initialY - SQUARE_SIDE * 10,
        initialY - SQUARE_SIDE * 11,
        initialY - SQUARE_SIDE * 12,
        initialY - SQUARE_SIDE * 13,
        initialY - SQUARE_SIDE * 14,
        initialY - SQUARE_SIDE * 14,
        initialY - SQUARE_SIDE * 14,
        initialY - SQUARE_SIDE * 13,
        initialY - SQUARE_SIDE * 12,
        initialY - SQUARE_SIDE * 11,
        initialY - SQUARE_SIDE * 10,
        initialY - SQUARE_SIDE * 9,
        initialY - SQUARE_SIDE * 9,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 8,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 6,
        initialY - SQUARE_SIDE * 5,
        initialY - SQUARE_SIDE * 5,
        initialY - SQUARE_SIDE * 4,
        initialY - SQUARE_SIDE * 3,
        initialY - SQUARE_SIDE * 2,
        initialY - SQUARE_SIDE,
        initialY,
        initialY,
        # Reds
        initialY - SQUARE_SIDE,
        initialY - SQUARE_SIDE * 2,
        initialY - SQUARE_SIDE * 3,
        initialY - SQUARE_SIDE * 4,
        initialY - SQUARE_SIDE * 5,
        # Greens
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        # Blues
        initialY - SQUARE_SIDE * 13,
        initialY - SQUARE_SIDE * 12,
        initialY - SQUARE_SIDE * 11,
        initialY - SQUARE_SIDE * 10,
        initialY - SQUARE_SIDE * 9,
        # Yellows
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
        initialY - SQUARE_SIDE * 7,
]

board = Board.Board()
piece = Piece.Piece()

done = False
i = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    board.drawBoard(screen)
    piece.drawRedPiece(screen, xValues[i], yValues[i], 30)
    time.sleep(0.3)
    i+=1

    pygame.display.flip()