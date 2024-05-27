class PossiblePositions:
    def __init__(self, piece, piece_name, type='white') -> None:
        self.piece = piece
        self.piece_name = piece_name
        self.box_size = 100
        if self.piece_name == 'rook':
            self.rook()
        elif self.piece_name == 'bishop':
            self.bishop()
        elif self.piece_name == 'knight':
            self.knight()
        elif self.piece_name == 'queen':
            self.queen()
        elif self.piece_name == 'king':
            self.king()
        elif self.piece_name == 'pawn':
            self.pawn(type)

    def rook(self):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            x, y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x = x
                y -= self.box_size
                if ((y >= 0 and y <=700) and (x >= 0 and x <=700)):
                    pos_pos.append((x,y))
                else:
                    break
        
            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x = x
                y += self.box_size
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break
            
            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x -= self.box_size
                y = y
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break

            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x += self.box_size
                y = y
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)
    
    def knight(self):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            x, y = curr_pos
            if ((x+(self.box_size*2) >= 0 and x+(self.box_size*2) <= 700) and (y-self.box_size >= 0 and y-self.box_size <= 700)):
                pos_pos.append((x+(self.box_size*2), y-self.box_size))
            
            if ((x+(self.box_size*2) >= 0 and x+(self.box_size*2) <= 700) and (y+self.box_size >= 0 and y+self.box_size <= 700)):
                pos_pos.append((x+(self.box_size*2), y+self.box_size))

            if ((x-(self.box_size*2) >= 0 and x-(self.box_size*2) <= 700) and (y-self.box_size >= 0 and y-self.box_size <= 700)):
                pos_pos.append((x-(self.box_size*2), y-self.box_size))

            if ((x-(self.box_size*2) >= 0 and x-(self.box_size*2) <= 700) and (y+self.box_size >= 0 and y+self.box_size <= 700)):
                pos_pos.append((x-(self.box_size*2), y+self.box_size))

            if ((x+self.box_size >= 0 and x+self.box_size <= 700) and (y-(self.box_size*2) >= 0 and y-(self.box_size*2) <= 700)):
                pos_pos.append((x+self.box_size, y-(self.box_size*2)))

            if ((x-self.box_size >= 0 and x-self.box_size <= 700) and (y-(self.box_size*2) >= 0 and y-(self.box_size*2) <= 700)):
                pos_pos.append((x-self.box_size, y-(self.box_size*2)))

            if ((x+self.box_size >= 0 and x+self.box_size <= 700) and (y+(self.box_size*2) >= 0 and y+(self.box_size*2) <= 700)):
                pos_pos.append((x+self.box_size, y+(self.box_size*2)))

            if ((x-self.box_size >= 0 and x-self.box_size <= 700) and (y+(self.box_size*2) >= 0 and y+(self.box_size*2) <= 700)):
                pos_pos.append((x-self.box_size, y+(self.box_size*2)))
            # pos_pos_alt = [(x+2, y-1), (x+2, y+1), (x-2, y-1), (x-2, y+1), (x+1, y-2), (x-1, y-2), (x+1, y+2), (x-1, y+2)]
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)

    def bishop(self):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            x, y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x += self.box_size
                y += self.box_size
                if ((y >= 0 and y <=700) and (x >= 0 and x <=700)):
                    pos_pos.append((x,y))
                else:
                    break
        
            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x -= self.box_size
                y -= self.box_size
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break
            
            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x += self.box_size
                y -= self.box_size
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break

            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x -= self.box_size
                y += self.box_size
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
                else:
                    break
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)
    
    def queen(self):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            new_rook = self.rook()
            for p in new_rook.keys():
                pos_pos += new_rook[p]['pos_pos']
            new_bishop = self.bishop()
            for p in new_bishop.keys():
                pos_pos += new_rook[p]['pos_pos']
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)
    
    def king(self):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            
            x, y = curr_pos
            x = x
            y -= self.box_size
            if ((y >= 0 and y <=700) and (x >= 0 and x <=700)):
                pos_pos.append((x,y))
        
            x,y = curr_pos
            x = x
            y += self.box_size
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))
            
            x,y = curr_pos
            x -= self.box_size
            y = y
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))

            x,y = curr_pos
            x += self.box_size
            y = y
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))
            
            x, y = curr_pos
            x += self.box_size
            y += self.box_size
            if ((y >= 0 and y <=700) and (x >= 0 and x <=700)):
                pos_pos.append((x,y))
        
            x,y = curr_pos
            x -= self.box_size
            y -= self.box_size
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))
            
            x,y = curr_pos
            x += self.box_size
            y -= self.box_size
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))

            x,y = curr_pos
            x -= self.box_size
            y += self.box_size
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)

    def pawn(self, type):
        pieces = list(self.piece.keys())
        for i in range(len(pieces)):
            pos_pos = [] # a list of all possible positions of the piece
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            x, y = curr_pos
            if type == 'white':
                y += self.box_size
            elif type == 'black':
                y -= self.box_size
            if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                pos_pos.append((x,y))
            self.piece[pieces[i]]['pos_pos'] = pos_pos
        return(self.piece)