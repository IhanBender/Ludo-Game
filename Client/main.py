import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

BACKGROUND_IMAGE = pygame.image.load("images/woodbg.jpg")

BORDER_BLUE = (100,100,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)

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
        initialX + SQUARE_SIDE
]

initialY = 600-75-SQUARE_SIDE
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
        initialY
]

done = False

def drawBoard():
    # background
    screen.fill([255, 255, 255])
    screen.blit(BACKGROUND_IMAGE, BACKGROUND_IMAGE.get_rect())
    # Board
    pygame.draw.rect(screen, WHITE, pygame.Rect(150, 50, 500, 500))
    pygame.draw.rect(screen, (BORDER_BLUE), [150, 50, 500, 500], 5)
    pygame.draw.rect(screen, (BORDER_BLUE), [160, 60, 480, 480], 2)
    # Circles
    # Green Circle
    pygame.draw.circle(screen, GREEN, (250, 150), 500/8)
    pygame.draw.circle(screen, (BORDER_BLUE), (250, 150), 500/8, 5)
    pygame.draw.circle(screen, WHITE, (230, 130), 500/32)
    pygame.draw.circle(screen, WHITE, (270, 170), 500/32)
    pygame.draw.circle(screen, WHITE, (230, 170), 500/32)
    pygame.draw.circle(screen, WHITE, (270, 130), 500/32)
    # Blue Circle
    pygame.draw.circle(screen, BLUE, (550, 150), 500/8)
    pygame.draw.circle(screen, (BORDER_BLUE), (550, 150), 500/8, 5)
    pygame.draw.circle(screen, WHITE, (800-230, 130), 500/32)
    pygame.draw.circle(screen, WHITE, (800-270, 170), 500/32)
    pygame.draw.circle(screen, WHITE, (800-230, 170), 500/32)
    pygame.draw.circle(screen, WHITE, (800-270, 130), 500/32)
    # Red Circle
    pygame.draw.circle(screen, RED, (250, 450), 500/8)
    pygame.draw.circle(screen, (BORDER_BLUE), (250, 450), 500/8, 5)
    pygame.draw.circle(screen, WHITE, (230, 600-130), 500/32)
    pygame.draw.circle(screen, WHITE, (270, 600-170), 500/32)
    pygame.draw.circle(screen, WHITE, (230, 600-170), 500/32)
    pygame.draw.circle(screen, WHITE, (270, 600-130), 500/32)
    # Yellow Circle
    pygame.draw.circle(screen, (255,255, 0), (550, 450), 500/8)
    pygame.draw.circle(screen, (BORDER_BLUE), (550, 450), 500/8, 5)
    pygame.draw.circle(screen, WHITE, (800-230, 600-130), 500/32)
    pygame.draw.circle(screen, WHITE, (800-270, 600-170), 500/32)
    pygame.draw.circle(screen, WHITE, (800-230, 600-170), 500/32)
    pygame.draw.circle(screen, WHITE, (800-270, 600-130), 500/32)
    # Central Area
    DOT1 = [175 + SQUARE_SIDE * 6 + 2, 75 + SQUARE_SIDE * 6]
    DOT2 = [175 + SQUARE_SIDE * 9 + 2, 75 + SQUARE_SIDE * 6]
    DOT3 = [175 + SQUARE_SIDE * 6 + 2, 75 + SQUARE_SIDE * 9]
    DOT4 = [175 + SQUARE_SIDE * 9 + 2, 75 + SQUARE_SIDE * 9]
    CENTER = [400, 300]

    #pygame.draw.rect(screen, BORDER_BLUE, pygame.Rect(175+ SQUARE_SIDE*5+2, 75 + SQUARE_SIDE * 9, SQUARE_SIDE, SQUARE_SIDE), 2)   
    #pygame.draw.rect(screen, BORDER_BLUE, pygame.Rect(800-x-SQUARE_SIDE + 1, 75 + SQUARE_SIDE * 9, SQUARE_SIDE, SQUARE_SIDE), 2)   

    pygame.draw.polygon(screen, BLUE, [DOT1, DOT2, CENTER])
    pygame.draw.polygon(screen, GREEN, [DOT1, DOT3, CENTER])
    pygame.draw.polygon(screen, RED, [DOT3, DOT4, CENTER])
    pygame.draw.polygon(screen, YELLOW, [DOT2, DOT4, CENTER])
    #pygame.draw.polygon(screen, WHITE, [[100, 100], [0, 200], [200, 200]])
    #pygame.draw.polygon(screen, WHITE, [[100, 100], [0, 200], [200, 200]])
    #pygame.draw.polygon(screen, WHITE, [[100, 100], [0, 200], [200, 200]])

    pygame.draw.polygon(screen, WHITE, [DOT1, DOT2, CENTER], 3)
    pygame.draw.polygon(screen, WHITE, [DOT1, DOT3, CENTER], 3)
    #pygame.draw.polygon(screen, RED, [[100, 100], [0, 200], [200, 200]], 5)
    #pygame.draw.polygon(screen, GREEN, [[100, 100], [0, 200], [200, 200]], 5)
    #pygame.draw.polygon(screen, YELLOW, [[100, 100], [0, 200], [200, 200]], 5)
    # Squares
    y = 75
    x = 175
    for i in range (5):
        y = y + SQUARE_SIDE
        x = x + SQUARE_SIDE
        # Blue
        pygame.draw.rect(screen, BLUE, pygame.Rect(387, y, SQUARE_SIDE, SQUARE_SIDE))
        pygame.draw.rect(screen, WHITE, pygame.Rect(387, y, SQUARE_SIDE, SQUARE_SIDE), 2)
        # Red
        pygame.draw.rect(screen, RED, pygame.Rect(387, 600-SQUARE_SIDE-y, SQUARE_SIDE, SQUARE_SIDE))
        pygame.draw.rect(screen, WHITE, pygame.Rect(387, 600-SQUARE_SIDE-y, SQUARE_SIDE, SQUARE_SIDE), 2)
        # Green
        pygame.draw.rect(screen, GREEN, pygame.Rect(x+2, 75 + SQUARE_SIDE * 7, SQUARE_SIDE, SQUARE_SIDE))
        pygame.draw.rect(screen, WHITE, pygame.Rect(x+2, 75 + SQUARE_SIDE * 7, SQUARE_SIDE, SQUARE_SIDE), 2)
        # Yellow
        pygame.draw.rect(screen, YELLOW, pygame.Rect(800-x-SQUARE_SIDE + 1, 75 + SQUARE_SIDE * 7, SQUARE_SIDE, SQUARE_SIDE))
        pygame.draw.rect(screen, WHITE, pygame.Rect(800-x-SQUARE_SIDE + 1, 75 + SQUARE_SIDE * 7, SQUARE_SIDE, SQUARE_SIDE), 2)

    for i in range(len(xValues)):
        pygame.draw.rect(screen, BORDER_BLUE, pygame.Rect(xValues[i], yValues[i], SQUARE_SIDE, SQUARE_SIDE), 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    drawBoard()
    pygame.display.flip()