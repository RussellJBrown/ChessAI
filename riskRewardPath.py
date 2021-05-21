import sys
import chess
import random

#Creating a risk reward system
#Creating an evaluation Function

def pieceAt(board,position):
    p1 = position[0]
    if p1=="a":
        if "a1"==position:
            return board.piece_at(chess.A1)
        elif "a2"==position:
            return board.piece_at(chess.A2)
        elif "a3"==position:
            return board.piece_at(chess.A3)
        elif "a4"==position:
            return board.piece_at(chess.A4)
        elif "a5"==position:
            return board.piece_at(chess.A5)
        elif "a6"== position:
            return board.piece_at(chess.A6)
        elif "a7"==position:
            return board.piece_at(chess.A7)
        elif "a8"==position:
            return board.piece_at(chess.A8)

    elif p1 == "b":
        if "b1"==position:
            return board.piece_at(chess.B1)
        elif "b2"==position:
            return board.piece_at(chess.B2)
        elif "b3"==position:
            return board.piece_at(chess.B3)
        elif "b4"==position:
            return board.piece_at(chess.B4)
        elif "b5"==position:
            return board.piece_at(chess.B5)
        elif "b6"== position:
            return board.piece_at(chess.B6)
        elif "b7"==position:
            return board.piece_at(chess.B7)
        elif "b8"==position:
            return board.piece_at(chess.B8)

    elif p1 == "c":
        if "c1"==position:
            return board.piece_at(chess.C1)
        elif "c2"==position:
            return board.piece_at(chess.C2)
        elif "c3"==position:
            return board.piece_at(chess.C3)
        elif "c4"==position:
            return board.piece_at(chess.C4)
        elif "c5"==position:
            return board.piece_at(chess.C5)
        elif "c6"== position:
            return board.piece_at(chess.C6)
        elif "c7"==position:
            return board.piece_at(chess.C7)
        elif "c8"==position:
            return board.piece_at(chess.C8)

    elif p1=="d":
        if "d1"==position:
            return board.piece_at(chess.D1)
        elif "d2"==position:
            return board.piece_at(chess.D2)
        elif "d3"==position:
            return board.piece_at(chess.D3)
        elif "d4"==position:
            return board.piece_at(chess.D4)
        elif "d5"==position:
            return board.piece_at(chess.D5)
        elif "d6"== position:
            return board.piece_at(chess.D6)
        elif "d7"==position:
            return board.piece_at(chess.D7)
        elif "d8"==position:
            return board.piece_at(chess.D8)

    elif p1=="e":
        if "e1"==position:
            return board.piece_at(chess.E1)
        elif "e2"==position:
            return board.piece_at(chess.E2)
        elif "e3"==position:
            return board.piece_at(chess.E3)
        elif "e4"==position:
            return board.piece_at(chess.E4)
        elif "e5"==position:
            return board.piece_at(chess.E5)
        elif "e6"== position:
            return board.piece_at(chess.E6)
        elif "e7"==position:
            return board.piece_at(chess.E7)
        elif "e8"==position:
            return board.piece_at(chess.E8)

    elif p1=="f":
        if "f1"==position:
            return board.piece_at(chess.F1)
        elif "f2"==position:
            return board.piece_at(chess.F2)
        elif "f3"==position:
            return board.piece_at(chess.F3)
        elif "f4"==position:
            return board.piece_at(chess.F4)
        elif "f5"==position:
            return board.piece_at(chess.F5)
        elif "f6"== position:
            return board.piece_at(chess.F6)
        elif "f7"==position:
            return board.piece_at(chess.F7)
        elif "f8"==position:
            return board.piece_at(chess.F8)

    elif p1=="g":
        if "g1"==position:
            return board.piece_at(chess.G1)
        elif "g2"==position:
            return board.piece_at(chess.G2)
        elif "g3"==position:
            return board.piece_at(chess.G3)
        elif "g4"==position:
            return board.piece_at(chess.G4)
        elif "g5"==position:
            return board.piece_at(chess.G5)
        elif "g6"== position:
            return board.piece_at(chess.G6)
        elif "g7"==position:
            return board.piece_at(chess.G7)
        elif "g8"==position:
            return board.piece_at(chess.G8)

    elif p1 =="h":
        if "h1"==position:
            return board.piece_at(chess.H1)
        elif "h2"==position:
            return board.piece_at(chess.H2)
        elif "h3"==position:
            return board.piece_at(chess.H3)
        elif "h4"==position:
            return board.piece_at(chess.H4)
        elif "h5"==position:
            return board.piece_at(chess.H5)
        elif "h6"== position:
            return board.piece_at(chess.H6)
        elif "h7"==position:
            return board.piece_at(chess.H7)
        elif "h8"==position:
            return board.piece_at(chess.H8)



def getPieceOnBoardSpot(board, move):
    position = move[-2:]
    return pieceAt(board,position)



def piecesWorth():
    pieces = {}
    pieces['P'] = 1
    pieces['p'] = -1
    pieces['R'] = 5
    pieces['r'] = -5
    pieces['N'] = 3
    pieces['n'] = -3
    pieces['B'] = 3
    pieces['b'] = -3
    pieces['Q'] = 9
    pieces['q'] = -9
    pieces['K'] = 100
    pieces['k'] = -100
    return pieces



#Perform a move a find out next likely moves based off the move
def calculateMoveValue(board,colour,computerColour,move):

    if "#" in move && colour==computerColour:
        return "WIN"

    else:
        #if currentDepth < selectDiff:
        piece = getPieceOnBoardSpot(board, move)
        pieces = piecesWorth()
        return pieces[piece], move




#White Will Try to Minimize
#Black Will Try to Maximize
def alphaBetaPruning(board,depth,maxDepth,colour,computerColour,alpha,beta):
    allComputerMoves = getMoveList(board)
    if colour == "White":
        bestVal = float('inf')
        for move in allComputerMoves:
            futureBoard = board
            futureBoard.push_san(move)
            value, move = alphaBetaPruning(futureBoard,depth+1,maxDepth,"Black",computerColour,alpha,beta)
            bestVal = min(bestVal,value)
            alpha = min(alpha,bestVal)
            if beta<=alpha:
                break
        return calculateMoveValue(board,colour,computerColour,bestVal)

    else:
        bestVal = float('-inf')
        for move in allComputerMoves:
            futureBoard = board
            futureBoard.push_san(move)
            value, move = alphaBetaPruning(futureBoard,depth+1,maxDepth,"White",computerColour,alpha,beta)
            bestVal = min(bestVal,balue)
            beta = min(beta,bestVal)
            if beta<=alpha:
                break
        return calculateMoveValue(board,colour,computerColour,bestVal)



#Board is the Current Boards State
#allComputerMoves is the list of all valid moves in current state
#selectDiff int used to perform diff depth
def performTree(board,colour,computerColour, selectDiff,currentDepth,bestMoveList):
    print("Perform Tree")
    futureBoard = board
    bestMove = allComputerMoves[0]
    bestMoveValue = 0

    if selectDiff==currentDepth:
        return move

    for move in allComputerMoves:
        #futureBoard.push_san(move)
        value = calculateMoveValue(futureBoard,colour,computerColour,selectDiff,currentDepth)
        if value == "WIN":
            return move

        if colour=="black":
            if value<bestMoveValue:
                bestMoveValue = value
                bestMove = move

        if colour=="white":
            if value>bestMoveValue:
                bestMostValue = value
                bestMove = move

    futureBoard.push_san(bestMove)
    bestMoveList.append(bestMove)

    if colour == computerColour:
        if computerColour=="white":
            colour = "black"
            return performTree(futureBoard,colour, computerColour, allComputerMoves, selectDiff, currentDepth+1,bestMoveList)
        else:
            colour = "white"
            return performTree(futureBoard,colour, computerColour, allComputerMoves, selectDiff, currentDepth+1,bestMoveList)


    else:
        if colour == "white":
            colour = "black"
            return performTree(futureBoard, colour, computerColour, allComputerMoves, selectDiff, currentDepth, bestMoveList)
        else:
            colour = "white"
            return performTree(futureBoard, colour, computerColour, allComputerMoves, selectDiff, currentDepth, bestMoveList)

def checkMovesRating(board,selectDiff,colour,computerColour):
    print("Make Computer Move")
    #allComputerMoves = getMoveList(board)
    bestMoveList = []
    #board,colour,computerColour, allComputerMoves,selectDiff,currentDepth,bestMoveList):
    #move = performTree(board,colour,computerColour ,allComputerMoves,selectDiff,0,bestMoveList)

    alpha = float('-inf')
    beta = float('inf')
    value, move = alphaBetaPruning(board,selectDiff,colour,computerColour,alpha,beta)
    if value==0:
        print("No Best Option")
    else:
        print("Best Move")
        print(move)

    return move

def getMoveList(board):
    moves = board.legal_moves
    moves = str(moves)
    split_string = moves.split("(")
    split_string2 = split_string[1].split(")")
    allComputerMoves = split_string2[0].split(", ")
    return allComputerMoves


def startingOpening(board):
    print("Computer Does Starting Opening")
