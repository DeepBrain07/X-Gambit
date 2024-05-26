import pygame
import time
from possiblePositions import PossiblePositions
from checkAvailablePositions import *

pygame.init()
win = pygame.display.set_mode((1000, 800))
win.fill((0,0,0))
counter = 0
box_size = 100

img_scale = (80,80)
small_img_scale = (65,65)

# White pieces
white_rook = pygame.image.load('backend/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, img_scale)
white_rook_small = pygame.transform.scale(white_rook, small_img_scale)
white_knight = pygame.image.load('backend/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, img_scale)
white_knight_small = pygame.transform.scale(white_knight, small_img_scale)
white_bishop = pygame.image.load('backend/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, img_scale)
white_bishop_small = pygame.transform.scale(white_bishop, small_img_scale)
white_queen = pygame.image.load('backend/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, img_scale)
white_queen_small = pygame.transform.scale(white_queen, small_img_scale)
white_king = pygame.image.load('backend/images/white king.png')
white_king = pygame.transform.scale(white_king, img_scale)
white_king_small = pygame.transform.scale(white_king, small_img_scale)
white_pawn = pygame.image.load('backend/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, img_scale)
white_pawn_small = pygame.transform.scale(white_pawn, small_img_scale)

# Black pieces
black_rook = pygame.image.load('backend/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, img_scale)
black_rook_small = pygame.transform.scale(black_rook, small_img_scale)
black_knight = pygame.image.load('backend/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, img_scale)
black_knight_small = pygame.transform.scale(black_knight, small_img_scale)
black_bishop = pygame.image.load('backend/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, img_scale)
black_bishop_small = pygame.transform.scale(black_bishop, small_img_scale)
black_queen = pygame.image.load('backend/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, img_scale)
black_queen_small = pygame.transform.scale(black_queen, small_img_scale)
black_king = pygame.image.load('backend/images/black king.png')
black_king = pygame.transform.scale(black_king, img_scale)
black_king_small = pygame.transform.scale(black_king, small_img_scale)
black_pawn = pygame.image.load('backend/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, img_scale)
black_pawn_small = pygame.transform.scale(black_pawn, small_img_scale)
white_pieces_all = {'rook': white_rook, 'knight': white_knight, 'bishop': white_bishop, 'queen': white_queen, 'king': white_king, 'pawn': white_pawn}
white_pos = {'rook': {'1':{'curr_pos': (0,0), 'pos_pos': []}, '2':{'curr_pos': (700,0), 'pos_pos': []}}, 'knight': {'1':{'curr_pos': (400,300), 'pos_pos': []}, '2':{'curr_pos': (600,0), 'pos_pos': []}},
             'bishop': {'1':{'curr_pos': (200,0), 'pos_pos': []}, '2':{'curr_pos': (500,0), 'pos_pos': []}}, 'queen': {'1':{'curr_pos': (300,0), 'pos_pos': []}}, 'king': {'1':{'curr_pos': (400,0), 'pos_pos': []}},
             'pawn': {'1':{'curr_pos': (0,100), 'pos_pos': [], 'moved': False}, '2':{'curr_pos': (100,100), 'pos_pos': [], 'moved': False}, '3':{'curr_pos': (200,100), 'pos_pos': [], 'moved': False}, '4':{'curr_pos': (300,100), 'pos_pos': [], 'moved': False}, '5':{'curr_pos': (400,100), 'pos_pos': [], 'moved': False}, '6':{'curr_pos': (500,100), 'pos_pos': [], 'moved': False}, '7':{'curr_pos': (600,100), 'pos_pos': [], 'moved': False}, '8':{'curr_pos': (700,100), 'pos_pos': [], 'moved': False}}}


black_pieces_all = {'rook': black_rook, 'knight': black_knight, 'bishop': black_bishop, 'queen': black_queen, 'king': black_king, 'pawn': black_pawn}
black_pos = {'rook': {'1':{'curr_pos': (0,600), 'pos_pos': []}, '2':{'curr_pos': (700,700), 'pos_pos': []}}, 'knight': {'1':{'curr_pos': (100,700), 'pos_pos': []}, '2':{'curr_pos': (600,700), 'pos_pos': []}},
             'bishop': {'1':{'curr_pos': (200,700), 'pos_pos': []}, '2':{'curr_pos': (500,700), 'pos_pos': []}}, 'queen': {'1':{'curr_pos': (300,700), 'pos_pos': []}}, 'king': {'1':{'curr_pos': (400,700), 'pos_pos': []}},
             'pawn': {'1':{'curr_pos': (0,200), 'pos_pos': [], 'moved': False}, '2':{'curr_pos': (100,600), 'pos_pos': [], 'moved': False}, '3':{'curr_pos': (200,600), 'pos_pos': [], 'moved': False}, '4':{'curr_pos': (300,600), 'pos_pos': [], 'moved': False}, '5':{'curr_pos': (400,600), 'pos_pos': [], 'moved': False}, '6':{'curr_pos': (500,600), 'pos_pos': [], 'moved': False}, '7':{'curr_pos': (600,600), 'pos_pos': [], 'moved': False}, '8':{'curr_pos': (700,600), 'pos_pos': [], 'moved': False}}}

def draw_pieces():
    # draws all the chess pieces on the board
    
    white_pieces = list(white_pos.keys()) # a list of all the white pieces
    for i in range(len(white_pieces)):
        piece = white_pieces[i]
        for j in range(len(list(white_pos[piece].keys()))):
            win.blit(white_pieces_all[piece], white_pos[piece][str(j+1)]['curr_pos'])
    
    
    black_pieces = list(black_pos.keys()) # a list of all the black pieces
    for i in range(len(black_pieces)):
        piece = black_pieces[i]
        for j in range(len(list(black_pos[piece].keys()))):
            win.blit(black_pieces_all[piece], black_pos[piece][str(j+1)]['curr_pos'])

def draw_board():
    rects = []
    iter = 1
    for i in range(9):
        if iter == 1:
            for j in range(iter, 9, 2):
                x = (j - 1) * box_size
                y = i * box_size
                rect = pygame.draw.rect(win, (125,0,0), (x, y, box_size, box_size))
                rect2 = pygame.draw.rect(win, (0,0,125), (x + box_size, y, box_size, box_size))
                rects.append(rect)
                rects.append(rect2)

            iter = 2
        elif iter == 2:
            for j in range(iter, 9, 2):
                x = (j - 1) * box_size
                y = i * box_size
                rect =pygame.draw.rect(win, (125,0,0), (x, y, box_size, box_size))
                rect2 = pygame.draw.rect(win, (0,0,125), (x - box_size, y, box_size, box_size))
                rects.append(rect)
                rects.append(rect2)
            iter = 1
    return rects

rects = draw_board()
draw_pieces()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for rect in rects:
                if rect.collidepoint(mouse_pos):
                    rects = draw_board()
                    draw_pieces()
                    clicked_pos = rect.topleft

                    piece, n = find_piece(black_pos, clicked_pos)
                    print(piece, n)
                    if piece and n:
                        curr_pos = black_pos[piece][n]['curr_pos']
                        
                        new_piece = PossiblePositions(black_pos[piece], piece)
                        pos_pos = black_pos[piece][n]['pos_pos']
                        if piece == 'rook':
                            available_pos = check_rook_available_positions(pos_pos, curr_pos, black_pos, white_pos)
                        elif piece == 'bishop':
                            available_pos = check_bishop_available_positions(pos_pos, curr_pos, black_pos, white_pos)
                        elif piece == 'knight':
                            available_pos = check_knight_available_positions(pos_pos, curr_pos, black_pos, white_pos)
                        elif piece == 'queen':
                            available_pos = check_queen_available_positions(pos_pos, curr_pos, black_pos, white_pos)
                        elif piece == 'king':
                            available_pos = check_king_available_positions(pos_pos, curr_pos, black_pos, white_pos)
                        elif piece == 'pawn':
                            available_pos = check_pawn_available_positions(pos_pos, curr_pos, black_pos, white_pos, n)
                        
                        for i in range(len(available_pos)):
                            x, y = available_pos[i]
                            x = x + 50
                            y = y + 50
                            pygame.draw.circle(win, (125,125,125), (x,y) , 10)
        
    pygame.display.flip()

