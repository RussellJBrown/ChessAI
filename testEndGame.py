import sys

def checkmate(board,currentColour):
    checkmate = board.is_checkmate()
    if checkmate == True:
        print(currentColour + " is the Winner")
        sys.exit()

def stalemate(board):
    stalemate = board.is_stalemate()
    if stalemate == True:
        print("Stalemate Game is a Draw")
        sys.exit()

def insufficient(board):
    insufficient = board.is_insufficient_material()
    if insufficient == True:
        print("The game is a draw by insufficient material")
        sys.exit()

def threeFoldRep(board):
    threeRep = board.can_claim_threefold_repetition()
    if threeRep == True:
        print("Draw by Repition")
        sys.exit()

def fiftyMoveNoCap(board):
    noCap = board.can_claim_fifty_moves()
    if noCap == True:
        print("No Capture in 50 moves, Game is a Draw")
        sys.exit()

def isGameOver(board,currentColour):
    checkmate(board,currentColour)
    stalemate(board)
    insufficient(board)
    threeFoldRep(board)
    fiftyMoveNoCap(board)
    gameOver = board.is_game_over()
    if gameOver == True:
        print("Game Over for a different reason")
        print("Add Reason Later")
        sys.exit()
    return False
