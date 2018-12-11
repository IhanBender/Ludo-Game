#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pygame
from board import Board
from pieceDrawer import PieceDrawer
from dice import Dice
from coordinates import Coordinates
import datetime
import time
import json

HOST = '192.168.0.16'  # Endereco IP do Servidor
PORT = 4000       # Porta que o Servidor esta


def messageType(msg):
    return msg.split(' ')[0]

def insideStartGame((x,y)):
    if x in range(280, 520) and y in range(260, 340):
        return True
    return False

def insideContinuar((x,y)):
    if x in range(280, 520) and y in range(460, 540):
        return True
    return False

def param1(msg):
    return msg.split(' ')[1]

def enterQueue():
    #startTime = time.time()
    tcp.send('/QUEUE')
    print "Buscando Partida"
    msg = tcp.recv(1024)
    if messageType(msg) == '/CONFIRM':
        state['inqueue'] = True
        # Animação
        state['screen'] = searchClick
        drawBackground()
        draw()
        # Tela de buscando partida
        state['screen'] = searching
        drawBackground()
        draw()
        return True
    elif messageType(msg) == '/BEGIN':
        enterGame(param1(msg))
        return True

    return False

def enterGame(currentMatch):
    print "Partida encontrada"
    state['currentMatch'] = currentMatch
    state['ingame'] = True
    state['inqueue'] = False
    state['inendscreen'] = False
    state['screen'] = board.BACKGROUND_IMAGE
    drawBackground()
    requestState()
    draw()


def checkWinner():
    if state['gamestate']['winner'] != '-1':
        if state['gamestate']['winner'] == \
        state['gamestate']['playerIndex']:
            state['screen'] = VICTORY_SCREEN
        else:
            state['screen'] = DEFEAT_SCREEN
    
        state['inendscreen'] = True
        state['ingame'] = False
        drawBackground()
        draw()

        tcp.send('/EXIT')
        msg = tcp.recv(1024)

        return True
    return False
            

def requestState():
    if state["ingame"]:
        tcp.send('/STATE')
        msg = tcp.recv(1024)
        if messageType(msg) == '/UPDATE':
            oldstate = state['gamestate']
            state['gamestate'] = json.loads(param1(msg))

            if oldstate != state['gamestate']:
                if checkWinner():
                    return       

                drawBackground()
                screen.blit(turnIndicators[int(state['gamestate']['currentTurn'])], (0, 0))
                if isMyTurn():
                    # Draw my colored dice without value
                    if state['gamestate']['currentPlay'] == 'dice':
                        dice.drawDice(screen, 7, state['gamestate']['currentTurn'])
                    else:
                        # Draw my colored dice with value
                        dice.drawDice(screen,   \
                        int(state['gamestate']['dice']), \
                        state['gamestate']['currentTurn'])
                else: #Not my turn
                    if state['gamestate']['currentPlay'] == 'dice':
                        # Draw normal dice without value
                        dice.drawDice(screen, 0)
                    else:
                        # Draw normal dice with value
                        dice.drawDice(screen, int(state['gamestate']['dice']))

                # Draw pieces
                positions = []
                for value in state['gamestate']['red']:
                    positions.append([int(value[0]), int(value[1])])
                for position in positions:
                    if position in coords.redFinals:
                        piecedrawer.drawRedPiece(screen, position, 15)
                    else:
                        piecedrawer.drawRedPiece(screen, position, 30)

                positions = []
                for value in state['gamestate']['green']:
                    positions.append([int(value[0]), int(value[1])])
                for position in positions:
                    if position in coords.greenFinals:
                        piecedrawer.drawGreenPiece(screen, position, 15)
                    else:
                        piecedrawer.drawGreenPiece(screen, position, 30)

                positions = []
                for value in state['gamestate']['blue']:
                    positions.append([int(value[0]), int(value[1])])
                for position in positions:
                    if position in coords.blueFinals:
                        piecedrawer.drawBluePiece(screen, position, 15)
                    else:
                        piecedrawer.drawBluePiece(screen, position, 30)

                positions = []
                for value in state['gamestate']['yellow']:
                    positions.append([int(value[0]), int(value[1])])
                for position in positions:
                    if position in coords.yellowFinals:
                        piecedrawer.drawYellowPiece(screen, position, 15)
                    else:
                        piecedrawer.drawYellowPiece(screen, position, 30)
                draw()

            return True
    return False

def isMyTurn():
    return str(state['gamestate']['currentTurn']) \
    == str(state['gamestate']['playerIndex'])

def diceHit((x, y)):
    hitbox = dice.hitbox()
    if x in hitbox["x"] and y in hitbox["y"]:
        return True
    return False

def pieceHit((x, y)):
    pIndex = int(state['gamestate']['playerIndex'])
    if pIndex == 0:
        positions = state['gamestate']['red']
    elif pIndex == 1:
        positions = state['gamestate']['green']
    elif pIndex == 2:
        positions = state['gamestate']['blue']
    else: #pIndex
        positions = state['gamestate']['yellow']

    for i in range(0,4):
        if x > int(positions[i][0]) and x < int(positions[i][0]) + coords.SQUARE_SIDE \
        and y > int(positions[i][1]) and y < int(positions[i][1]) + coords.SQUARE_SIDE:
            return i

    return -1

def rollDice():
    if not state['rolling']:
        state['rolling'] = True
        tcp.send('/DICE')
        msg = tcp.recv(1024)
        if messageType(msg) == '/CONFIRM':
            dice.drawDice(screen, 0, state['gamestate']['playerIndex'])
            draw()
            tcp.send('/STATE')
            msg = tcp.recv(1024)
            if messageType(msg) == '/UPDATE':
                state['gamestate'] = json.loads(param1(msg))
                dice.drawDice(screen, int(state['gamestate']['dice']), state['gamestate']['playerIndex'])
                time.sleep(0.7)
                draw()
                return True

        return False
    return False

def movePiece(piece):
    tcp.send('/MOVE' + ' ' + str(piece))
    msg = tcp.recv(1024)
    if messageType(msg) == '/CONFIRM':
        return True
    # /DENY
    return False

def drawBackground():
    screen.blit(state['screen'], state['screen'].get_rect())

def draw():
    pygame.display.flip()

name = raw_input('Por favor, digite o seu nome de usuário: ')
# Conecta ao servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
# Tenta conectar ao servidor
print ("Trying to connect")
tcp.connect(dest)

# Verifica o nome
while True:
    print ("Verifying username")
    tcp.send('/USERNAME ' + name)
    print ("Waiting answer")
    msg = tcp.recv(1024)

    if msg.split(' ')[0] == '/DENY':
        name = raw_input('Nome de usuário já utilizado, digite um novo: ')
    elif msg.split(' ')[0] == '/CONFIRM':
        print("Bem vindo ao jogo, " + name)
        break

# Inicializa jogo
pygame.init()
initialScreen = pygame.image.load("images/main_menu.jpg")
searchClick = pygame.image.load("images/main_menu2.jpg")
searching = pygame.image.load("images/buscando3.png")
turnIndicators = [
    pygame.image.load("images/turnRed.png"),
    pygame.image.load("images/turnGreen.png"),
    pygame.image.load("images/turnBlue.png"),
    pygame.image.load("images/turnYellow.png"),
]
VICTORY_SCREEN = pygame.image.load("images/vitoria1.png")
VITORIA_ANIM = pygame.image.load("images/vitoria2.png")
DEFEAT_SCREEN = pygame.image.load("images/derrota1.png")
DEFEAT_ANIM = pygame.image.load("images/derrota2.png")

screen = pygame.display.set_mode((800, 600))

coords = Coordinates()
board = Board()
piecedrawer = PieceDrawer()
dice = Dice()

startTime = 0.0

state = {
    'inqueue' : False,
    'ingame' : False,
    'inendscreen' : False,
    'rolling': False,
    'screen' : initialScreen,
    'gamestate' : {}
}

drawBackground()
draw()

done = False
screen.fill([255, 255, 255])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Mouse pressed events
        if  (pygame.mouse.get_pressed()[0] == 1):
            # Buscar partida
            if (insideStartGame(pygame.mouse.get_pos())) and \
            state['screen'] == initialScreen:
                if enterQueue() and state['inqueue']:
                    msg = tcp.recv(1024)
                    if messageType(msg) == '/BEGIN':
                        enterGame(param1(msg))

            # Rolar dado
            if diceHit(pygame.mouse.get_pos()) and \
            state['screen'] == board.BACKGROUND_IMAGE and \
            state['ingame']:
                if isMyTurn() and state['gamestate']['currentPlay'] == 'dice':
                    roll = rollDice()
                    if roll:
                        state['rolling'] = False
            # Mover peça
            if state['screen'] == board.BACKGROUND_IMAGE and \
            state['ingame']:
                piece_hit = pieceHit(pygame.mouse.get_pos())
                if piece_hit != -1:
                    if isMyTurn() and state['gamestate']['currentPlay'] == 'piece':
                        move = movePiece(piece_hit)
                        #####
                        #if move:
                            # Informe usuário que a jogada foi bem sucedida
                        #else:
                            # Informe que deve fazer outra jogada

            # Sair da tela de fim da partida
            if (state['screen'] == VICTORY_SCREEN or    \
            state['screen'] == DEFEAT_SCREEN) \
            and state['inendscreen']:
                if insideContinuar(pygame.mouse.get_pos()):
                    if state['screen'] == VICTORY_SCREEN:
                        state['screen'] = VITORIA_ANIM
                    else:
                        state['screen'] = DEFEAT_ANIM
                    drawBackground()
                    draw()
                    time.sleep(0.7)       
                    state['inendscreen'] = False
                    state['gamestate'] = {}
                    state['screen']  = initialScreen  
                    drawBackground()
                    draw()


        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Sai da partida (se tiver)
                tcp.send('/EXIT')
                # Sinaliza saida do loop principal
                done = True


        requestState()

    # If ingame, draw current state
tcp.close()