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
            
            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x -= self.box_size
                y = y
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))

            x,y = curr_pos
            while ((x >= 0 and x <= 700) and (y >= 0 and y <= 700)):
                x += self.box_size
                y = y
                if (y >= 0 and y <=700) and (x >= 0 and x <=700):
                    pos_pos.append((x,y))
        print(pos_pos)
        return(pos_pos)