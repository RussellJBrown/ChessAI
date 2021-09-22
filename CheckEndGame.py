import chess

def EndGame(board):
    whitePiece = 0
    blackPiece = 0
    for i in range(64):
        piece = board.piece_at(i)
        try:
            piece_type = piece.piece_type
            piece_colour = piece.color

            if piece_colour == False:
                if piece_type == 2 or piece_type == 3 or piece_type == 5 or piece_type == 4:
                    blackPiece+=1

            elif piece_colour == True:
                if piece_type == 2 or piece_type == 3 or piece_type == 5 or piece_type == 4:
                    whitePiece+=1                            
        except:
            pass

        if whitePiece>1 and blackPiece>1:
            return False

    if whitePiece<2 or blackPiece<2:
        return True


if __name__ == '__main__':
    board = chess.Board()
    print(EndGame(board))