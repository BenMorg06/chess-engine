N, E, S, W = 8, -1, -8, 1
class Piece:
    def __init__(self):
        pass
#
# White Pieces
#
class W_Pawns(Piece):
    value = 1
    colour = 'white'
    moves = [N, N+N, N+E, N+W]
    pst_adjustment = [
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        0.5, -0.5, -1.0,  0.0,  0.0, -1.0 , -0.5, 0.5, 
        0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5,
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
    ]
    
class W_Knights(Piece):
    value = 3
    colour = 'white'
    moves = [N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W]
    pst_adjustment = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
    ]
    
class W_Bishops(Piece):
    value = 3
    colour = 'white'
    moves = [N+E, S+E, S+W, N+W]
    pst_adjustment = [
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
        -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
        -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
        -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
        -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
    ]
    

class W_Rooks(Piece):
    value = 5
    colour = 'white'
    moves = [N, E, S, W]
    pst_adjustment = [
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,  0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
         0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0,  0.0, 
    ]
class W_Queens(Piece):
    value = 9
    colour = 'white'
    moves = [N, E, S, W, N+E, S+E, S+W, N+W]
    pst_adjustment = [
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
         0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
        -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0
    ]
class W_King(Piece):
    value = 10000
    colour = 'white'
    moves = [N, E, S, W, N+E, S+E, S+W, N+W]
    pst_adjustment = [
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
        -1.0, -2.0, -2.0, -3.0, -3.0, -2.0, -2.0, -1.0,
         2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
         2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0
    ]
#
# Black Pieces
#
class B_Pawns(Piece):
    value = -1
    colour = 'black'
    moves = [-N, -(N+N), -(N+E), -(N+W)]
    pst_adjustment = [
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
        0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5,
        0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
        0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
        0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
        1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
        5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
        0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0
    ]
class B_Knights(Piece):
    value = -3
    colour = 'black'
    moves = [N+N+E, E+N+E, E+S+E, S+S+E, S+S+W, W+S+W, W+N+W, N+N+W]
    pst_adjustment = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
    ]
    
class B_Bishops(Piece):
    value = -3
    colour = 'black'
    moves = [N+E, S+E, S+W, N+W]
    pst_adjustment = [
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
        -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
        -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
        -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
        -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
        -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
    ]
class B_Rooks(Piece):
    value = -5
    colour = 'black'
    moves = [N, E, S, W]
    pst_adjustment = [
        0.0,  0.0, 0.0, 0.5, 0.5, 0.0, 0.0,  0.0,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
        0.5,  1.0, 1.0, 1.0, 1.0, 1.0, 1.0,  0.5,
        0.0,  0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.0,
    ]

    
class B_Queens(Piece):
    value = -9
    colour = 'black'
    moves = [N, E, S, W, N+E, S+E, S+W, N+W]
    pst_adjustment = [
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
        -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
        -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0,  0.0,
        -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0,  0.0,
        -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
        -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
        -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
    ]
    
class B_King(Piece):
    value = -10000
    colour = 'black'
    moves = [N, E, S, W, N+E, S+E, S+W, N+W]
    pst_adjustment = [
         2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0,
         2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
        -1.0, -2.0, -2.0, -3.0, -3.0, -2.0, -2.0, -1.0,
        -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
        -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0
    ]