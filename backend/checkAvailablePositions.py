

def find_closest_number(numbers, target):
    if numbers != []:
        closest_number = numbers[0]
        smallest_difference = abs(numbers[0] - target)
        
        for number in numbers:
            current_difference = abs(number - target)
            if current_difference < smallest_difference:
                smallest_difference = current_difference
                closest_number = number
        
        return closest_number
    
def check_rook_available_positions(piece_pos, curr_pos, your_pos, op_pieces):
    # checks for the available positions
    box_size = 100
    op_pieces_pos = [] # opponent's pieces positions
    your_pieces_pos = [] # your pieces' positions

    # get all the positions of the opponent's pieces
    for i in op_pieces.keys():
        for j in op_pieces[i].keys():
            pos = op_pieces[i][j]['curr_pos']
            op_pieces_pos.append(pos)
    
    # get all the positions of the your pieces
    for i in your_pos.keys():
        for j in your_pos[i].keys():
            pos = your_pos[i][j]['curr_pos']
            your_pieces_pos.append(pos)

    first_op_piece_pos = [] # a list of first oponent's piece possition that coincides with your piece
    pos_above = []
    pos_below = []
    pos_left = []
    pos_right = []
    # iterate over each pos_pos to get the above values

    x, y = curr_pos
    # get the values for pos_below
    while y < 700:
        y += box_size
        # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            pos_below.append(y)
    if pos_below != []:
        first_op_piece_pos = ((x,find_closest_number(pos_below, curr_pos[1])))
        y = first_op_piece_pos[1]
        if (x, y) in your_pieces_pos and (x, y) in piece_pos:
            piece_pos.remove((x,y))
        while y < 700:
            y += box_size
            # check if any pos in pos_below is present in op_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for pos_above
    while y > 0:
        y -= box_size
        # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            pos_above.append(y)
    if pos_above != []:
        first_op_piece_pos = (x,find_closest_number(pos_above, curr_pos[1]))
        y = first_op_piece_pos[1]
        if (x, y) in your_pieces_pos and (x, y) in piece_pos:
            piece_pos.remove((x,y))
        while y > 0:
            y -= box_size
            # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for pos_left
    while x > 0:
        x -= box_size
        # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            pos_left.append(x)
    if pos_left != []:
        first_op_piece_pos = (find_closest_number(pos_left, curr_pos[0]), y)
        x = first_op_piece_pos[0]
        if (x, y) in your_pieces_pos and (x, y) in piece_pos:
            piece_pos.remove((x,y))
        while x > 0:
            x -= box_size
            # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for pos_right
    while x < 700:
        x += box_size
        # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            pos_right.append(x)
    if pos_right != []:
        first_op_piece_pos = (find_closest_number(pos_right, curr_pos[0]), y)
        x = first_op_piece_pos[0]
        if (x, y) in your_pieces_pos and (x, y) in piece_pos:
            piece_pos.remove((x,y))
        while x < 700:
            x += box_size
            # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))
    
    return piece_pos
    
def check_bishop_available_positions(piece_pos, curr_pos, your_pos, op_pieces):
    # checks for the available positions
    box_size = 100
    op_pieces_pos = [] # opponent's pieces positions
    your_pieces_pos = [] # your pieces' positions

    # get all the positions of the opponent's pieces
    for i in op_pieces.keys():
        for j in op_pieces[i].keys():
            pos = op_pieces[i][j]['curr_pos']
            op_pieces_pos.append(pos)
    
    # get all the positions of the your pieces
    for i in your_pos.keys():
        for j in your_pos[i].keys():
            pos = your_pos[i][j]['curr_pos']
            your_pieces_pos.append(pos)

    first_op_piece_pos = [] # a list of first oponent's piece possition that coincides with your piece
    t_left = []
    t_right = []
    b_left = []
    b_right = []
    # iterate over each pos_pos to get the above values

    x, y = curr_pos
    # get the values for t_left
    while y > 0 and x > 0:
        x -= box_size
        y -= box_size
        # check if any pos in t_left is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            t_left.append((x,y))
    if t_left != []:
        t_left_alt = [] # an alternative list that contains the y values only
        for p in t_left:
            t_left_alt.append(p[1])
        y_new = find_closest_number(t_left_alt, curr_pos[1])
        for p in t_left:
            if p[1] == y_new:
                first_op_piece_pos = (p[0], y_new)
        if first_op_piece_pos in your_pieces_pos and first_op_piece_pos in piece_pos:
            piece_pos.remove(first_op_piece_pos)
        x,y = first_op_piece_pos
        while y > 0 and x > 0:
            x -= box_size
            y -= box_size
            # check if any pos in t_left is present in op_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for t_right
    while y > 0 and x < 700:
        x += box_size
        y -= box_size
        # check if any pos in t_right is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            t_right.append((x,y))
    if t_right != []:
        t_right_alt = [] # an alternative list that contains the y values only
        for p in t_right:
            t_right_alt.append(p[1])
        y_new = find_closest_number(t_right_alt, curr_pos[1])
        for p in t_right:
            if p[1] == y_new:
                first_op_piece_pos = (p[0], y_new)
        if first_op_piece_pos in your_pieces_pos and first_op_piece_pos in piece_pos:
            piece_pos.remove(first_op_piece_pos)
        x,y = first_op_piece_pos
        while y > 0 and x < 700:
            x += box_size
            y -= box_size
            # check if any pos in t_right is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for b_left
    while x > 0 and y < 700:
        x -= box_size
        y += box_size
        # check if any pos in b_left is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            b_left.append((x,y))
    if b_left != []:
        b_left_alt = [] # an alternative list that contains the y values only
        for p in b_left:
            b_left_alt.append(p[1])
        y_new = find_closest_number(b_left_alt, curr_pos[1])
        for p in b_left:
            if p[1] == y_new:
                first_op_piece_pos = (p[0], y_new)
        if first_op_piece_pos in your_pieces_pos and first_op_piece_pos in piece_pos:
            piece_pos.remove(first_op_piece_pos)
        x,y = first_op_piece_pos
        while x > 0 and y < 700:
            x -= box_size
            y += box_size
            # check if any pos in b_left is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))

    x, y = curr_pos
    # get the values for b_right
    while x < 700 and y < 700:
        x += box_size
        y += box_size
        # check if any pos in b_right is present in op_pieces_pos and your_pieces_pos
        if ((x,y) in op_pieces_pos) or ((x,y) in your_pieces_pos):
            b_right.append((x,y))
    if b_right != []:
        b_right_alt = [] # an alternative list that contains the y values only
        for p in b_right:
            b_right_alt.append(p[1])
        y_new = find_closest_number(b_right_alt, curr_pos[1])
        for p in b_right:
            if p[1] == y_new:
                first_op_piece_pos = (p[0], y_new)
        if first_op_piece_pos in your_pieces_pos and first_op_piece_pos in piece_pos:
            piece_pos.remove(first_op_piece_pos)
        x,y = first_op_piece_pos
        while x < 700 and y < 700:
            x += box_size
            y += box_size
            # check if any pos in pos_below is present in op_pieces_pos and your_pieces_pos
            if (x,y) in piece_pos:
                piece_pos.remove((x,y))
    
    return piece_pos

def check_queen_available_positions(piece_pos, curr_pos, your_pos, op_pieces):
    # get available positions for the rook
    for_rook = check_rook_available_positions(piece_pos, curr_pos, your_pos, op_pieces)
    # get available positions for the bishop
    for_bishop = check_bishop_available_positions(piece_pos, curr_pos, your_pos, op_pieces)
    available_positions = for_bishop + for_rook
    return available_positions

def check_king_available_positions(piece_pos, curr_pos, your_pos, op_pieces):
    your_pieces_pos = [] # your pieces' positions
    available_positions = []
    # get all the positions of the your pieces
    for i in your_pos.keys():
        for j in your_pos[i].keys():
            pos = your_pos[i][j]['curr_pos']
            your_pieces_pos.append(pos)
            
    for (x,y) in piece_pos:
        if (x,y) not in  your_pieces_pos:
            available_positions.append((x,y))
    return available_positions


def check_knight_available_positions(piece_pos, curr_pos, your_pos, op_pieces):
    your_pieces_pos = [] # your pieces' positions
    available_positions = []
    # get all the positions of the your pieces
    for i in your_pos.keys():
        for j in your_pos[i].keys():
            pos = your_pos[i][j]['curr_pos']
            your_pieces_pos.append(pos)
            
    for (x,y) in piece_pos:
        if (x,y) not in  your_pieces_pos:
            available_positions.append((x,y))
    print(piece_pos, "======", available_positions)
    return available_positions

def check_pawn_available_positions(piece_pos, curr_pos, your_pos, op_pieces, n, type):
    box_size = 100
    available_positions = []
    op_pieces_pos = [] # opponent's pieces positions
    your_pieces_pos = [] # your pieces' positions
    # get all the positions of the opponent's pieces
    for i in op_pieces.keys():
        for j in op_pieces[i].keys():
            pos = op_pieces[i][j]['curr_pos']
            op_pieces_pos.append(pos)

    # get all the positions of the your pieces
    for i in your_pos.keys():
        for j in your_pos[i].keys():
            pos = your_pos[i][j]['curr_pos']
            your_pieces_pos.append(pos)

    x,y = curr_pos  
    if type == "white":
        alt_y = y + box_size
        alt_x = x + box_size
        alt_y2 = y + box_size
        alt_x2 = x - box_size
    if type == "black":
        alt_y = y - box_size
        alt_x = x + box_size
        alt_y2 = y - box_size
        alt_x2 = x - box_size
        
    if (alt_x, alt_y) in op_pieces_pos and (alt_x >= 0 and alt_x <= 700) and (alt_y >= 0 and alt_y <= 700):
        available_positions.append((alt_x, alt_y))
    
    if (alt_x2, alt_y2) in op_pieces_pos and (alt_x2 >= 0 and alt_x2 <= 700) and (alt_y2 >= 0 and alt_y2 <= 700):
        available_positions.append((alt_x2, alt_y2))

    if available_positions == []:
        x,y = piece_pos[0]
        if ((x,y) not in  your_pieces_pos) and ((x,y) not in  op_pieces_pos):
            available_positions.append((x,y))
        if your_pos['pawn'][n]['moved'] is False:
            if type == 'white':
                y2 = y + box_size
            elif type == 'black':
                y2 = y - box_size

            if ((x,y2) not in  your_pieces_pos) and ((x,y2) not in  op_pieces_pos):
                if ((x,y) not in  your_pieces_pos) and ((x,y) not in  op_pieces_pos):
                    available_positions.append((x,y2))

    return available_positions

# find the position of a piece based on a given position
def find_piece(piece_color, pos):
    pieces = list(piece_color.keys())
    for p in pieces:
        nums = list(piece_color[p].keys())
        for n in nums:
            curr_pos = piece_color[p][n]['curr_pos']
            if curr_pos == pos:
                return p, n
    return None, None