# In this file there will be a few example positions that will be used to test the chess engine
# These positions are going to be fixed for demonstration purposes
import pieces as p
def read_board(boards):
    board = "{0:064b}".format(boards[p.W_Pawns]+boards[p.W_Rooks]+boards[p.W_Knights]+boards[p.W_Queens]+boards[p.W_Bishops]+boards[p.W_King]+boards[p.B_Pawns]+boards[p.B_Rooks]+boards[p.B_Bishops]+boards[p.B_Queens]+boards[p.B_Knights]+boards[p.B_King])
                                                                                                                                                                                                                                
    for i in range(8):
        print(board[8*i:8*i+8])

starting_position = {
                    p.W_Pawns  : 0b0000000000000000000000000000000000000000000000001111111100000000,
                    p.W_Rooks  : 0b0000000000000000000000000000000000000000000000000000000010000001,
                    p.W_Knights: 0b0000000000000000000000000000000000000000000000000000000001000010,
                    p.W_Bishops: 0b0000000000000000000000000000000000000000000000000000000000100100,
                    p.W_Queens : 0b0000000000000000000000000000000000000000000000000000000000010000,
                    p.W_King   : 0b0000000000000000000000000000000000000000000000000000000000001000,                        
                    p.B_Pawns  : 0b0000000011111111000000000000000000000000000000000000000000000000,
                    p.B_Rooks  : 0b1000000100000000000000000000000000000000000000000000000000000000,
                    p.B_Knights: 0b0100001000000000000000000000000000000000000000000000000000000000,
                    p.B_Bishops: 0b0010010000000000000000000000000000000000000000000000000000000000,
                    p.B_Queens : 0b0001000000000000000000000000000000000000000000000000000000000000,
                    p.B_King   : 0b0000100000000000000000000000000000000000000000000000000000000000
                    }

black_mated = {
                p.W_Pawns  : 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.W_Rooks  : 0b0000000000000000000000000000000000000000000000000000001000000001,
                p.W_Knights: 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.W_Bishops: 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.W_Queens : 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.W_King   : 0b0000000000000000000000000000000000000000000000000000000000001000,                        
                p.B_Pawns  : 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.B_Rooks  : 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.B_Knights: 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.B_Bishops: 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.B_Queens : 0b0000000000000000000000000000000000000000000000000000000000000000,
                p.B_King   : 0b0000000100000000000000000000000000000000000000000000000000000000
                }

midgame_position = {
    p.W_Pawns  : 0b0000000000000000000010000000100000001000000010000001000000000000,
    p.W_Rooks  : 0b0000000000000000000000000000000000000000000000000000010000000001,
    p.W_Knights: 0b0000000000000000000000000000000000100000000000000000000010000000,
    p.W_Bishops: 0b0000000000000000000000000000000100000000000000000010000000000000,
    p.W_Queens : 0b0000000000000000000000000000000000000100000000000000000000000000,
    p.W_King   : 0b0000000000000000000000000000000000000000000000000000000000000010,
    p.B_Pawns  : 0b0000000000010000001000000100000010000000000000000000000000000000,
    p.B_Rooks  : 0b0000000100000000000000000000000000000000000000000000000000000000,
    p.B_Knights: 0b0000000000000000000001000000000000000000000000000000000000000000,
    p.B_Bishops: 0b0000000000000000000000000000000000000000010000000000010000000000,
    p.B_Queens : 0b0000000000000000000000000100000000000000000000000000000000000000,
    p.B_King   : 0b0100000000000000000000000000000000000000000000000000000000000000
}

midgame_position2 = {
    # White pieces
    p.W_Pawns  : 0b0000000000000000000000000000000000000000000101000100010000000000, # Pawns are scattered, with some advanced
    p.W_Rooks  : 0b0000000000000000000000000000000000000000000000000000000010000000, # One rook on the first rank, one has been captured
    p.W_Knights: 0b0000000000000000000000000000000000000000000000000000000000000000, # Both knights have been captured
    p.W_Bishops: 0b0000000000000000000000000000000000000000000000000000000000000010, # One bishop remains on the board
    p.W_Queens : 0b0000000000000000000000000000000000000000000000000000000000000000, # Queen has been captured
    p.W_King   : 0b0000000000000000000000000000000000000000000000000000000000001000, # King is castled kingside

    # Black pieces
    p.B_Pawns  : 0b0000000000000100010000000000000000000000000000000000000000000000, # Pawns are well-positioned, advancing on the queenside
    p.B_Rooks  : 0b0000000000000000000000000000000000000000000000000000000000001000, # One rook on the h3
    p.B_Knights: 0b0000000000000000000000000000000000000000000000000000000000000000, # Both knights have been captured
    p.B_Bishops: 0b0010010000000000000000000000000000000000000000000000000000000000, # Both bishops active on their respective diagonals
    p.B_Queens : 0b0000000000000000000000000000000000000000000000000001000000000000, # Queen is advanced on the queenside
    p.B_King   : 0b0000000000000000000000000000000000000000000000000000000000000001  # King has been castled queenside
}

#read_board(midgame_position)