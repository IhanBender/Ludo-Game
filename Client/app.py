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
            return True
    return False

def isMyTurn():
    return str(state['gamestate']['currentTurn']) == str(state['gamestate']['players'][name])

def diceHit((x, y)):
    hitbox = dice.hitbox()
    if x in hitbox["x"] and y in hitbox["y"]:
        return True
    return False

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
            print roll
            return roll
        return False
    return False

def drawBackground():
    screen.blit(state['screen'], state['screen'].get_rect())

def draw():
    pygame.display.flip()

name = raw_input('Por favor, digite o seu nome de usuário: ')
# Conecta ao servidor
ip = '192.168.0.13'
HOST = ip              # Endereco IP do Servidor
PORT = 10000       # Porta que o Servidor esta
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
        if  (pygame.mouse.get_pressed()[0] == 1):
            if (insideStartGame(pygame.mouse.get_pos())) and \
            state['screen'] == inicialScreen:
                if enterQueue():
                    msg = tcp.recv(1024)
                    if messageType(msg) == '/BEGIN':
                        enterGame(param1(msg))

            if diceHit(pygame.mouse.get_pos()) and \
            state['screen'] == board.BACKGROUND_IMAGE and \
            state['ingame']:
                if isMyTurn():
                    roll = rollDice()
                    if roll:
                        state['rolling'] = False
                    # Movement

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

        requestState()

#msg = raw_input()
#while msg <> '\x18':
#    tcp.send (msg)
#    msg = raw_input()
tcp.close()