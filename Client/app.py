#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import pygame
from board import Board
from pieceDrawer import PieceDrawer
from dice import Dice
from coordinates import Coordinates
import protocol
import datetime
import time
import json

def messageType(msg):
    return msg.split(' ')[0]

def insideStartGame((x,y)):
    if x in range(280, 520) and y in range(260, 340):
        return True
    return False

def param1(msg):
    return msg.split(' ')[1]

def enterQueue():
    startTime = time.time()
    tcp.send(protocol.QueueMessage())
    print "Buscando Partida"
    msg = tcp.recv(1024)
    if messageType(msg) == '/CONFIRM':
        state['inqueue'] = True
        state['screen'] = searchClick
        drawBackground()
        draw()
        state['screen'] = searching
        drawBackground()
        draw()
        return True
    elif messageType(msg) == '/BEGIN':
        enterGame(param1(msg))
    return False

def enterGame(currentMatch):
    print "Partida encontrada"
    state['currentMatch'] = currentMatch
    state['ingame'] = True
    state['screen'] = board.BACKGROUND_IMAGE
    drawBackground()
    requestState()
    draw()

def requestState():
    if state["ingame"]:
        tcp.send('/STATE ' + state['currentMatch'])
        msg = tcp.recv(1024)
        if messageType(msg) == '/UPDATE':
            state['gamestate'] = json.loads(param1(msg))
            if isMyTurn():
                dice.drawDice(screen, 0)

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

            return True
    return False

def isMyTurn():
    return str(state['gamestate']['currentTurn']) \
    == str(state['gamestate']['players'][name])

def diceHit((x, y)):
    hitbox = dice.hitbox()
    if x in hitbox["x"] and y in hitbox["y"]:
        return True
    return False

def pieceHit((x, y)):
    print (state['gamestate']['playerIndex'])
    if state['gamestate']['playerIndex'] == 0:
        positions = state['gamestate']['red']
    elif state['gamestate']['playerIndex'] == 1:
        positions = state['gamestate']['green']
    elif state['gamestate']['playerIndex'] == 2:
        positions = state['gamestate']['blue']
    else: #state['gamestate']['playerIndex'] == 3
        positions = state['gamestate']['yellow']

    for i in range(0,4):
        if x > positions[i][0] and x < positions[i][0] + coords.SQUARE_SIDE \
        and y > positions[i][1] and y < positions[i][1] + coords.SQUARE_SIDE:
            return i

    return -1

def rollDice():
    if not state['rolling']:
        state['rolling'] = True
        tcp.send('/DICE ' + state['currentMatch'])
        dice.drawDice(screen, 0)
        draw()
        msg = tcp.recv(1024)
        if messageType(msg) == '/DICE':
            roll = int(param1(msg))
            dice.drawDice(screen, roll)
            time.sleep(0.7)
            draw()
            return roll
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
ip = '192.168.0.102'
HOST = ip              # Endereco IP do Servidor
PORT = 5000       # Porta que o Servidor esta
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
    if not msg: break
    if msg.split(' ')[0] == '/DENY':
        name = raw_input('Nome de usuário já utilizado, digite um novo: ')
    elif msg.split(' ')[0] == '/CONFIRM':
        print("Bem vindo ao jogo " + name)
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
    'currentMatch' : '',
    #'screen' : inicialScreen,
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

        if diceHit(pygame.mouse.get_pos()) and \
            state['screen'] == board.BACKGROUND_IMAGE and \
            state['ingame']:
                if isMyTurn() and state['gamestate']['currentPlay'] == 'dice':
                    roll = rollDice()
                    if roll:
                        state['rolling'] = False

        if state['screen'] == board.BACKGROUND_IMAGE and \
            state['ingame'] and \
            pieceHit(pygame.mouse.get_pos()) != -1:
                piece = pieceHit(pygame.mouse.get_pos())
                if isMyTurn() and state['gamestate']['currentPlay'] == 'move':
                    move = movePiece(piece)
                    #if move:
                        # Informe usuário que a jogada foi bem sucedida
                    #else:
                        # Informe que deve fazer outra jogada

        if  (pygame.mouse.get_pressed()[0] == 1):
            if (insideStartGame(pygame.mouse.get_pos())) and \
            state['screen'] == inicialScreen:
                if enterQueue():
                    msg = tcp.recv(1024)
                    if messageType(msg) == '/BEGIN':
                        enterGame(param1(msg))
                    elif messageType(msg) == '/CONFIRM':
                        msg = tcp.recv(1024)
                        if messageType(msg) == '/BEGIN':
                            enterGame(param1(msg))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                tcp.send('/EXIT')
                done = True


        requestState()

    # If ingame, draw current state
tcp.close()