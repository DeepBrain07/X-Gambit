import pygame
import time
from possiblePositions import PossiblePositions

pygame.init()
win = pygame.display.set_mode((1000, 800))
win.fill((0,0,0))
counter = 0
iter = 1
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
white_pos = {'rook': {'1':{'curr_pos': (0,0), 'pos_pos': []}, '2':{'curr_pos': (700,0), 'pos_pos': []}}, 'knight': {'1':{'curr_pos': (100,0), 'pos_pos': []}, '2':{'curr_pos': (600,0), 'pos_pos': []}},
             'bishop': {'1':{'curr_pos': (200,0), 'pos_pos': []}, '2':{'curr_pos': (500,0), 'pos_pos': []}}, 'queen': {'1':{'curr_pos': (300,0), 'pos_pos': []}}, 'king': {'1':{'curr_pos': (400,0), 'pos_pos': []}},
             'pawn': {'1':{'curr_pos': (0,100), 'pos_pos': []}, '2':{'curr_pos': (100,100), 'pos_pos': []}, '3':{'curr_pos': (200,100), 'pos_pos': []}, '4':{'curr_pos': (300,100), 'pos_pos': []}, '5':{'curr_pos': (400,100), 'pos_pos': []}, '6':{'curr_pos': (500,100), 'pos_pos': []}, '7':{'curr_pos': (600,100), 'pos_pos': []}, '8':{'curr_pos': (700,100), 'pos_pos': []}}}

black_pieces_all = {'rook': black_rook, 'knight': black_knight, 'bishop': black_bishop, 'queen': black_queen, 'king': black_king, 'pawn': black_pawn}
black_pos = {'rook': {'1':{'curr_pos': (0,700), 'pos_pos': []}, '2':{'curr_pos': (700,700), 'pos_pos': []}}, 'knight': {'1':{'curr_pos': (100,700), 'pos_pos': []}, '2':{'curr_pos': (600,700), 'pos_pos': []}},
             'bishop': {'1':{'curr_pos': (200,700), 'pos_pos': []}, '2':{'curr_pos': (500,700), 'pos_pos': []}}, 'queen': {'1':{'curr_pos': (300,700), 'pos_pos': []}}, 'king': {'1':{'curr_pos': (400,700), 'pos_pos': []}},
             'pawn': {'1':{'curr_pos': (0,600), 'pos_pos': []}, '2':{'curr_pos': (100,600), 'pos_pos': []}, '3':{'curr_pos': (200,600), 'pos_pos': []}, '4':{'curr_pos': (300,600), 'pos_pos': []}, '5':{'curr_pos': (400,600), 'pos_pos': []}, '6':{'curr_pos': (500,600), 'pos_pos': []}, '7':{'curr_pos': (600,600), 'pos_pos': []}, '8':{'curr_pos': (700,600), 'pos_pos': []}}}

# black_pos = {'rook': [[(0,700), (700,700)], black_rook], 'knight': [[(100,700), (600,700)], black_knight], 'bishop': [[(200,700), (500,700)], black_bishop],
#              'queen': [[(300,700)], black_queen], 'king': [[(400,700)], black_king], 'pawn': [[(0,600), (100,600), (200,600), (300,600), (400,600), (500,600), (600,600), (700,600)], black_pawn]} 

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

for i in range(9):
    if iter == 1:
        for j in range(iter, 9, 2):
            x = (j - 1) * box_size
            y = i * box_size
            pygame.draw.rect(win, (125,0,0), (x, y, box_size, box_size))
            pygame.display.update()
        iter = 2
    elif iter == 2:
        for j in range(iter, 9, 2):
            x = (j - 1) * box_size
            y = i * box_size
            pygame.draw.rect(win, (125,0,0), (x, y, box_size, box_size))
            pygame.display.update()
        iter = 1
    draw_pieces()
    rook_possible_positions = PossiblePositions(white_pos['king'])
    pos_pos = rook_possible_positions.king()
    for i in range(len(pos_pos)):
        x, y = pos_pos[i]
        x = x + 50
        y = y + 50
        pygame.draw.circle(win, (125,125,125), (x,y) , 10)
iter = 1



time.sleep(10)