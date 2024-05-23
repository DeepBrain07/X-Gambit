class PossiblePositions:
    def __init__(self, piece) -> None:
        self.piece = piece
        self.box_size = 100
    def rook(self):
        pieces = list(self.piece.keys())
        pos_pos = [] # a list of all possible positions of the piece
        for i in range(len(pieces)):
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
        return(pos_pos)
    
    def knight(self):
        pieces = list(self.piece.keys())
        pos_pos = [] # a list of all possible positions of the piece
        for i in range(len(pieces)):
            key = pieces[i]
            curr_pos = self.piece[key]['curr_pos'] # get the current position of the piece
            x, y = curr_pos
            print(x,y)
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
        return pos_pos

    def bishop(self):
        pieces = list(self.piece.keys())
        pos_pos = [] # a list of all possible positions of the piece
        for i in range(len(pieces)):
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
        return(pos_pos)
    
    def queen(self):
        pos_pos = [] # a list of all possible positions of the piece
        rooks_pos_pos = self.rook()
        bishops_pos_pos = self.bishop()
        pos_pos = rooks_pos_pos + bishops_pos_pos
        return pos_pos
    
    def king(self):
        pieces = list(self.piece.keys())
        pos_pos = [] # a list of all possible positions of the piece
        for i in range(len(pieces)):
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
        return(pos_pos)
