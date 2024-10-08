import pieces as p
import examplePositions as exp
import copy

N, E, S, W = 8, -1, -8, 1

def read_board(boards):
    board = "{0:064b}".format(boards[p.W_Pawns]+boards[p.W_Rooks]+boards[p.W_Knights]+boards[p.W_Queens]+boards[p.W_Bishops]+boards[p.W_King]+boards[p.B_Pawns]+boards[p.B_Rooks]+boards[p.B_Bishops]+boards[p.B_Queens]+boards[p.B_Knights]+boards[p.B_King])
                                                                                                                                                                                                                                
    for i in range(8):
        print(board[8*i:8*i+8])

def count_pieces(bitboard):
    positions = []
    count = bin(bitboard).count("1")
    return count, positions


def find_all_set_bits(bitboard):
    binary_str = format(bitboard, "064b")
    locations = [i + 1 for i, bit in enumerate(binary_str) if bit == "1"]
    if locations == []:
        return None
    else: return locations


class ChessEngine:
    def __init__(self, board):
        self.score = 0
        self.board = board

    def evaluate_position(self):
        # Evaluate the position and return who is winning or if someones has won, a draw etc.
        if self.board.black_mated():
            return 10000
        if self.board.white_mated():
            return -10000
        if self.board.is_stalemate():
            return 0

        self.score += self.board.score()

        self.score += self.board.position_adjustment()
        return self.score / 10


class Board:
    def __init__(self, position):
        self.position = position
        self.is_stalemate = False

    def black_mated(self):
        return False

    def white_mated(self):
        return False

    def score(self):
        score = 0
        for piece in self.position:
            score += count_pieces(self.position[piece])[0] * piece.value
        return score

    def position_adjustment(self):
        score = 0
        for piece in self.position:
            if piece.colour == "white":
                for i in find_all_set_bits(self.position[piece]):
                    score += piece.pst_adjustment[i - 1]
            if piece.colour == "black":
                for i in find_all_set_bits(self.position[piece]):
                    score -= piece.pst_adjustment[i - 1]
        return score

    def find_legal_move(self):
        # Find all possible legal moves for a piece
        position = copy.deepcopy(self.position)
        for piece in self.position:
            while position[piece]:
                square = position[piece].bit_length() - 1
                position[piece] ^= 1 << square  # Remove the piece from the bitboard

                # print('{0:064b}'.format(self.position[piece])[square])
                self.find_piece_moves(square, piece)

    def find_piece_moves(self, square, piece):
        moves = []
        legal_moves = []
        black_position = (
            self.position[p.B_Pawns]
            + self.position[p.B_Rooks]
            + self.position[p.B_Bishops]
            + self.position[p.B_Queens]
            + self.position[p.B_Knights]
            + self.position[p.B_King]
        )
        white_position = (
            self.position[p.W_Pawns]
            + self.position[p.W_Rooks]
            + self.position[p.W_Knights]
            + self.position[p.W_Queens]
            + self.position[p.W_Bishops]
            + self.position[p.W_King]
        )
        old_position = black_position + white_position
        #print('{0:064b}'.format(position))
        #print('\n'+'{0:064b}'.format(self.position[piece]))
        solo_piece = 2**square
        #print('{0:064b}'.format(solo_piece))
        for move in piece.moves:
            self.shift(move, solo_piece)
            moves.append(move)   
        # does not allow advanced pawns to move 2 squares
        if piece == p.W_Pawns:
            if solo_piece > 2**16:
                moves.remove(16)
        if piece == p.B_Pawns:
            if solo_piece < 2**48:
                moves.remove(-16)
        
        for move in moves:
            #shift piece by move increment and check if any collision on the board (either disallow move or take colliding piece)
            #then check if it puts the king in check 
            new_solo_piece = self.shift(move, solo_piece) # stores new location of the solo piece after it has been moved
    
            # check if new piece moves to a space occupied by another piece of the same colour
            #print(find_all_set_bits(new_solo_piece), find_all_set_bits(white_position))
            if find_all_set_bits(new_solo_piece) != None:
                if find_all_set_bits(new_solo_piece)[0] in (find_all_set_bits(white_position) if piece.colour == "white" else find_all_set_bits(black_position)):
                    # If there is a collision, remove the move
                    moves.remove(move)

            # if piece moves into a space occupied by the opposing king, it cannot move there
            if new_solo_piece == (self.position[p.B_King]if piece.colour == 'white' else self.position[p.W_King]):
                moves.remove(move)
            
            # checks if a pawn can move diagonally to take a piece of the opposite colour
            if piece == p.W_Pawns or piece == p.B_Pawns:
                if find_all_set_bits(new_solo_piece) not in (find_all_set_bits(black_position) if piece.colour == "white" else find_all_set_bits(white_position)):
                    if move != N:
                        moves.remove(move)

            # if new position puts same colour king in check then move must be removed
            if self.king_check():
                moves.remove(move)

        print(piece, moves)
    
    def king_check(self):
        return False

    def shift(self, direction, piece):
        if direction < 1:
            return piece >> abs(direction)
        if direction >= 1:
            return piece << abs(direction)


board = Board(exp.midgame_position2)
manatee = ChessEngine(board)
# print(manatee.evaluate_position())
board.find_legal_move()
