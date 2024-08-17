import pieces as p
import examplePositions as exp
import copy


def count_pieces(bitboard):
    positions = []
    count = bin(bitboard).count("1")
    return count, positions


def find_all_set_bits(bitboard):
    binary_str = format(bitboard, "064b")
    return [i + 1 for i, bit in enumerate(binary_str) if bit == "1"]


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
            if piece.colour == 'white':
                while position[piece]:
                    square = position[piece].bit_length() - 1
                    position[piece] ^= (1 << square)  # Remove the piece from the bitboard
                    
                    #print('{0:064b}'.format(self.position[piece])[square])
                    self.find_piece_moves(square, piece)

    def find_piece_moves(self,square, piece):
        moves = []
        black_position = self.position[p.B_Pawns]+self.position[p.B_Rooks]+self.position[p.B_Bishops]+self.position[p.B_Queens]+self.position[p.B_Knights]+self.position[p.B_King]
        white_position = self.position[p.W_Pawns]+self.position[p.W_Rooks]+self.position[p.W_Knights]+self.position[p.W_Queens]+self.position[p.W_Bishops]+self.position[p.W_King]
        #print('{0:064b}'.format(self.position[piece]))
        solo_piece = 2**square
        #print(solo)
        for move in piece.moves:
            self.shift(move,solo_piece)
            moves.append(move)
            
        print(moves)

    

    def shift(self,direction, piece):
        if direction < 1:
            return piece >> abs(direction)
        if direction >= 1:
            return piece << abs(direction)

board = Board(exp.midgame_position2)
manatee = ChessEngine(board)
#print(manatee.evaluate_position())
board.find_legal_move()


