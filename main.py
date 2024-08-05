#Chess 

#FILES ARE THE X VALUE THE COLUMNS
#RANKS ARE ROWS THE Y VALUE

#random
import random


#all the image urls
WHITE_PAWN_URL = 'https://codehs.com/uploads/019d3c264968b78b18d8d8897218544f'
BLACK_PAWN_URL = 'https://codehs.com/uploads/680de1f51a3b5f60d84f62ac83ee315d'
WHITE_KNIGHT_URL = 'https://codehs.com/uploads/afcb8730ead8719610a56cf85ca89140'
BLACK_KNIGHT_URL = 'https://codehs.com/uploads/ea27731f7478c52294056b2019d847f3'
WHITE_BISHOP_URL = 'https://codehs.com/uploads/5da4473a4e30536944146626e08332f2'
BLACK_BISHOP_URL = 'https://codehs.com/uploads/31f2cb2710ee6a1f18160ba47e21d828'
WHITE_ROOK_URL = 'https://codehs.com/uploads/98e8241ddfe5dbaf47ab835623d9ce7c'
BLACK_ROOK_URL = 'https://codehs.com/uploads/a0439dbfde6493cde993c0e55a67c52c'
WHITE_KING_URL = 'https://codehs.com/uploads/c16a802d7e7861abdbd3be87ebe4f9c1'
BLACK_KING_URL = 'https://codehs.com/uploads/42935f981f4e0960a073f7857838a683'
WHITE_QUEEN_URL = 'https://codehs.com/uploads/c91071a374626ab70fdcb9161f3a7afe'
BLACK_QUEEN_URL = 'https://codehs.com/uploads/8f94fc35e8d3f3fa6a5780d97ab3e5ee'

#variables
color = 'white'
rank = ''
square_clicked = ''
highlight_on = False
during_turn = False
highlight_list_moves = []
highlight_list_moved = [] 
squares_to_highlight = []
old_piece_list = []
player_turn = True
game_over = False

#return the king piece
def find_king(color):
    for s in Square.square_list:
        if s.piece == 'King' and s.color == color:
            return s

#checks if the king is in check
def check_for_check(kingPos):
    for s in Square.square_list:
        legal_moves(s)
        for move in s.moves:
            if kingPos in moves[0]:
                return True
    return False

#assigns a value to the current board position
def assign_value():
    value = 0
    white_value = 0
    black_value = 0

    for s in Square.square_list:
        if s.color == 'white':
            white_value += s.value
        elif s.color =='black':
            black_value += s.value


    value = black_value - white_value
    #print(value)

    return value

#checks every move available and returns the best move to make
def check_every_move():
    global square0, square1, square2, square3, square4, square5, square6, square7, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28, square29, square30, square31, square32, square33, square34, square35, square36, square37, square38, square39, square40, square41, square42, square43, square44, square45, square46, square47, square48, square49, square50, square51, square52, square53, square54, square55, square56, square57, square58, square59, square60, square61, square62, square63, old_square0, old_square1, old_square2, old_square3, old_square4, old_square5, old_square6, old_square7, old_square8, old_square9, old_square10, old_square11, old_square12, old_square13, old_square14, old_square15, old_square16, old_square17, old_square18, old_square19, old_square20, old_square21, old_square22, old_square23, old_square24, old_square25, old_square26, old_square27, old_square28, old_square29, old_square30, old_square31, old_square32, old_square33, old_square34, old_square35, old_square36, old_square37, old_square38, old_square39, old_square40, old_square41, old_square42, old_square43, old_square44, old_square45, old_square46, old_square47, old_square48, old_square49, old_square50, old_square51, old_square52, old_square53, old_square54, old_square55, old_square56, old_square57, old_square58, old_square59, old_square60, old_square61, old_square62, old_square63

    old_pos_list = save_board_position()

    for s in Square.square_list:
        if s.color == 'black':
            legal_moves(s)
            for move in s.moves:
                moveObj = get_square_object(move[0])
                moveObj.highlighted = True
                make_move(moveObj, s, 'black')
                move[1] = assign_value()
                reset_board(old_pos_list)

                
    return find_best_move()

#saves the current board position
def save_board_position():
    global square0, square1, square2, square3, square4, square5, square6, square7, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28, square29, square30, square31, square32, square33, square34, square35, square36, square37, square38, square39, square40, square41, square42, square43, square44, square45, square46, square47, square48, square49, square50, square51, square52, square53, square54, square55, square56, square57, square58, square59, square60, square61, square62, square63, old_square0, old_square1, old_square2, old_square3, old_square4, old_square5, old_square6, old_square7, old_square8, old_square9, old_square10, old_square11, old_square12, old_square13, old_square14, old_square15, old_square16, old_square17, old_square18, old_square19, old_square20, old_square21, old_square22, old_square23, old_square24, old_square25, old_square26, old_square27, old_square28, old_square29, old_square30, old_square31, old_square32, old_square33, old_square34, old_square35, old_square36, old_square37, old_square38, old_square39, old_square40, old_square41, old_square42, old_square43, old_square44, old_square45, old_square46, old_square47, old_square48, old_square49, old_square50, old_square51, old_square52, old_square53, old_square54, old_square55, old_square56, old_square57, old_square58, old_square59, old_square60, old_square61, old_square62, old_square63

    old_square0.__dict__.update(square0.__dict__)
    old_square1.__dict__.update(square1.__dict__)
    old_square2.__dict__.update(square2.__dict__)
    old_square3.__dict__.update(square3.__dict__)
    old_square4.__dict__.update(square4.__dict__)
    old_square5.__dict__.update(square5.__dict__)
    old_square6.__dict__.update(square6.__dict__)
    old_square7.__dict__.update(square7.__dict__)
    old_square8.__dict__.update(square8.__dict__)
    old_square9.__dict__.update(square9.__dict__)
    old_square10.__dict__.update(square10.__dict__)
    old_square11.__dict__.update(square11.__dict__)
    old_square12.__dict__.update(square12.__dict__)
    old_square13.__dict__.update(square13.__dict__)
    old_square14.__dict__.update(square14.__dict__)
    old_square15.__dict__.update(square15.__dict__)
    old_square16.__dict__.update(square16.__dict__)
    old_square17.__dict__.update(square17.__dict__)
    old_square18.__dict__.update(square18.__dict__)
    old_square19.__dict__.update(square19.__dict__)
    old_square20.__dict__.update(square20.__dict__)
    old_square21.__dict__.update(square21.__dict__)
    old_square22.__dict__.update(square22.__dict__)
    old_square23.__dict__.update(square23.__dict__)
    old_square24.__dict__.update(square24.__dict__)
    old_square25.__dict__.update(square25.__dict__)
    old_square26.__dict__.update(square26.__dict__)
    old_square27.__dict__.update(square27.__dict__)
    old_square28.__dict__.update(square28.__dict__)
    old_square29.__dict__.update(square29.__dict__)
    old_square30.__dict__.update(square30.__dict__)
    old_square31.__dict__.update(square31.__dict__)
    old_square32.__dict__.update(square32.__dict__)
    old_square33.__dict__.update(square33.__dict__)
    old_square34.__dict__.update(square34.__dict__)
    old_square35.__dict__.update(square35.__dict__)
    old_square36.__dict__.update(square36.__dict__)
    old_square37.__dict__.update(square37.__dict__)
    old_square38.__dict__.update(square38.__dict__)
    old_square39.__dict__.update(square39.__dict__)
    old_square40.__dict__.update(square40.__dict__)
    old_square41.__dict__.update(square41.__dict__)
    old_square42.__dict__.update(square42.__dict__)
    old_square43.__dict__.update(square43.__dict__)
    old_square44.__dict__.update(square44.__dict__)
    old_square45.__dict__.update(square45.__dict__)
    old_square46.__dict__.update(square46.__dict__)
    old_square47.__dict__.update(square47.__dict__)
    old_square48.__dict__.update(square48.__dict__)
    old_square49.__dict__.update(square49.__dict__)
    old_square50.__dict__.update(square50.__dict__)
    old_square51.__dict__.update(square51.__dict__)
    old_square52.__dict__.update(square52.__dict__)
    old_square53.__dict__.update(square53.__dict__)
    old_square54.__dict__.update(square54.__dict__)
    old_square55.__dict__.update(square55.__dict__)
    old_square56.__dict__.update(square56.__dict__)
    old_square57.__dict__.update(square57.__dict__)
    old_square58.__dict__.update(square58.__dict__)
    old_square59.__dict__.update(square59.__dict__)
    old_square60.__dict__.update(square60.__dict__)
    old_square61.__dict__.update(square61.__dict__)
    old_square62.__dict__.update(square62.__dict__)
    old_square63.__dict__.update(square63.__dict__)
    
    return [old_square0, old_square1, old_square2, old_square3, old_square4, old_square5, old_square6, old_square7, old_square8, old_square9, old_square10, old_square11, old_square12, old_square13, old_square14, old_square15, old_square16, old_square17, old_square18, old_square19, old_square20, old_square21, old_square22, old_square23, old_square24, old_square25, old_square26, old_square27, old_square28, old_square29, old_square30, old_square31, old_square32, old_square33, old_square34, old_square35, old_square36, old_square37, old_square38, old_square39, old_square40, old_square41, old_square42, old_square43, old_square44, old_square45, old_square46, old_square47, old_square48, old_square49, old_square50, old_square51, old_square52, old_square53, old_square54, old_square55, old_square56, old_square57, old_square58, old_square59, old_square60, old_square61, old_square62, old_square63]

#resets board positon
def reset_board(old_pos_list):
    global square0, square1, square2, square3, square4, square5, square6, square7, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28, square29, square30, square31, square32, square33, square34, square35, square36, square37, square38, square39, square40, square41, square42, square43, square44, square45, square46, square47, square48, square49, square50, square51, square52, square53, square54, square55, square56, square57, square58, square59, square60, square61, square62, square63, old_square0, old_square1, old_square2, old_square3, old_square4, old_square5, old_square6, old_square7, old_square8, old_square9, old_square10, old_square11, old_square12, old_square13, old_square14, old_square15, old_square16, old_square17, old_square18, old_square19, old_square20, old_square21, old_square22, old_square23, old_square24, old_square25, old_square26, old_square27, old_square28, old_square29, old_square30, old_square31, old_square32, old_square33, old_square34, old_square35, old_square36, old_square37, old_square38, old_square39, old_square40, old_square41, old_square42, old_square43, old_square44, old_square45, old_square46, old_square47, old_square48, old_square49, old_square50, old_square51, old_square52, old_square53, old_square54, old_square55, old_square56, old_square57, old_square58, old_square59, old_square60, old_square61, old_square62, old_square63
    
    square0.__dict__.update(old_pos_list[0].__dict__)
    square1.__dict__.update(old_pos_list[1].__dict__)
    square2.__dict__.update(old_pos_list[2].__dict__)
    square3.__dict__.update(old_pos_list[3].__dict__)
    square4.__dict__.update(old_pos_list[4].__dict__)
    square5.__dict__.update(old_pos_list[5].__dict__)
    square6.__dict__.update(old_pos_list[6].__dict__)
    square7.__dict__.update(old_pos_list[7].__dict__)
    square8.__dict__.update(old_pos_list[8].__dict__)
    square9.__dict__.update(old_pos_list[9].__dict__)
    square10.__dict__.update(old_pos_list[10].__dict__)
    square11.__dict__.update(old_pos_list[11].__dict__)
    square12.__dict__.update(old_pos_list[12].__dict__)
    square13.__dict__.update(old_pos_list[13].__dict__)
    square14.__dict__.update(old_pos_list[14].__dict__)
    square15.__dict__.update(old_pos_list[15].__dict__)
    square16.__dict__.update(old_pos_list[16].__dict__)
    square17.__dict__.update(old_pos_list[17].__dict__)
    square18.__dict__.update(old_pos_list[18].__dict__)
    square19.__dict__.update(old_pos_list[19].__dict__)
    square20.__dict__.update(old_pos_list[20].__dict__)
    square21.__dict__.update(old_pos_list[21].__dict__)
    square22.__dict__.update(old_pos_list[22].__dict__)
    square23.__dict__.update(old_pos_list[23].__dict__)
    square24.__dict__.update(old_pos_list[24].__dict__)
    square25.__dict__.update(old_pos_list[25].__dict__)
    square26.__dict__.update(old_pos_list[26].__dict__)
    square27.__dict__.update(old_pos_list[27].__dict__)
    square28.__dict__.update(old_pos_list[28].__dict__)
    square29.__dict__.update(old_pos_list[29].__dict__)
    square30.__dict__.update(old_pos_list[30].__dict__)
    square31.__dict__.update(old_pos_list[31].__dict__)
    square32.__dict__.update(old_pos_list[32].__dict__)
    square33.__dict__.update(old_pos_list[33].__dict__)
    square34.__dict__.update(old_pos_list[34].__dict__)
    square35.__dict__.update(old_pos_list[35].__dict__)
    square36.__dict__.update(old_pos_list[36].__dict__)
    square37.__dict__.update(old_pos_list[37].__dict__)
    square38.__dict__.update(old_pos_list[38].__dict__)
    square39.__dict__.update(old_pos_list[39].__dict__)
    square40.__dict__.update(old_pos_list[40].__dict__)
    square41.__dict__.update(old_pos_list[41].__dict__)
    square42.__dict__.update(old_pos_list[42].__dict__)
    square43.__dict__.update(old_pos_list[43].__dict__)
    square44.__dict__.update(old_pos_list[44].__dict__)
    square45.__dict__.update(old_pos_list[45].__dict__)
    square46.__dict__.update(old_pos_list[46].__dict__)
    square47.__dict__.update(old_pos_list[47].__dict__)
    square48.__dict__.update(old_pos_list[48].__dict__)
    square49.__dict__.update(old_pos_list[49].__dict__)
    square50.__dict__.update(old_pos_list[50].__dict__)
    square51.__dict__.update(old_pos_list[51].__dict__)
    square52.__dict__.update(old_pos_list[52].__dict__)
    square53.__dict__.update(old_pos_list[53].__dict__)
    square54.__dict__.update(old_pos_list[54].__dict__)
    square55.__dict__.update(old_pos_list[55].__dict__)
    square56.__dict__.update(old_pos_list[56].__dict__)
    square57.__dict__.update(old_pos_list[57].__dict__)
    square58.__dict__.update(old_pos_list[58].__dict__)
    square59.__dict__.update(old_pos_list[59].__dict__)
    square60.__dict__.update(old_pos_list[60].__dict__)
    square61.__dict__.update(old_pos_list[61].__dict__)
    square62.__dict__.update(old_pos_list[62].__dict__)
    square63.__dict__.update(old_pos_list[63].__dict__)

#find best move based on move values
def find_best_move():
    #assigns a random best move so if all moves are equal this will be played

    rand_list = []
    for s in Square.square_list:
        if s.color == 'black':
            legal_moves(s)
            if s.moves != [[0, 0], 0]:
                rand_list.append(s)
                s.moves = []
    piece_to_move = random.choice(rand_list)
    legal_moves(piece_to_move)
    piece_to_move.moves = []
    best_move = random.choice(piece_to_move.moves)
    piece_to_move = piece_to_move.position


    for s in Square.square_list:
        for move in s.moves:
            if move[1] > best_move[1]:
                best_move = move
                piece_to_move = s
    return [best_move, piece_to_move]

#make the board
def make_board():
    #position
    posX = 0
    posY = 0
    #Colors
    LIGHT_COLOR = 'rgb(236,236,208)'
    DARK_COLOR = 'rgb(119,149,87)'
    color = LIGHT_COLOR
    
    for i in range(8):
        for i in range(8):
            rec = Rectangle(get_width() / 8, get_height() / 8)
            rec.set_color(color)
            rec.set_position(posX, posY)
            posX += get_width() / 8
            add(rec)
            if color == LIGHT_COLOR:
                color = DARK_COLOR
            else:
                color = LIGHT_COLOR        
        posX = 0
        posY += get_height() / 8
        if color == LIGHT_COLOR:
            color = DARK_COLOR
        else:
            color = LIGHT_COLOR
make_board()

#promoting pawns
def promote(piece):
    #if the piece is a pawn and it is on the last rank
    if piece.piece == "Pawn":
        if piece.position[1] == 8 or piece.position[1] == 1:
            piece.piece = 'Queen'

#returns true if a piece is in the way and false if it is not
def check_for_piece_in_way(square_to_check, original_square, num1, num2):
    #i is multiplied by num1 and num2 to do addition or subtraction depending on direction

    #this makes a list of all the pieces behind the original square so they dont count as being in the way of the piece
    do_not_check_list = []
    for i in range(8):
        do_not_check_list.append([original_square.position[0] + (i * num1), original_square.position[1] + (i * num2)])

    #add the original piece and the piece to check so they dont count
    do_not_check_list.append(original_square.position)
    do_not_check_list.append(square_to_check.position)

    for sq in Square.square_list:
        for i in range(8, -1, -1):
            #this finds each square that is on the same diagonal and is not behind the original square. If there is a piece there, return true
            if square_to_check.position[0] + (i * num1) == sq.position[0] and square_to_check.position[1] + (i * num2) == sq.position[1] and sq.position not in do_not_check_list:
                if sq.piece != 'None':
                    return True
    return False

#all the moves a piece can make
def legal_moves(piece):
    #pawn
    if piece.piece == "Pawn":
        pawn_legal_moves(piece)
        
    #bishop
    if piece.piece == 'Bishop':
        bishop_legal_moves(piece)

    #knight
    if piece.piece == 'knight':
        knight_legal_moves(piece)

    #rook
    if piece.piece == 'Rook':
        rook_legal_moves(piece)
    
    #queen
    if piece.piece == 'Queen':
        queen_legal_moves(piece)

    #king
    if piece.piece == 'King':
        king_legal_moves(piece)
    
#pawn moves
def pawn_legal_moves(piece):
    piece.moves = []

    #white pawns
    if piece.color == 'white':
        #this checks for the peice above the pawn and if it is none then it can move
        for sq in Square.square_list:
            #moves once if piece ahead is none
            if sq.position[0] == piece.position[0] and sq.position[1] == piece.position[1] + 1 and sq.piece == 'None':
                piece.moves.append([[piece.position[0], piece.position[1] + 1], 0])
                #checks if it can move twice
                for sq in Square.square_list:
                    if sq.position[0] == piece.position[0] and sq.position[1] == piece.position[1] + 2 and sq.piece == 'None' and not piece.has_moved:
                        piece.moves.append([[piece.position[0], piece.position[1] + 2], 0])
            # capturing if the pawn is the opposing color and one up and to the left or right
            if (sq.position[0] == piece.position[0] + 1 or sq.position[0] == piece.position[0] - 1) and (sq.position[1] == piece.position[1] + 1):
                if sq.color == 'black':
                    piece.moves.append([sq.position, 0])
    #black pawns
    elif piece.color == 'black':
        #this checks for the peice above the pawn and if it is none then it can move
        for sq in Square.square_list:
            #moves once if piece ahead is none
            if sq.position[0] == piece.position[0] and sq.position[1] == piece.position[1] - 1 and sq.piece == 'None':
                piece.moves.append([[piece.position[0], piece.position[1] - 1], 0])
                #checks if it can move twice
                for sq in Square.square_list:
                    if sq.position[0] == piece.position[0] and sq.position[1] == piece.position[1] - 2 and sq.piece == 'None' and not piece.has_moved:
                        piece.moves.append([[piece.position[0], piece.position[1] - 2], 0])
            # capturing if the pawn is the opposing color and one up and to the left or right
            if (sq.position[0] == piece.position[0] + 1 or sq.position[0] == piece.position[0] - 1) and (sq.position[1] == piece.position[1] - 1):
                if sq.color == 'white':
                    piece.moves.append([sq.position, 0])

#bishop moves
def bishop_legal_moves(piece):
    piece.moves = []

    for sq in Square.square_list:
        for i in range(8):
            i += 1
            #checking so oyu cant take same colored pieces
            if piece.color != sq.color:
                #Diagonal 1: up 1 right 1
                if piece.position[0] + i == sq.position[0] and piece.position[1] + i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, -1, -1):
                        piece.moves.append([sq.position, 0])

                #diagonal 2: down one left one
                if piece.position[0] - i == sq.position[0] and piece.position[1] - i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, 1, 1):
                        piece.moves.append([sq.position, 0])

                #diagonal 3: down one right one
                if piece.position[0] + i == sq.position[0] and piece.position[1] - i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, -1, 1):
                        piece.moves.append([sq.position, 0])

                #diagonal 4: up one left one
                if piece.position[0] - i == sq.position[0] and piece.position[1] + i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, 1, -1):
                        piece.moves.append([sq.position, 0])

#knight moves
def knight_legal_moves(piece):
    piece.moves = []

    for sq in Square.square_list:
        #over 1 then 2
        if (sq.position[0] == piece.position[0] + 1 or sq.position[0] == piece.position[0] - 1) and (sq.position[1] == piece.position[1] + 2 or sq.position[1] == piece.position[1] - 2) and sq.color != piece.color:
            piece.moves.append([sq.position, 0])
        #over 2 then 1
        if (sq.position[0] == piece.position[0] + 2 or sq.position[0] == piece.position[0] - 2) and (sq.position[1] == piece.position[1] + 1 or sq.position[1] == piece.position[1] - 1) and sq.color != piece.color:
            piece.moves.append([sq.position, 0])

#rook moves
def rook_legal_moves(piece):
    if piece.piece != 'Queen':
        piece.moves = []
    for sq in Square.square_list:
        for i in range(8):
            i += 1
            #this makes it so you can ony take different colored pieces
            if piece.color != sq.color:
                #hor 1: right
                if piece.position[0] + i == sq.position[0] and piece.position[1] == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, -1, 0):
                        piece.moves.append([sq.position, 0])

                #hor 2: left
                if piece.position[0] - i == sq.position[0] and piece.position[1] == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, 1, 0):
                        piece.moves.append([sq.position, 0])

                #vert 1: up
                if piece.position[0] == sq.position[0] and piece.position[1] + i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, 0, -1):
                        piece.moves.append([sq.position, 0])

                #vert 2: down
                if piece.position[0] == sq.position[0] and piece.position[1] - i == sq.position[1]:
                    if not check_for_piece_in_way(sq, piece, 0, 1):
                        piece.moves.append([sq.position, 0])

#queen moves
def queen_legal_moves(piece):
    bishop_legal_moves(piece)
    rook_legal_moves(piece)

#king moves
def king_legal_moves(piece):
    piece.moves = []

    #if it can move to any square next to it and it is not the same color
    for sq in Square.square_list:
        if sq.position[0] in [piece.position[0] + 1, piece.position[0] - 1, piece.position[0]] and sq.position[1] in [piece.position[1] + 1, piece.position[1] - 1, piece.position[1]] and sq.color != piece.color:
            piece.moves.append([sq.position, 0])


#removes the highlight
def remove_highlight(type_of_highlight):
    global highlight_list_moves, highlight_list_moved
    
    if type_of_highlight == 1:
        for h in highlight_list_moves:
            remove(h)
            highlight_list_moves = []
            for s in Square.square_list:
                s.highlighted = False
    elif type_of_highlight == 2:
        for h in highlight_list_moved:
            remove(h)
            highlight_list_moved = []

#Highlight the square that a piece can be moved to
def highlight_squares(squares_to_highlight, type_of_highlight): 
    global highlight_on, highlight, highlight_list_moved, highlight_list_moves
    
    if highlight_on:
        remove_highlight(1)
        highlight_on = False
        highlight_list_moves = []
    
    if type_of_highlight == 1:
        for i in squares_to_highlight:
            for s in Square.square_list:
                if s.position == i[0]:
                    highlight = Circle(get_width() / 64)
                    highlight.set_position(convert_file(s.position[0]) + get_width() / 16, convert_rank(s.position[1]) + get_height() / 16)
                    highlight.set_color('rgb(70, 59, 48, .8)')
                    highlight_list_moves.append(highlight)
                    add(highlight)
                    highlight_on = True
                    s.highlighted = True
    elif type_of_highlight == 2:
        for i in squares_to_highlight:
            for s in Square.square_list:
                if s.position == i:
                    highlight = Rectangle(get_width() / 8, get_height() / 8)
                    highlight.set_position(convert_file(s.position[0]), convert_rank(s.position[1]))
                    highlight.set_color('rgb(200, 210, 0, .5)')
                    highlight_list_moved.append(highlight)
                    add(highlight)

#finds the rank of the square the user clicked and calls find file
def find_rank(x):
    global rank
    #rank 1
    if x < get_width() / 8:
        rank = 1
    #rank 2
    elif x < get_width() / 8 * 2:
        rank = 2
    #rank 3
    elif x < get_width() / 8 * 3:
        rank = 3
    #rank 4
    elif x < get_width() / 8 * 4:
        rank = 4
    #rank 5
    elif x < get_width() / 8 * 5:
        rank = 5
    #rank 6
    elif x < get_width() / 8 * 6:
        rank = 6
    #rank 7
    elif x < get_width() / 8 * 7:
        rank = 7
    #rank 8
    elif x < get_width():
        rank = 8
    
#find what file user clicked and returns the rank and file
def find_file(y, rank):
    global square_clicked
    #file 8
    if y < get_height() / 8:
        file = 8
    #file 7
    elif y < get_height() / 8 * 2:
        file = 7
    #file 6
    elif y < get_height() / 8 * 3:
        file = 6
    #file 5
    elif y < get_height() / 8 * 4:
        file = 5
    #file 4
    elif y < get_height() / 8 * 5:
        file = 4
    #file 3
    elif y < get_height() / 8 * 6:
        file = 3
    #file 2
    elif y < get_height() / 8 * 7:
        file = 2
    #file 1
    elif y < get_height():
        file = 1
    square_clicked = [rank, file]

#convert the file of a piece into an x value
def convert_file(file):
    #file 1
    if file == 1:
        return 0
    #file 2
    elif file == 2:
        return get_width() / 8
    #file 3
    elif file == 3:
        return get_width() / 8 * 2
    #file 4
    elif file == 4:
        return get_width() / 8 * 3
    #file 5
    elif file == 5:
        return get_width() / 8 * 4
    #file 6
    elif file == 6:
        return get_width() / 8 * 5
    #file 7
    elif file == 7:
        return get_width() / 8 * 6
    #file 8
    elif file == 8:
        return get_width() / 8 * 7

#converts a rank into a y coord
def convert_rank(rank):
    #rank 1
    if rank == 1:
        return get_height() / 8 * 7
    #rank 2
    elif rank == 2:
        return get_height() / 8 * 6
    #rank 3
    elif rank == 3:
        return get_height() / 8 * 5
    #rank 4
    elif rank == 4:
        return get_height() / 8 * 4
    #rank 5
    elif rank == 5:
        return get_height() / 8 * 3
    #rank 6
    elif rank == 6:
        return get_height() / 8 * 2
    #rank 7
    elif rank == 7:
        return get_height() / 8 * 1
    #rank 8
    elif rank == 8:
        return 0

#Class for every square on the board
#contains piece info, position, color, if a piece has moved, if it is highlighted, and a list of legal moves
class Square:
    square_list = []
    pieces_list = []

    def __init__(self, piece, position, color, has_moved, highlighted, moves, value, move_to_make, append):
        self.position = position
        self.piece = piece
        self.color = color
        self.has_moved = has_moved
        self.highlighted = highlighted
        self.moves = moves
        self.value = value
        self.move_to_make = move_to_make
        self.append = append
        if append == True:
            self.square_list.append(self)
            if piece != 'None':
                self.pieces_list.append(self)

#every square as an object
def make_square_objects():
    global square0, square1, square2, square3, square4, square5, square6, square7, square7, square8, square9, square10, square11, square12, square13, square14, square15, square16, square17, square18, square19, square20, square21, square22, square23, square24, square25, square26, square27, square28, square29, square30, square31, square32, square33, square34, square35, square36, square37, square38, square39, square40, square41, square42, square43, square44, square45, square46, square47, square48, square49, square50, square51, square52, square53, square54, square55, square56, square57, square58, square59, square60, square61, square62, square63, old_square0, old_square1, old_square2, old_square3, old_square4, old_square5, old_square6, old_square7, old_square8, old_square9, old_square10, old_square11, old_square12, old_square13, old_square14, old_square15, old_square16, old_square17, old_square18, old_square19, old_square20, old_square21, old_square22, old_square23, old_square24, old_square25, old_square26, old_square27, old_square28, old_square29, old_square30, old_square31, old_square32, old_square33, old_square34, old_square35, old_square36, old_square37, old_square38, old_square39, old_square40, old_square41, old_square42, old_square43, old_square44, old_square45, old_square46, old_square47, old_square48, old_square49, old_square50, old_square51, old_square52, old_square53, old_square54, old_square55, old_square56, old_square57, old_square58, old_square59, old_square60, old_square61, old_square62, old_square63

    square0 = Square('Rook', [1, 1], 'white', False, False, [], 5, [], True)
    square1 =  Square('knight', [2, 1], 'white', False, False, [], 3, [], True)
    square2 =  Square('Bishop', [3, 1], 'white', False, False, [], 3, [], True)
    square3 =  Square('Queen', [4, 1], 'white', False, False, [], 9, [], True)
    square4 =  Square('King', [5, 1], 'white', False, False, [], 100, [], True)
    square5 =  Square('Bishop', [6, 1], 'white', False, False, [], 3, [], True)
    square6 =  Square('knight', [7, 1], 'white', False, False, [], 3, [], True)
    square7 =  Square('Rook', [8, 1], 'white', False, False, [], 5, [], True)
    square8 =  Square('Pawn', [1, 2], 'white', False, False, [], 1, [], True)
    square9 =  Square('Pawn', [2, 2], 'white', False, False, [], 1, [], True)
    square10 =  Square('Pawn', [3, 2], 'white', False, False, [], 1, [], True)
    square11 =  Square('Pawn', [4, 2], 'white', False, False, [], 1, [], True)
    square12 = Square('Pawn', [5, 2], 'white', False, False, [], 1, [], True)
    square13 = Square('Pawn', [6, 2], 'white', False, False, [], 1, [], True)
    square14 = Square('Pawn', [7, 2], 'white', False, False, [], 1, [], True)
    square15 = Square('Pawn', [8, 2], 'white', False, False, [], 1, [], True)
    square16 = Square('None', [1, 3], 'none', False, False, [], 0, [], True)
    square17 = Square('None', [2, 3], 'none', False, False, [], 0, [], True)
    square18 = Square('None', [3, 3], 'none', False, False, [], 0, [], True)
    square19 = Square('None', [4, 3], 'none', False, False, [], 0, [], True)
    square20 = Square('None', [5, 3], 'none', False, False, [], 0, [], True)
    square21 = Square('None', [6, 3], 'none', False, False, [], 0, [], True)
    square22 = Square('None', [7, 3], 'none', False, False, [], 0, [], True)
    square23 = Square('None', [8, 3], 'none', False, False, [], 0, [], True)
    square24 = Square('None', [1, 4], 'none', False, False, [], 0, [], True)
    square25 = Square('None', [2, 4], 'none', False, False, [], 0, [], True)
    square26 = Square('None', [3, 4], 'none', False, False, [], 0, [], True)
    square27 = Square('None', [4, 4], 'none', False, False, [], 0, [], True)
    square28 = Square('None', [5, 4], 'none', False, False, [], 0, [], True)
    square29 = Square('None', [6, 4], 'none', False, False, [], 0, [], True)
    square30 = Square('None', [7, 4], 'none', False, False, [], 0, [], True)
    square31 = Square('None', [8, 4], 'none', False, False, [], 0, [], True)
    square32 = Square('None', [1, 5], 'none', False, False, [], 0, [], True)
    square33 = Square('None', [2, 5], 'none', False, False, [], 0, [], True)
    square34 = Square('None', [3, 5], 'none', False, False, [], 0, [], True)
    square35 = Square('None', [4, 5], 'none', False, False, [], 0, [], True)
    square36 = Square('None', [5, 5], 'none', False, False, [], 0, [], True)
    square37 = Square('None', [6, 5], 'none', False, False, [], 0, [], True)
    square38 = Square('None', [7, 5], 'none', False, False, [], 0, [], True)
    square39 = Square('None', [8, 5], 'none', False, False, [], 0, [], True)
    square40 = Square('None', [1, 6], 'none', False, False, [], 0, [], True)
    square41 = Square('None', [2, 6], 'none', False, False, [], 0, [], True)
    square42 = Square('None', [3, 6], 'none', False, False, [], 0, [], True)
    square43 = Square('None', [4, 6], 'none', False, False, [], 0, [], True)
    square44 = Square('None', [5, 6], 'none', False, False, [], 0, [], True)
    square45 = Square('None', [6, 6], 'none', False, False, [], 0, [], True)
    square46 = Square('None', [7, 6], 'none', False, False, [], 0, [], True)
    square47 = Square('None', [8, 6], 'none', False, False, [], 0, [], True)
    square48 = Square('Pawn', [1, 7], 'black', False, False, [], 1, [], True)
    square49 = Square('Pawn', [2, 7], 'black', False, False, [], 1, [], True)
    square50 = Square('Pawn', [3, 7], 'black', False, False, [], 1, [], True)
    square51 = Square('Pawn', [4, 7], 'black', False, False, [], 1, [], True)
    square52 = Square('Pawn', [5, 7], 'black', False, False, [], 1, [], True)
    square53 = Square('Pawn', [6, 7], 'black', False, False, [], 1, [], True)
    square54 = Square('Pawn', [7, 7], 'black', False, False, [], 1, [], True)
    square55 = Square('Pawn', [8, 7], 'black', False, False, [], 1, [], True)
    square56 = Square('Rook', [1, 8], 'black', False, False, [], 5, [], True)
    square57 = Square('knight', [2, 8], 'black', False, False, [], 3, [], True)
    square58 = Square('Bishop', [3, 8], 'black', False, False, [], 3, [], True)
    square59 = Square('Queen', [4, 8], 'black', False, False, [], 9, [], True)
    square60 = Square('King', [5, 8], 'black', False, False, [], 100, [], True)
    square61 = Square('Bishop', [6, 8], 'black', False, False, [], 3, [], True)
    square62 = Square('knight', [7, 8], 'black', False, False, [], 3, [], True)
    square63 = Square('Rook', [8, 8], 'black', False, False, [], 5, [], True)
    old_square0 = Square('Rook', [1, 1], 'white', False, False, [], 5, [], False)
    old_square1 = Square('knight', [2, 1], 'white', False, False, [], 3, [], False)
    old_square2 = Square('Bishop', [3, 1], 'white', False, False, [], 3, [], False)
    old_square3 = Square('Queen', [4, 1], 'white', False, False, [], 9, [], False)
    old_square4 = Square('King', [5, 1], 'white', False, False, [], 100, [], False)
    old_square5 = Square('Bishop', [6, 1], 'white', False, False, [], 3, [], False)
    old_square6 = Square('knight', [7, 1], 'white', False, False, [], 3, [], False)
    old_square7 = Square('Rook', [8, 1], 'white', False, False, [], 5, [], False)
    old_square8 = Square('Pawn', [1, 2], 'white', False, False, [], 1, [], False)
    old_square9 = Square('Pawn', [2, 2], 'white', False, False, [], 1, [], False)
    old_square10 = Square('Pawn', [3, 2], 'white', False, False, [], 1, [], False)
    old_square11 = Square('Pawn', [4, 2], 'white', False, False, [], 1, [], False)
    old_square12 = Square('Pawn', [5, 2], 'white', False, False, [], 1, [], False)
    old_square13 = Square('Pawn', [6, 2], 'white', False, False, [], 1, [], False)
    old_square14 = Square('Pawn', [7, 2], 'white', False, False, [], 1, [], False)
    old_square15 = Square('Pawn', [8, 2], 'white', False, False, [], 1, [], False)
    old_square16 = Square('None', [1, 3], 'none', False, False, [], 0, [], False)
    old_square17 = Square('None', [2, 3], 'none', False, False, [], 0, [], False)
    old_square18 = Square('None', [3, 3], 'none', False, False, [], 0, [], False)
    old_square19 = Square('None', [4, 3], 'none', False, False, [], 0, [], False)
    old_square20 = Square('None', [5, 3], 'none', False, False, [], 0, [], False)
    old_square21 = Square('None', [6, 3], 'none', False, False, [], 0, [], False)
    old_square22 = Square('None', [7, 3], 'none', False, False, [], 0, [], False)
    old_square23 = Square('None', [8, 3], 'none', False, False, [], 0, [], False)
    old_square24 = Square('None', [1, 4], 'none', False, False, [], 0, [], False)
    old_square25 = Square('None', [2, 4], 'none', False, False, [], 0, [], False)
    old_square26 = Square('None', [3, 4], 'none', False, False, [], 0, [], False)
    old_square27 = Square('None', [4, 4], 'none', False, False, [], 0, [], False)
    old_square28 = Square('None', [5, 4], 'none', False, False, [], 0, [], False)
    old_square29 = Square('None', [6, 4], 'none', False, False, [], 0, [], False)
    old_square30 = Square('None', [7, 4], 'none', False, False, [], 0, [], False)
    old_square31 = Square('None', [8, 4], 'none', False, False, [], 0, [], False)
    old_square32 = Square('None', [1, 5], 'none', False, False, [], 0, [], False)
    old_square33 = Square('None', [2, 5], 'none', False, False, [], 0, [], False)
    old_square34 = Square('None', [3, 5], 'none', False, False, [], 0, [], False)
    old_square35 = Square('None', [4, 5], 'none', False, False, [], 0, [], False)
    old_square36 = Square('None', [5, 5], 'none', False, False, [], 0, [], False)
    old_square37 = Square('None', [6, 5], 'none', False, False, [], 0, [], False)
    old_square38 = Square('None', [7, 5], 'none', False, False, [], 0, [], False)
    old_square39 = Square('None', [8, 5], 'none', False, False, [], 0, [], False)
    old_square40 = Square('None', [1, 6], 'none', False, False, [], 0, [], False)
    old_square41 = Square('None', [2, 6], 'none', False, False, [], 0, [], False)
    old_square42 = Square('None', [3, 6], 'none', False, False, [], 0, [], False)
    old_square43 = Square('None', [4, 6], 'none', False, False, [], 0, [], False)
    old_square44 = Square('None', [5, 6], 'none', False, False, [], 0, [], False)
    old_square45 = Square('None', [6, 6], 'none', False, False, [], 0, [], False)
    old_square46 = Square('None', [7, 6], 'none', False, False, [], 0, [], False)
    old_square47 = Square('None', [8, 6], 'none', False, False, [], 0, [], False)
    old_square48 = Square('Pawn', [1, 7], 'black', False, False, [], 1, [], False)
    old_square49 = Square('Pawn', [2, 7], 'black', False, False, [], 1, [], False)
    old_square50 = Square('Pawn', [3, 7], 'black', False, False, [], 1, [], False)
    old_square51 = Square('Pawn', [4, 7], 'black', False, False, [], 1, [], False)
    old_square52 = Square('Pawn', [5, 7], 'black', False, False, [], 1, [], False)
    old_square53 = Square('Pawn', [6, 7], 'black', False, False, [], 1, [], False)
    old_square54 = Square('Pawn', [7, 7], 'black', False, False, [], 1, [], False)
    old_square55 = Square('Pawn', [8, 7], 'black', False, False, [], 1, [], False)
    old_square56 = Square('Rook', [1, 8], 'black', False, False, [], 1, [], False)
    old_square57 = Square('knight', [2, 8], 'black', False, False, [], 3, [], False)
    old_square58 = Square('Bishop', [3, 8], 'black', False, False, [], 3, [], False)
    old_square59 = Square('Queen', [4, 8], 'black', False, False, [], 9, [], False)
    old_square60 = Square('King', [5, 8], 'black', False, False, [], 100, [], False)
    old_square61 = Square('Bishop', [6, 8], 'black', False, False, [], 3, [], False)
    old_square62 = Square('knight', [7, 8], 'black', False, False, [], 3, [], False)
    old_square63 = Square('Rook', [8, 8], 'black', False, False, [], 5, [], False)
make_square_objects()

#returns the square object based off the position
def get_square_object(pos):
    for s in Square.square_list:
        if s.position == pos:
            return s

#display the pieces
def display_pieces():

    global old_piece_list

    for t in old_piece_list:
        remove(t)
    old_piece_list = []
    for s in Square.square_list:
        if s.piece != 'None':
            if s.piece == 'Rook':
                if s.color == 'white':
                    image = Image(WHITE_ROOK_URL)
                else:
                    image = Image(BLACK_ROOK_URL)
            elif s.piece == 'Pawn':
                if s.color == 'white':
                    image = Image(WHITE_PAWN_URL)
                else:
                    image = Image(BLACK_PAWN_URL)
            elif s.piece == 'Queen':
                if s.color == 'white':
                    image = Image(WHITE_QUEEN_URL)
                else:
                    image = Image(BLACK_QUEEN_URL)
            elif s.piece == 'King':
                if s.color == 'white':
                    image = Image(WHITE_KING_URL)
                else:
                    image = Image(BLACK_KING_URL)
            elif s.piece == 'Bishop':
                if s.color == 'white':
                    image = Image(WHITE_BISHOP_URL)
                else:
                    image = Image(BLACK_BISHOP_URL)
            elif s.piece == 'knight':
                if s.color == 'white':
                    image = Image(WHITE_KNIGHT_URL)
                else:
                    image = Image(BLACK_KNIGHT_URL)
            image.set_position(convert_file(s.position[0]), convert_rank(s.position[1]) - 50 + get_height() / 8)
            add(image)
            old_piece_list.append(image)
display_pieces()

#make a move
#true if you can move there
def make_move(square_to_move_to, original_square, color_moving):

    old_P = square_to_move_to.piece
    old_C = original_square.color

    #if you click a square you can move to
    if square_to_move_to.highlighted:
        remove_highlight(2)
        square_to_move_to.piece = original_square.piece
        original_square.piece = 'None'
        square_to_move_to.color = original_square.color
        square_to_move_to.has_moved = True
        square_to_move_to.value = original_square.value
        original_square.color = 'none'
        original_square.moves = []
        original_square.value = 0
        square_to_move_to.moves = []
        promote(square_to_move_to)

        #end game if king is taken
        if old_P == 'King':
            end_game(old_C)

#the turn for the person
def player_turn(x, y, color_to_move):
    global player_turn, rank, square_clicked, during_turn, squares_to_highlight, original_square, old_piece_list, game_over, color

    color = color_to_move

    can_move_list = []
    #find the position of the cursor when its clicked
    find_rank(x)
    find_file(y, rank)

    #get the object of the square that was clicked
    square_clicked_object = get_square_object(square_clicked)

    #if you click a square that isnt highlighted it says you arent doing a move anymore
    if not square_clicked_object.highlighted:
        during_turn = False
        remove_highlight(1)

    #if you click a piece and it is not that colors turn then you arent making a move and return
    if square_clicked_object.color != color_to_move and square_clicked_object.color != 'none' and not during_turn:
        during_turn = False
        remove_highlight(1)
        return


    #show legal moves that can be made with that piece attached to the square
    #only does this if you arent currently making a move
    if not during_turn:

        original_square = square_clicked_object
        legal_moves(square_clicked_object)
        highlight_squares(square_clicked_object.moves, 1)
        during_turn = True
        return
    #this does your move after clicked a highlighted piece
    else:
        #make the move if you have already clicked a peice
        during_turn = False
        make_move(square_clicked_object, original_square, 'white')
        highlight_squares([square_clicked_object.position, original_square.position], 2)
        display_pieces()
        remove_highlight(1)
        if color_to_move == 'white':
            color = 'black'
        else:
            color = 'white'
        # ai move
        # if game_over:
        #     return
        # bot_piece_being_moved = check_every_move()[1]
        # bot_moving_to = check_every_move()[0]
        # print(bot_moving_to[0])
        # print(bot_piece_being_moved)
        # for s in Square.square_list:
        #     if s.position == bot_moving_to[0]:
        #         bot_moving_to = s
        #         print(s)
        #     elif s.position == bot_piece_being_moved:
        #         bot_piece_being_moved = s
        # bot_moving_to.highlighted = True
        # print(2)
        # make_move(bot_moving_to, bot_piece_being_moved, 'black')
        # highlight_squares([bot_moving_to.position, bot_piece_being_moved.position], 2)
        # display_pieces()

#the game function that runs when mouse is clicked
def game(x, y):
    global player_turn, game_over, color

    if player_turn and not game_over:
        player_turn(x, y, color)

#ends the game and prints the winner
def end_game(winner):
    global game_over

    game_over = True
    print('The Winner is ' + str(winner).capitalize() + '!')

add_mouse_click_handler(game)
