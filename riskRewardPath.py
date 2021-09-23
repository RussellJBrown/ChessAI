import sys
import chess
import random
from openDatabase import *
import copy
from getBoardValue import *
from CheckEndGame import EndGame
import ast
import math
from chessBoard import changeColour

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
    if "#" in move or "+" in move:
        position=move[:-1]
        # print("Reached in get Piece ////")
        # print(position)
        return pieceAt(board,position[-2:])

    else:
        return pieceAt(board,move[-2:])


def convertPiece(piece):
    if repr(piece).lower() == "'p'":
        #print("Pawn")
        return "P"
    elif repr(piece).lower() == "'b'":
        #print("Bish")
        return "B"
    elif repr(piece).lower() == "'r'":
        #print("Rook")
        return "R"
    elif repr(piece).lower() == "'n'":
        #print("Night")
        return "N"
    elif repr(piece).lower() == "'q'":
       # print("Queen")
        return "Q"
    elif repr(piece).lower() == "'k'":
       # print("King")
        return "K"
    else:
        return piece


'''
Returns the piece being moved

Move: The current move being checked by the user.
'''
def getPieceBeingMove(move):
    piece = move[0]
    if piece == "a" or piece == "b" or piece == "c" or piece == "d" or piece == "e" or piece == "f" or piece == "g" or piece == "h":
        return "P"

    elif "O" in move:
        return "K"

    else:
        return convertPiece(piece)


def getPlaceFromMove(move):

    if "#" in move or "+" in move:
        move=move[-1]
        return move[-2:]

    else:
        return move[-2:]


'''
move: the move of the player

returns the last 2 charactes of a move
'''
def getPosition(move):
    return move[-2:]


'''
file = file Name

Reads Dictionary from file.
'''
def readDictionary(file):
    file = open(file,"r")
    contents = file.read()
    moveValues=ast.literal_eval(contents)
    file.close()
    return moveValues


'''
Method Returns a Dictionary that contains the point values for each piece
'''
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


'''
Method opens up Dictionary of piece to determine what the piece is worth on that spot.

piece: represents the current piece being moved
colour: current colour
ff: Are we in the lateGame
'''
def placeWorthWithPiece(piece,colour,lateGame):
    piece=str(repr(piece))
    positionWorth = {}
    try:
        if colour.lower()=="black":
            if piece == "'P'":
                positionWorth = readDictionary("pawnBlack.txt")
                piece="P"
            elif piece == "'R'":
                positionWorth = readDictionary("rookBlack.txt")
                piece="R"
            elif piece == "'N'":
                positionWorth = readDictionary("knightBlack.txt")
                piece="N"
            elif piece == "'K'" and lateGame==False:
                print("King Early Game")
                positionWorth = readDictionary("kingEarlyBlack.txt")
                piece="K"
            elif piece == "'K'" and lateGame==True:
                print("King Late Game")
                positionWorth = readDictionary("kingLateBlack.txt")
                piece="K"
            elif piece == "'Q'":
                positionWorth = readDictionary("queenBlack.txt")
                piece = "Q"
            elif piece == "'B'":
                positionWorth = readDictionary("bishopBlack.txt")
                piece="B"

        elif colour.lower()=="white":
            if piece=="'P'":
                positionWorth = readDictionary("pawnWhite.txt")
                piece="P"
            elif piece=="'R'":
                positionWorth = readDictionary("rookWhite.txt")
                piece="R"
            elif piece=="'N'":
                positionWorth = readDictionary("knightWhite.txt")
                piece="N"
            elif piece=="'K'" and lateGame==True:
                print("Late Game")
                positionWorth = readDictionary("kingLateWhite.txt")
                piece="K"
            elif piece=="'K'" and lateGame==False:
                print("Early Game")
                positionWorth = readDictionary("kingEarlyWhite.txt")
                piece="K"
            elif piece=="'Q'":
                positionWorth = readDictionary("queenWhite.txt")
                piece="Q"
            elif piece=="'B'":
                positionWorth = readDictionary("bishopWhite.txt")
                piece="B"
    except Exception as e:
        print("Error in Places With Piece Worth")
        print(e)
        sys.exit()



    return positionWorth


'''
move: the current move of the player
visitedPlatforms: Dictionary of the nodes and there values, used to ensure no place is visited multiple times.
'''
def EnterMoveIntoDictionary(move, visitedPlatforms, value,depth):
    if move not in visitedPlatforms:
        visitedPlatforms[str(depth)+move] = value
        return visitedPlatforms
    else:
        return visitedPlatforms

'''
move: the current mvoe of the player
visitedPlatforms: Dictionary of moves the player.
depth: current depth
'''
def CheckMoveIntoDictionary(move, visitedPlatforms, depth):
    dictMoveKey = str(depth) + move
    if dictMoveKey in visitedPlatforms:
        return True
    else:
        return False


'''
board: currently represents the board state
colour: current colour
computerColour: Computer Colour
move: current move
'''
def calculateMoveValue(board,colour,move,lateGame):
    print("Calculated Move Value")
    value=0
    white="White"
    black="Black"
    if "#" in move and colour==white:
        value+=math.inf

    elif "#" in move and colour==black:
        value+=-math.inf

    elif "+" in move and colour==white and lateGame==True:
        value+=50

    elif "+" in move and colour==black and lateGame==True:
        value+=-50

    elif "O-O-O" in move and colour == white:
        value+=50

    elif "O-O-O" in move and colour == black:
        value+=-50

    elif "0-0" in move and colour == white:
        value+=50

    elif "0-0" in move and colour == black:
        value+=-50

    elif "=" in move and colour == white:
        value+=25
    elif "=" in move and colour == black:
        value+=25

    valueT,piece_value = BoardValue(board,lateGame)
    value+=valueT
    return value,piece_value

'''
board: represents the current board state
depth: represents the current colour
maxDepth: the max depth the algorthim will reach
colour: current colour
alpha: represents the alpha value
beta: represents the beta balue
move: the current move
'''
def alphaBetaTree(board,depth,maxDepth,colour,alpha,beta,move):
    allComputerMoves = getMoveList(board)
    if depth == maxDepth:
        endgame=EndGame(board)
        if colour == "White":
            return calculateMoveValue(board,"Black",move,endgame)
        else:
            return calculateMoveValue(board,"White",move,endgame)

    if colour=="White":
        bestVal = float('-inf')
        bestPieceVal = float('-inf')
        for moveInList in allComputerMoves:
            futureBoard = board.copy()
            futureBoard.push_san(moveInList)
            treeValue,piece_value = alphaBetaTree(futureBoard,depth+1,maxDepth,"Black",alpha,beta,moveInList)
            bestVal = max(bestVal,treeValue)
            bestPieceVal = max(bestPieceVal,piece_value)
            alpha = max(alpha,best)
            if beta<=alpha:
                break
        return bestVal, piece_value

    else:
        bestVal = float('inf')
        bestPieceVal=float('inf')
        for moveInList in allComputerMoves:
            futureBoard = board.copy()
            print("Trying to Push")
            print(moveInList)
            futureBoard.push_san(moveInList)
            treeValue,piece_value = alphaBetaTree(futureBoard,depth+1,maxDepth,"White",alpha,beta,moveInList)
            bestVal = min(bestVal,treeValue)
            bestPieceVal = min(bestPieceVal,piece_value)
            beta = min(beta, best)
            if beta<=alpha:
                break

        return bestVal,piece_value


'''
board: A state of the board that will be analyzed
colour: current players move
computerColour: Computer Colour
selectDiff: The Difficulty of the computer
currentDepth: Current Depth of the search tree
bestMoveList: Currently unknown if this is still needed
move: the most recently move by player or AI

Method sets new board state with one of the possible moves

'''
def performTree(board,currentColour,computerColour, selectDiff,currentDepth,bestMoveList,move,value,BlackValue,WhiteValue,previousValue):
    print("Reached Perform Tree")
    futureBoard = board.copy()
    bestMove=""
    HighestValue = -math.inf
    LowestValue = math.inf

    #Method 1
    allComputerMoves = getMoveList(board)
    newColour = changeColour(currentColour)
    for move in allComputerMoves:
      print("Check if this move is best")
      futureBoard.push_san(move)
      value, moveValue = checkMovesRating(futureBoard,selectDiff,newColour)
      futureBoard.pop()
      if ((currentColour=="White" and (moveValue>=previousValue)) or (value == float("inf") and currentColour=="White"))  :
          if value>HighestValue:
              bestMove=move
              HighestValue=value

          if ((moveValue>0 and WhiteValue==BlackValue) or moveValue>previousValue and value!=float("inf")):
              bestMove=move
              previousValue=moveValue


      elif((currentColour=="Black" and (moreValue<=previousValue)) or (value==float("-inf") and currentColour=="Black")):
          if value<LowestValue:
              bestMove=move
              LowestValue=value
          if((moveValue<0 and WhiteValue==BlackValue)or moveValue<previousValue and value!=float("-inf")):
              bestMove=move
              previousValue=moveValue

    print(bestMove)
    return bestMove,previousValue

'''
board: A state of the board that will be analyzed
selectDiff: Currently represents the max depth we are looking for.
colour: current player move
computerColour: Represents the colour of the computer.
InEndGame: Tells if the game is in the end game state, used to determine better moves for king.

Currently acting as an inbetween method, don't know if this needed for the long term future

#To Do find Depth Limit
'''
def checkMovesRating(board,selectDiff,colour):
    value,moveValue = alphaBetaTree(board,0,selectDiff,colour,-math.inf,math.inf,"")
    return value, moveValue


'''
board: A state of the board

Gets a List of moves in the current board and does basic string manipulation
'''
def getMoveList(board):
    moves = board.legal_moves
    moves = str(moves)
    split_string = moves.split("(")
    split_string2 = split_string[1].split(")")
    allComputerMoves = split_string2[0].split(", ")
    return allComputerMoves
