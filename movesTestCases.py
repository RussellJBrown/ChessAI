from CalculateLegalMoves import *


def testCase1():
    test = False
    return test

def getTestCase1(chessBoard):
    chessBoard[0][0] = "WRook"
    chessBoard[1][0] = "WKnight"
    chessBoard[2][0] = "WBishop"
    chessBoard[3][0] = "WQueen"
    chessBoard[4][0] = "WKing"
    chessBoard[5][0] = "WBishop2"
    chessBoard[6][0] = "WKnight2"
    chessBoard[7][0] = "WRook2"

    chessBoard[0][1] = "WPawn"
    chessBoard[1][1] = "WPawn2"
    chessBoard[2][1] = "WPawn3"
    chessBoard[3][1] = "WPawn4"
    chessBoard[4][1] = "WPawn5"
    chessBoard[5][1] = "WPawn6"
    chessBoard[6][1] = "WPawn7"
    chessBoard[7][1] = "WPawn8"

    chessBoard[0][7] = "BRook"
    chessBoard[1][7] = "BKnight"
    chessBoard[2][7] = "BBishop"
    chessBoard[3][7] = "BQueen"
    chessBoard[4][7] = "BKing"
    chessBoard[5][7] = "BBishop2"
    chessBoard[6][7] = "BKnight2"
    chessBoard[7][7] = "BRook2"

    chessBoard[0][1] = "WPawn"
    chessBoard[1][1] = "WPawn2"
    chessBoard[2][1] = "WPawn3"
    chessBoard[3][1] = "WPawn4"
    chessBoard[4][1] = "WPawn5"
    chessBoard[5][1] = "WPawn6"
    chessBoard[6][1] = "WPawn7"
    chessBoard[7][1] = "WPawn8"

    chessBoard[0][6] = "BPawn"
    chessBoard[1][6] = "BPawn2"
    chessBoard[2][6] = "BPawn3"
    chessBoard[3][6] = "BPawn4"
    chessBoard[4][6] = "BPawn5"
    chessBoard[5][6] = "BPawn6"
    chessBoard[6][6] = "BPawn7"
    chessBoard[7][6] = "BPawn8"

    return chessBoard

def getTestCase2(testCase2):
    testCase2[3][1] = "BPawn"
    testCase2[6][1] = "WKnight"
    testCase2[0][2] = "BBishop"
    testCase2[0][3] = "BPawn"
    testCase2[1][3] = "BKing"
    testCase2[4][3] = "BPawn"

    testCase2[0][4] = "WPawn"
    testCase2[3][4] = "BPawn"
    testCase2[5][4] = "BBishop"

    testCase2[2][5] = "WKing"
    testCase2[3][5] = "WPawn"
    testCase2[5][5] = "WPawn"

    testCase2[0][6] = "WRook"
    testCase2[1][6] = "WPawn"
    testCase2[3][6] = "WBishop"
    testCase2[0][7] = "BQueen"

    return testCase2

#Testing Getting out of Check White
def getOutTestWhite(testCase3):
    testCase3[0][0] = "WKing"
    testCase3[0][7] = "BQueen"
    return testCase3



#Testing Getting out of Check Black
def getTestCase4(testCase4):
    testCase4[0][0]="BKing"
    testCase4[0][8]="WRook"
    return testCase4

#Testing Checkmate detects White
def getTestCase5(testCase5):
    testCase5[0][0] = "WKing"
    testCase5[0][8] = "BQueen"
    testCase5[1][8] = "BRook"
    return testCase5

#Testing Checkmate detects Black
def getTestCase6(testCase6):
    testCase5[0][0] = "BKing"
    testCase5[0][8] = "WQueen"
    testCase5[1][8] = "WRook"
    return testCase6




def testCase2():
    test = False
    return test

def testWhiteCheck(Colour,KingSpace,Board):
    moveList = validKing(Colour, KingSpace, Board)
    if moveList:
        return True
    else:
        return False

def testCase4():
    test = False
    return test

def testCase5():
    test = False
    return test

def testCase6():
    test = False
    return test


def getPawnCaptureBoard(currentBoard):
    currentBoard[5][5] = "WPawn"
    currentBoard[4][6] = "BPawn"
    return currentBoard



def testPawnCapture(Colour, currentBoard, ExpectedOutput):
    validMoves = validPawn(Colour,currentBoard)
    current= validMoves[0][0]
    currentBoard = movePiece(current,next)

#    if currentBoard == ExpectedOutput:
#        return True
#    else:
#        return False


def getEnPassantBoard(currentBoard):
    currentBoard[5][5] = "WPawn"
    currentBoard[4][5] = "BPawn"
    return currentBoard

def testEnPassantCapture(currentBoard,ExpectedOutput):
    if currentBoard == ExpectedOutput:
        return True
    else:
        return False




def getPawnPromotion(currentBoard):
    currentBoard[5][6] = "WPawn"

def testPawnPromotion(currentBoard,ExpectedOutput):

    if currentBoard == ExpectedOutput:
        return True
    else:
        return False





if __name__ == '__main__':

    #Testing Valid Moves

    #Starting Board State
    w, h = 8, 8;
    testCase1 = [[0 for x in range(w)] for y in range(h)]
    testCase1 = getTestCase1(testCase1)

    #White
    testCase1 = []
    testCase1("White",testCase1,testSolution1)


    #Black
    testCase1("Black",testCase1,testSolution1)

    #Not Initial Board State
    w, h = 8, 8;
    testCase2 = [[0 for x in range(w)] for y in range(h)]
    testCase2 = getTestCase2(testCase2)
    testCase2("White",testCase2,testSolution2)
    testCase2("Black",testCase2,testSolution2)

    #Get Out of Check White
    w, h = 8, 8;
    testCase3 = [[0 for x in range(w)] for y in range(h)]
    testCase3 = getTestCase2(testCase3)
    testCase3("White",testCase3,testSolution3)

    #Get out of Check Black
    w, h = 8, 8;
    testCase4 = [[0 for x in range(w)] for y in range(h)]
    testCase4 = getTestCase2(testCase4)
    testCase4("Black",testCase4,testSolution4)

    w, h = 8, 8
    testCase5 = [[0 for x in range(w)] for y in range(h)]
    testCase5 = getTestCase5(testCase5)
    testCase5(testCase5,testSolution5)

    w, h = 8, 8
    testCase6 = [[0 for x in range(w)] for y in range(h)]
    testCase6 = getTestCase5(testCase6)
    testCase5(testCase6,testSolution6)




    #Pawn Capture Normal
    w, h = 8, 8
    testCase7 = [[0 for x in range(w)] for y in range(h)]
    testCase7 = getPawnCaptureBoard(testCase7)
    PawnCapture(testCase6,testSolution7)

    #Pawn Capture En passant
    w, h = 8, 8
    testCase8 = [[0 for x in range(w)] for y in range(h)]
    testCase8 = getEnPassantBoard(testCase8)
    testCase8(testCase6,testSolution8)

    #Pawn Promotion
    w,h = 8,8
    testCase8 = [[0 for x in range(w)] for y in range(h)]
    testCase8 = getPawnPromotion(testCase8)
    PawnPromtion(testCase6,testSolution8)







    #Rook Capture Horizontally Left
    w, h = 8, 8
    testCase9 = [[0 for x in range(w)] for y in range(h)]
    testCase9 = getTestCase5(testCase9)
    testCase9(testCase9,testSolution9)


    #Rook Capture Horizontally Right
    w, h = 8, 8
    testCase10 = [[0 for x in range(w)] for y in range(h)]
    testCase10 = getTestCase5(testCase10)
    testCase10(testCase9,testSolution10)


    #Rook Capture Vertically Up
    w, h = 8, 8
    testCase10 = [[0 for x in range(w)] for y in range(h)]
    testCase10 = getTestCase5(testCase10)
    testCase10(testCase9,testSolution10)


    #Rook Capture Vertically Down
    w, h = 8, 8
    testCase10 = [[0 for x in range(w)] for y in range(h)]
    testCase10 = getTestCase5(testCase10)
    testCase10(testCase9,testSolution10)


    #Bishop Left Up
    #Bishop Left Down
    #Bishop Right Up
    #Bishop Right Down


    #Knight 1
    #Knight 2
    #Knight 3
    #Knight 4
    #Knight 5
    #Knight 6
    #Knight 7
    #Knight 8

    #Queen Diagonal Left Up
    #Queen Diagonal Left Down
    #Queen Diagonal Right Up
    #Queen Diagonal Right Down

    #Queen Horizontal Right
    #Queen Horizontal Left
    #Queen Vertical Up
    #Queen Vertical Down
