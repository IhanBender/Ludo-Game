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

HOST = '192.168.0.8'  # Endereco IP do Servidor
PORT = 6000       # Porta que o Servidor esta


def messageType(msg):
    return msg.split(' ')[0]

def insideStartGame((x,y)):
    if x in range(280, 520) and y in range(260, 340):
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
    state['screen'] = board.BACKGROUND_IMAGE
    drawBackground()
    requestState()
    draw()

def requestState():
    if state["ingame"]:
        tcp.send('/STATE')
        msg = tcp.recv(1024)
        if messageType(msg) == '/UPDATE':
            oldstate = state['gamestate']
            state['gamestate'] = json.loads(param1(msg))

            if oldstate != state['gamestate']:
                drawBackground()
                # Draw dice with value
                if isMyTurn():
                    if state['gamestate']['currentPlay'] == 'dice':
                        dice.drawDice(screen, 0)
                    else:
                        dice.drawDice(screen,int(state['gamestate']['dice']))

                # Draw pieces
                for position in state['gamestate']['red']:
                    if position in coords.redFinals:
                        piecedrawer.drawRedPiece(screen, position, 15)
                    else:
                        piecedrawer.drawRedPiece(screen, position, 30)
                for position in state['gamestate']['green']:
                    if position in coords.greenFinals:
                        piecedrawer.drawGreenPiece(screen, position, 15)
                    else:
                        piecedrawer.drawGreenPiece(screen, position, 30)
                for position in state['gamestate']['blue']:
                    if position in coords.blueFinals:
                        piecedrawer.drawBluePiece(screen, position, 15)
                    else:
                        piecedrawer.drawBluePiece(screen, position, 30)
                for position in state['gamestate']['yellow']:
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

    #print positions
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
            dice.drawDice(screen, 0)
            draw()
            tcp.send('/STATE')
            msg = tcp.recv(1024)
            if messageType(msg) == '/UPDATE':
                state['gamestate'] = json.loads(param1(msg))
                dice.drawDice(screen, int(state['gamestate']['dice']))
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
inicialScreen = pygame.image.load("images/main_menu.jpg")
searchClick = pygame.image.load("images/main_menu2.jpg")
searching = pygame.image.load("images/buscando3.png")
screen = pygame.display.set_mode((800, 600))

coords = Coordinates()
board = Board()
piecedrawer = PieceDrawer()
dice = Dice()

startTime = 0.0

state = {
    'inqueue' : False,
    'ingame' : False,
    'rolling': False,
    'screen' : inicialScreen,
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
            state['screen'] == inicialScreen:
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
                        #if move:
                            # Informe usuário que a jogada foi bem sucedida
                        #else:
                            # Informe que deve fazer outra jogada

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Sai da partida (se tiver)
                tcp.send('/EXIT')
                # Sinaliza saida do loop principal
                done = True


        requestState()

    # If ingame, draw current state
tcp.close()