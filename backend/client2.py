import socket
from player import Player
import pygame
import json

pygame.init()
win = pygame.display.set_mode((500, 500))
player = Player(1)
def game():
    width = 60
    height = 60
    vel = 5

    x, y = player.get_pos()
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel
        pos = player.set_pos(x, y)
        # get player's position then send it to the server
        print(pos)

        c = socket.socket()
        c.connect(('192.168.1.179', 9999))
        c.send(bytes(json.dumps(player.__dict__), 'utf-8'))
        playersPos = (json.loads(c.recv(1024).decode()))
        win.fill((0,0,0))
        pygame.draw.rect(win, (0,125,0), (x, y, width, height))
        pygame.draw.rect(win, (125,0,0), (playersPos['0'][0], playersPos['0'][1], width, height))
        pygame.display.update()
    
    pygame.quit()
game()