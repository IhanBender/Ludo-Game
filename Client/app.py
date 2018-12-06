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
import netifaces as ni

interfaces = ni.interfaces()
if 'wlp3s0' in interfaces:
    ip = ni.ifaddresses('wlp3s0')[ni.AF_INET][0]['addr']
else:
    ip = '192.168.0.8'

def insideStartGame((x,y)):
    if x >= 0 and y >= 0:
        return True
    return False

def draw(state):
    screen.blit(state['screen'], state['screen'].get_rect())

    pygame.display.flip()

name = raw_input('Por favor, digite o seu nome de usuário: ')
# Conecta ao servidor
HOST = ip              # Endereco IP do Servidor
PORT = 4000            # Porta que o Servidor esta
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
    #'screen' : inicialScreen,
    'screen' : inicialScreen,
    'gamestate' : []
}

done = False
screenChange = True
screen.fill([255, 255, 255])
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if  (pygame.mouse.get_pressed()[0] == 1) and \
        (insideStartGame(pygame.mouse.get_pos())) and \
        state['screen'] == inicialScreen:
            startTime = time.time()
            state['inqueue'] = True
            tcp.send(protocol.QueueMessage())
            print "Buscando Partida"
            state['screen'] = searchClick
            draw(state)
            state['screen'] = searching
            draw(state)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    if screenChange:
        # piecedrawer.drawRedPiece(screen, coords.yellowFinals[0], 15)
        # dice.drawDice(screen, 0)
        draw(state)
        screenChange = False

#msg = raw_input()
#while msg <> '\x18':
#    tcp.send (msg)
#    msg = raw_input()
tcp.close()