import json

#White Methods
def bishopBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"] = -50
    BoardValues["a2"] = 0
    BoardValues["a3"] = 0
    BoardValues["a4"] = 0
    BoardValues["a5"] = 0
    BoardValues["a6"] = 0
    BoardValues["a7"] = 0
    BoardValues["a8"] = -40

    BoardValues["b1"] = -20
    BoardValues["b2"] = 5
    BoardValues["b3"] = 0
    BoardValues["b4"] = 5
    BoardValues["b5"] = 10
    BoardValues["b6"] = 10
    BoardValues["b7"] = 5
    BoardValues["b8"] = -20

    BoardValues["c1"] = -10
    BoardValues["c2"] = 0
    BoardValues["c3"] = 5
    BoardValues["c4"] = 10
    BoardValues["c5"] = 10
    BoardValues["c6"] = 10
    BoardValues["c7"] = 5
    BoardValues["c8"] = -15

    BoardValues["d1"] = -20
    BoardValues["d2"] = 0
    BoardValues["d3"] = 5
    BoardValues["d4"] = 18
    BoardValues["d5"] = 18
    BoardValues["d6"] = 18
    BoardValues["d7"] = 5
    BoardValues["d8"] = -15

    BoardValues["e1"]=-20
    BoardValues["e2"]=0
    BoardValues["e3"]=5
    BoardValues["e4"]=18
    BoardValues["e5"]=18
    BoardValues["e6"]=18
    BoardValues["e7"]=5
    BoardValues["e8"] = -15

    BoardValues["f1"]=-10
    BoardValues["f2"]=0
    BoardValues["f3"]=5
    BoardValues["f4"]=10
    BoardValues["f5"]=10
    BoardValues["f6"]=10
    BoardValues["f7"]=5
    BoardValues["f8"]=-15

    BoardValues["g1"]=-20
    BoardValues["g2"]=5
    BoardValues["g3"]=0
    BoardValues["g4"]=5
    BoardValues["g5"]=10
    BoardValues["g6"]=10
    BoardValues["g7"]=0
    BoardValues["g8"]=-20

    BoardValues["h1"]=-50
    BoardValues["h2"]=0
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=0
    BoardValues["h8"]=-40
    return BoardValues

def knightBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=-50
    BoardValues["a2"]=-5
    BoardValues["a3"]=-5
    BoardValues["a4"]=-5
    BoardValues["a5"]=-5
    BoardValues["a6"]=-5
    BoardValues["a7"]=-5
    BoardValues["a8"]=-50

    BoardValues["b1"]=-20
    BoardValues["b2"]=0
    BoardValues["b3"]=5
    BoardValues["b4"]=5
    BoardValues["b5"]=5
    BoardValues["b6"]=5
    BoardValues["b7"]=5
    BoardValues["b8"]=-10

    BoardValues["c1"]=-10
    BoardValues["c2"]=5
    BoardValues["c3"]=8
    BoardValues["c4"]=10
    BoardValues["c5"]=10
    BoardValues["c6"]=10
    BoardValues["c7"]=5
    BoardValues["c8"]=-5

    BoardValues["d1"]=-10
    BoardValues["d2"]=5
    BoardValues["d3"]=8
    BoardValues["d4"]=15
    BoardValues["d5"]=15
    BoardValues["d6"]=15
    BoardValues["d7"]=5
    BoardValues["d8"]=-5

    BoardValues["e1"]=-10
    BoardValues["e2"]=5
    BoardValues["e3"]=8
    BoardValues["e4"]=15
    BoardValues["e5"]=15
    BoardValues["e6"]=15
    BoardValues["e7"]=5
    BoardValues["e8"]=-5

    BoardValues["f1"]=-10
    BoardValues["f2"]=5
    BoardValues["f3"]=8
    BoardValues["f4"]=10
    BoardValues["f5"]=10
    BoardValues["f6"]=10
    BoardValues["f7"]=5
    BoardValues["f8"]=-5

    BoardValues["g1"]=-20
    BoardValues["g2"]=0
    BoardValues["g3"]=5
    BoardValues["g4"]=5
    BoardValues["g5"]=5
    BoardValues["g6"]=5
    BoardValues["g7"]=5
    BoardValues["g8"]=-10

    BoardValues["h1"]=-50
    BoardValues["h2"]=-5
    BoardValues["h3"]=-5
    BoardValues["h4"]=-5
    BoardValues["h5"]=-5
    BoardValues["h6"]=-5
    BoardValues["h7"]=-5
    BoardValues["h8"]=-40

    return BoardValues

def rookBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=0
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=5
    BoardValues["a8"]=10

    BoardValues["b1"]=0
    BoardValues["b2"]=0
    BoardValues["b3"]=0
    BoardValues["b4"]=0
    BoardValues["b5"]=0
    BoardValues["b6"]=0
    BoardValues["b7"]=5
    BoardValues["b8"]=10

    BoardValues["c1"]=5
    BoardValues["c2"]=5
    BoardValues["c3"]=5
    BoardValues["c4"]=5
    BoardValues["c5"]=5
    BoardValues["c6"]=5
    BoardValues["c7"]=5
    BoardValues["c8"]=10

    BoardValues["d1"]=10
    BoardValues["d2"]=10
    BoardValues["d3"]=10
    BoardValues["d4"]=10
    BoardValues["d5"]=10
    BoardValues["d6"]=10
    BoardValues["d7"]=10
    BoardValues["d8"]=10

    BoardValues["e1"]=10
    BoardValues["e2"]=10
    BoardValues["e3"]=10
    BoardValues["e4"]=10
    BoardValues["e5"]=10
    BoardValues["e6"]=10
    BoardValues["e7"]=10
    BoardValues["e8"]=10

    BoardValues["f1"]=5
    BoardValues["f2"]=5
    BoardValues["f3"]=5
    BoardValues["f4"]=5
    BoardValues["f5"]=5
    BoardValues["f6"]=5
    BoardValues["f7"]=5
    BoardValues["f8"]=10

    BoardValues["g1"]=0
    BoardValues["g2"]=0
    BoardValues["g3"]=0
    BoardValues["g4"]=0
    BoardValues["g5"]=0
    BoardValues["g6"]=0
    BoardValues["g7"]=5
    BoardValues["g8"]=10

    BoardValues["h1"]=0
    BoardValues["h2"]=0
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=5
    BoardValues["h8"]=10
    return BoardValues

def queenBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"] = 0
    BoardValues["a2"] = 0
    BoardValues["a3"] = 0 
    BoardValues["a4"] = 0
    BoardValues["a5"] = 0
    BoardValues["a6"] = 0
    BoardValues["a7"] = 0
    BoardValues["a8"] = 0

    BoardValues["b1"] = 0
    BoardValues["b2"] = 0
    BoardValues["b3"] = 0
    BoardValues["b4"] = 0
    BoardValues["b5"] = 0
    BoardValues["b6"] = 0
    BoardValues["b7"] = 0
    BoardValues["b8"] = 0

    BoardValues["c1"] = 0
    BoardValues["c2"] = 0
    BoardValues["c3"] = 10
    BoardValues["c4"] = 10
    BoardValues["c5"] = 10
    BoardValues["c6"] = 10
    BoardValues["c7"] = 0
    BoardValues["c8"] = 0

    BoardValues["d1"] = 0
    BoardValues["d2"] = 0
    BoardValues["d3"] = 10
    BoardValues["d4"] = 15
    BoardValues["d5"] = 15
    BoardValues["d6"] = 10
    BoardValues["d7"] = 0
    BoardValues["d8"] = 0

    BoardValues["e1"] = 0
    BoardValues["e2"] = 0
    BoardValues["e3"] = 10
    BoardValues["e4"] = 15
    BoardValues["e5"] = 15
    BoardValues["e6"] = 10
    BoardValues["e7"] = 0
    BoardValues["e8"] = 0

    BoardValues["f1"] = 0
    BoardValues["f2"] = 0
    BoardValues["f3"] = 10
    BoardValues["f4"] = 10
    BoardValues["f5"] = 10
    BoardValues["f6"] = 10
    BoardValues["f7"] = 0
    BoardValues["f8"] = 0

    BoardValues["g1"] = 0
    BoardValues["g2"] = 0
    BoardValues["g3"] = 0
    BoardValues["g4"] = 0
    BoardValues["g5"] = 0
    BoardValues["g6"] = 0
    BoardValues["g7"] = 0
    BoardValues["g8"] = 0

    BoardValues["h1"] = 0
    BoardValues["h2"] = 0
    BoardValues["h3"] = 0
    BoardValues["h4"] = 0
    BoardValues["h5"] = 0
    BoardValues["h6"] = 0
    BoardValues["h7"] = 0
    BoardValues["h8"] = 0
    return BoardValues

def kingBoardValuesWhiteEarly():
    BoardValues={}   
    BoardValues["a1"]=24
    BoardValues["a2"]=24
    BoardValues["a3"]=16
    BoardValues["a4"]=12
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=0
    BoardValues["a8"]=0

    BoardValues["b1"] = 24
    BoardValues["b2"] = 20
    BoardValues["b3"] = 12
    BoardValues["b4"] = 8
    BoardValues["b5"] = 0
    BoardValues["b6"] = 0
    BoardValues["b7"] = 0
    BoardValues["b8"] = 0

    BoardValues["c1"] = 24
    BoardValues["c2"] = 16
    BoardValues["c3"] = 8
    BoardValues["c4"] = 4
    BoardValues["c5"] = 0
    BoardValues["c6"] = 0
    BoardValues["c7"] = 0
    BoardValues["c8"] = 0

    BoardValues["d1"] = 16
    BoardValues["d2"] = 12
    BoardValues["d3"] = 4
    BoardValues["d4"] = 0
    BoardValues["d5"] = 0
    BoardValues["d6"] = 0
    BoardValues["d7"] = 0
    BoardValues["d8"] = 0

    BoardValues["e1"] = 16
    BoardValues["e2"] = 12
    BoardValues["e3"] = 4
    BoardValues["e4"] = 0
    BoardValues["e5"] = 0
    BoardValues["e6"] = 0
    BoardValues["e7"] = 0
    BoardValues["e8"] = 0

    BoardValues["f1"] = 6
    BoardValues["f2"] = 16
    BoardValues["f3"] = 8
    BoardValues["f4"] = 4
    BoardValues["f5"] = 0
    BoardValues["f6"] = 0
    BoardValues["f7"] = 0
    BoardValues["f8"] = 0

    BoardValues["g1"] = 32
    BoardValues["g2"] = 20
    BoardValues["g3"] = 12
    BoardValues["g4"] = 8
    BoardValues["g5"] = 0
    BoardValues["g6"] = 0
    BoardValues["g7"] = 0
    BoardValues["g8"] = 0

    BoardValues["h1"] = 32
    BoardValues["h2"] = 24
    BoardValues["h3"] = 16
    BoardValues["h4"] = 12
    BoardValues["h5"] = 0
    BoardValues["h6"] = 0
    BoardValues["h7"] = 0
    BoardValues["h8"] = 0
    return BoardValues

def kingBoardValuesWhiteLate():
    BoardValues={}   
    BoardValues["a1"] = -40
    BoardValues["a2"] = -10
    BoardValues["a3"] = 0
    BoardValues["a4"] = 0
    BoardValues["a5"] = 0
    BoardValues["a6"] = 0
    BoardValues["a7"] = -5
    BoardValues["a8"] = -30

    BoardValues["b1"] = -10
    BoardValues["b2"] = 0
    BoardValues["b3"] = 0
    BoardValues["b4"] = 0
    BoardValues["b5"] = 0
    BoardValues["b6"] = 0
    BoardValues["b7"] = 0
    BoardValues["b8"] = -5

    BoardValues["c1"] = -5
    BoardValues["c2"] = 0
    BoardValues["c3"] = 0
    BoardValues["c4"] = 0
    BoardValues["c5"] = 0
    BoardValues["c6"] = 0
    BoardValues["c7"] = 0
    BoardValues["c8"] = 0

    BoardValues["d1"] = -5
    BoardValues["d2"] = 0 
    BoardValues["d3"] = 0
    BoardValues["d4"] = 5
    BoardValues["d5"] = 5
    BoardValues["d6"] = 0
    BoardValues["d7"] = 0
    BoardValues["d8"] = 0

    BoardValues["e1"] = -5
    BoardValues["e2"] = 0
    BoardValues["e3"] = 0
    BoardValues["e4"] = 5
    BoardValues["e5"] = 5
    BoardValues["e6"] = 0
    BoardValues["e7"] = 0
    BoardValues["e8"] = 0

    BoardValues["f1"] = -5
    BoardValues["f2"] = 0
    BoardValues["f3"] = 0
    BoardValues["f4"] = 0
    BoardValues["f5"] = 0
    BoardValues["f6"] = 0
    BoardValues["f7"] = 0
    BoardValues["f8"] = 0

    BoardValues["g1"] = -10
    BoardValues["g2"] = 0
    BoardValues["g3"] = 0
    BoardValues["g4"] = 0
    BoardValues["g5"] = 0
    BoardValues["g6"] = 0
    BoardValues["g7"] = 0
    BoardValues["g8"] = -5

    BoardValues["h1"] = -40
    BoardValues["h2"] = -10
    BoardValues["h3"] = 0
    BoardValues["h4"] = 0
    BoardValues["h5"] = 0
    BoardValues["h6"] = 0
    BoardValues["h7"] = -5
    BoardValues["h8"] = -30
    return BoardValues

def pawnBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=0
    BoardValues["a3"]=2
    BoardValues["a4"]=4
    BoardValues["a5"]=8
    BoardValues["a6"]=12
    BoardValues["a7"]=20
    BoardValues["a8"]=0

    BoardValues["b1"]=0
    BoardValues["b2"]=0
    BoardValues["b3"]=2
    BoardValues["b4"]=6
    BoardValues["b5"]=10
    BoardValues["b6"]=14
    BoardValues["b7"]=26
    BoardValues["b8"]=0

    BoardValues["c1"]=0
    BoardValues["c2"]=0
    BoardValues["c3"]=4
    BoardValues["c4"]=8
    BoardValues["c5"]=12
    BoardValues["c6"]=16
    BoardValues["c7"]=26
    BoardValues["c8"]=0

    BoardValues["d1"]=0
    BoardValues["d2"]=-4
    BoardValues["d3"]=6
    BoardValues["d4"]=14
    BoardValues["d5"]=18
    BoardValues["d6"]=21
    BoardValues["d7"]=28
    BoardValues["d8"]=0

    BoardValues["e1"]=0
    BoardValues["e2"]=-4
    BoardValues["e3"]=6
    BoardValues["e4"]=16
    BoardValues["e5"]=18
    BoardValues["e6"]=21
    BoardValues["e7"]=28
    BoardValues["e8"]=0

    BoardValues["f1"]=0
    BoardValues["f2"]=0
    BoardValues["f3"]=4
    BoardValues["f4"]=8
    BoardValues["f5"]=12
    BoardValues["f6"]=16
    BoardValues["f7"]=26
    BoardValues["f8"]=0

    BoardValues["g1"]=0
    BoardValues["g2"]=0
    BoardValues["g3"]=2
    BoardValues["g4"]=6
    BoardValues["g5"]=12
    BoardValues["g6"]=14
    BoardValues["g7"]=26
    BoardValues["g8"]=0

    BoardValues["h1"]=0
    BoardValues["h2"]=0
    BoardValues["h3"]=2
    BoardValues["h4"]=4
    BoardValues["h5"]=8
    BoardValues["h6"]=12
    BoardValues["h7"]=20
    BoardValues["h8"]=0
    return BoardValues


#Black Methods
def bishopBoardValuesBlack():
    BoardValues={}   
    BoardValues["a1"]=40
    BoardValues["a2"]=0
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=0
    BoardValues["a8"]=50

    BoardValues["b1"]=20
    BoardValues["b2"]=-5
    BoardValues["b3"]=-10
    BoardValues["b4"]=-10
    BoardValues["b5"]=-5
    BoardValues["b6"]=0
    BoardValues["b7"]=-5
    BoardValues["b8"]=20

    BoardValues["c1"]= 15
    BoardValues["c2"]= -5
    BoardValues["c3"]= -10
    BoardValues["c4"]= -10
    BoardValues["c5"]= -10
    BoardValues["c6"]= -5
    BoardValues["c7"]= 0
    BoardValues["c8"]= 10

    BoardValues["d1"]=15
    BoardValues["d2"]=-5
    BoardValues["d3"]=-18
    BoardValues["d4"]=-18
    BoardValues["d5"]=-18
    BoardValues["d6"]=-5
    BoardValues["d7"]=0
    BoardValues["d8"]=20

    BoardValues["e1"]=15
    BoardValues["e2"]=-5
    BoardValues["e3"]=-18
    BoardValues["e4"]=-18
    BoardValues["e5"]=-18
    BoardValues["e6"]=-5
    BoardValues["e7"]=0
    BoardValues["e8"]=20

    BoardValues["f1"]=15
    BoardValues["f2"]=-5
    BoardValues["f3"]=-10
    BoardValues["f4"]=-10
    BoardValues["f5"]=-10
    BoardValues["f6"]=-5
    BoardValues["f7"]=0
    BoardValues["f8"]=10

    BoardValues["g1"]=20
    BoardValues["g2"]=0
    BoardValues["g3"]=-10
    BoardValues["g4"]=-10
    BoardValues["g5"]=-5
    BoardValues["g6"]=0
    BoardValues["g7"]=-5
    BoardValues["g8"]=20

    BoardValues["h1"]=40
    BoardValues["h2"]=0
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=0
    BoardValues["h8"]=50
    return BoardValues

def knightBoardValuesBlack():
    BoardValues={}   
    BoardValues["a1"]=40
    BoardValues["a2"]=5
    BoardValues["a3"]=5
    BoardValues["a4"]=5
    BoardValues["a5"]=5
    BoardValues["a6"]=5
    BoardValues["a7"]=5
    BoardValues["a8"]=50

    BoardValues["b1"]=10
    BoardValues["b2"]=-5
    BoardValues["b3"]=-5
    BoardValues["b4"]=-5
    BoardValues["b5"]=-5
    BoardValues["b6"]=-5
    BoardValues["b7"]=0
    BoardValues["b8"]=20

    BoardValues["c1"]=5
    BoardValues["c2"]=-5
    BoardValues["c3"]=-10
    BoardValues["c4"]=-10
    BoardValues["c5"]=-10
    BoardValues["c6"]=-8
    BoardValues["c7"]=-5
    BoardValues["c8"]=10

    BoardValues["d1"]=5
    BoardValues["d2"]=-5
    BoardValues["d3"]=-15
    BoardValues["d4"]=-15
    BoardValues["d5"]=-15
    BoardValues["d6"]=-8
    BoardValues["d7"]=-5
    BoardValues["d8"]=10

    BoardValues["e1"]=5
    BoardValues["e2"]=-5
    BoardValues["e3"]=-15
    BoardValues["e4"]=-15
    BoardValues["e5"]=-15
    BoardValues["e6"]=-8
    BoardValues["e7"]=-5
    BoardValues["e8"]=10

    BoardValues["f1"]=5
    BoardValues["f2"]=-5
    BoardValues["f3"]=-10
    BoardValues["f4"]=-10
    BoardValues["f5"]=-10
    BoardValues["f6"]=-8
    BoardValues["f7"]=-5
    BoardValues["f8"]=10

    BoardValues["g1"]=10
    BoardValues["g2"]=-5
    BoardValues["g3"]=-5
    BoardValues["g4"]=-5
    BoardValues["g5"]=-5
    BoardValues["g6"]=-5
    BoardValues["g7"]=0
    BoardValues["g8"]=20

    BoardValues["h1"]=40
    BoardValues["h2"]=5
    BoardValues["h3"]=5
    BoardValues["h4"]=5
    BoardValues["h5"]=5
    BoardValues["h6"]=5
    BoardValues["h7"]=5
    BoardValues["h8"]=50
    return BoardValues

def rookBoardValuesBlack():
    BoardValues={}   
    BoardValues["a1"]=-10
    BoardValues["a2"]=-5
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=0
    BoardValues["a8"]=0

    BoardValues["b1"]=-10
    BoardValues["b2"]=-5
    BoardValues["b3"]=0
    BoardValues["b4"]=0
    BoardValues["b5"]=0
    BoardValues["b6"]=0
    BoardValues["b7"]=0
    BoardValues["b8"]=0

    BoardValues["c1"]=-10
    BoardValues["c2"]=-5
    BoardValues["c3"]=-5
    BoardValues["c4"]=-5
    BoardValues["c5"]=-5
    BoardValues["c6"]=-5
    BoardValues["c7"]=-5
    BoardValues["c8"]=-5

    BoardValues["d1"]=-10
    BoardValues["d2"]=-10
    BoardValues["d3"]=-10
    BoardValues["d4"]=-10
    BoardValues["d5"]=-10
    BoardValues["d6"]=-10
    BoardValues["d7"]=-10
    BoardValues["d8"]=-10

    BoardValues["e1"]=-10
    BoardValues["e2"]=-10
    BoardValues["e3"]=-10
    BoardValues["e4"]=-10
    BoardValues["e5"]=-10
    BoardValues["e6"]=-10
    BoardValues["e7"]=-10
    BoardValues["e8"]=-10

    BoardValues["f1"]=-10
    BoardValues["f2"]=-5
    BoardValues["f3"]=-5
    BoardValues["f4"]=-5
    BoardValues["f5"]=-5
    BoardValues["f6"]=-5
    BoardValues["f7"]=-5
    BoardValues["f8"]=-5

    BoardValues["g1"]=-10
    BoardValues["g2"]=-5
    BoardValues["g3"]=0
    BoardValues["g4"]=0
    BoardValues["g5"]=0
    BoardValues["g6"]=0
    BoardValues["g7"]=0
    BoardValues["g8"]=0

    BoardValues["h1"]=-10
    BoardValues["h2"]=-5
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=0
    BoardValues["h8"]=0
    return BoardValues

def queenBoardValuesBlack():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=0
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=0
    BoardValues["a8"]=0

    BoardValues["b1"]=0
    BoardValues["b2"]=0
    BoardValues["b3"]=0
    BoardValues["b4"]=0
    BoardValues["b5"]=0
    BoardValues["b6"]=0
    BoardValues["b7"]=0
    BoardValues["b8"]=0

    BoardValues["c1"]=0
    BoardValues["c2"]=0
    BoardValues["c3"]=-10
    BoardValues["c4"]=-10
    BoardValues["c5"]=-10
    BoardValues["c6"]=-10
    BoardValues["c7"]=0
    BoardValues["c8"]=0

    BoardValues["d1"]=0
    BoardValues["d2"]=0
    BoardValues["d3"]=-10
    BoardValues["d4"]=-15
    BoardValues["d5"]=-15
    BoardValues["d6"]=-10
    BoardValues["d7"]=0
    BoardValues["d8"]=0

    BoardValues["e1"]=0
    BoardValues["e2"]=0
    BoardValues["e3"]=-10
    BoardValues["e4"]=-15
    BoardValues["e5"]=-15
    BoardValues["e6"]=-10
    BoardValues["e7"]=0
    BoardValues["e8"]=0

    BoardValues["f1"]=0
    BoardValues["f2"]=0
    BoardValues["f3"]=-10
    BoardValues["f4"]=-10
    BoardValues["f5"]=-10
    BoardValues["f6"]=-10
    BoardValues["f7"]=0
    BoardValues["f8"]=0

    BoardValues["g1"]=0
    BoardValues["g2"]=0
    BoardValues["g3"]=0
    BoardValues["g4"]=0
    BoardValues["g5"]=0
    BoardValues["g6"]=0
    BoardValues["g7"]=0
    BoardValues["g8"]=0

    BoardValues["h1"]=0
    BoardValues["h2"]=0
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=0
    BoardValues["h8"]=0
    return BoardValues

def kingBoardValuesBlackEarly():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=0
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=-12
    BoardValues["a6"]=-16
    BoardValues["a7"]=-24
    BoardValues["a8"]=-24

    BoardValues["b1"]=0
    BoardValues["b2"]=0
    BoardValues["b3"]=0
    BoardValues["b4"]=0
    BoardValues["b5"]=-8
    BoardValues["b6"]=-12
    BoardValues["b7"]=-20
    BoardValues["b8"]=-24

    BoardValues["c1"]=0
    BoardValues["c2"]=0
    BoardValues["c3"]=0
    BoardValues["c4"]=0
    BoardValues["c5"]=-4
    BoardValues["c6"]=-8
    BoardValues["c7"]=-16
    BoardValues["c8"]=-24

    BoardValues["d1"]=0
    BoardValues["d2"]=0
    BoardValues["d3"]=0
    BoardValues["d4"]=0
    BoardValues["d5"]=0
    BoardValues["d6"]=-4
    BoardValues["d7"]=-12
    BoardValues["d8"]=-16

    BoardValues["e1"]=0
    BoardValues["e2"]=0
    BoardValues["e3"]=0
    BoardValues["e4"]=0
    BoardValues["e5"]=0
    BoardValues["e6"]=-4
    BoardValues["e7"]=-12
    BoardValues["e8"]=-16

    BoardValues["f1"]=0
    BoardValues["f2"]=0
    BoardValues["f3"]=0
    BoardValues["f4"]=0
    BoardValues["f5"]=-4
    BoardValues["f6"]=-8
    BoardValues["f7"]=-16
    BoardValues["f8"]=-6

    BoardValues["g1"]=0
    BoardValues["g2"]=0
    BoardValues["g3"]=0
    BoardValues["g4"]=0
    BoardValues["g5"]=-8
    BoardValues["g6"]=-12
    BoardValues["g7"]=-20
    BoardValues["g8"]=-32

    BoardValues["h1"]=0
    BoardValues["h2"]=0
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=-12
    BoardValues["h6"]=-16
    BoardValues["h7"]=-24
    BoardValues["h8"]=-32
    return BoardValues

def kingBoardValuesBlackLate():
    BoardValues={}   
    BoardValues["a1"]=30
    BoardValues["a2"]=5
    BoardValues["a3"]=0
    BoardValues["a4"]=0
    BoardValues["a5"]=0
    BoardValues["a6"]=0
    BoardValues["a7"]=10
    BoardValues["a8"]=40

    BoardValues["b1"]=5
    BoardValues["b2"]=0
    BoardValues["b3"]=0
    BoardValues["b4"]=0
    BoardValues["b5"]=0
    BoardValues["b6"]=0
    BoardValues["b7"]=0
    BoardValues["b8"]=10

    BoardValues["c1"]=0
    BoardValues["c2"]=0
    BoardValues["c3"]=0
    BoardValues["c4"]=0
    BoardValues["c5"]=0
    BoardValues["c6"]=0
    BoardValues["c7"]=0
    BoardValues["c8"]=5

    BoardValues["d1"]=0
    BoardValues["d2"]=0
    BoardValues["d3"]=0
    BoardValues["d4"]=-5
    BoardValues["d5"]=-5
    BoardValues["d6"]=0
    BoardValues["d7"]=0
    BoardValues["d8"]=5

    BoardValues["e1"]=0
    BoardValues["e2"]=0
    BoardValues["e3"]=0
    BoardValues["e4"]=-5
    BoardValues["e5"]=-5
    BoardValues["e6"]=0
    BoardValues["e7"]=0
    BoardValues["e8"]=5

    BoardValues["f1"]=0
    BoardValues["f2"]=0
    BoardValues["f3"]=0
    BoardValues["f4"]=0
    BoardValues["f5"]=0
    BoardValues["f6"]=0
    BoardValues["f7"]=0
    BoardValues["f8"]=5

    BoardValues["g1"]=5
    BoardValues["g2"]=0
    BoardValues["g3"]=0
    BoardValues["g4"]=0
    BoardValues["g5"]=0
    BoardValues["g6"]=0
    BoardValues["g7"]=0
    BoardValues["g8"]=10

    BoardValues["h1"]=30
    BoardValues["h2"]=5
    BoardValues["h3"]=0
    BoardValues["h4"]=0
    BoardValues["h5"]=0
    BoardValues["h6"]=0
    BoardValues["h7"]=0
    BoardValues["h8"]=40
    return BoardValues

def pawnBoardValuesBlack():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=-20
    BoardValues["a3"]=-12
    BoardValues["a4"]=-8
    BoardValues["a5"]=-4
    BoardValues["a6"]=-2
    BoardValues["a7"]=0
    BoardValues["a8"]=0

    BoardValues["b1"]=0
    BoardValues["b2"]=-26
    BoardValues["b3"]=-14
    BoardValues["b4"]=-10
    BoardValues["b5"]=-6
    BoardValues["b6"]=-2
    BoardValues["b7"]=0
    BoardValues["b8"]=0

    BoardValues["c1"]=0
    BoardValues["c2"]=-26
    BoardValues["c3"]=-16
    BoardValues["c4"]=-12
    BoardValues["c5"]=-8
    BoardValues["c6"]=-4
    BoardValues["c7"]=0
    BoardValues["c8"]=0

    BoardValues["d1"]=0
    BoardValues["d2"]=-28
    BoardValues["d3"]=-21
    BoardValues["d4"]=-18
    BoardValues["d5"]=-16
    BoardValues["d6"]=-6
    BoardValues["d7"]=4
    BoardValues["d8"]=0

    BoardValues["e1"]=0
    BoardValues["e2"]=-28
    BoardValues["e3"]=-21
    BoardValues["e4"]=-18
    BoardValues["e5"]=-16
    BoardValues["e6"]=-6
    BoardValues["e7"]=4
    BoardValues["e8"]=0

    BoardValues["f1"]=0
    BoardValues["f2"]=-26
    BoardValues["f3"]=-16
    BoardValues["f4"]=-12
    BoardValues["f5"]=-8
    BoardValues["f6"]=-4
    BoardValues["f7"]=0
    BoardValues["f8"]=0

    BoardValues["g1"]=0
    BoardValues["g2"]=-26
    BoardValues["g3"]=-14
    BoardValues["g4"]=-10
    BoardValues["g5"]=-6
    BoardValues["g6"]=-2
    BoardValues["g7"]=0
    BoardValues["g8"]=0

    BoardValues["h1"]=0
    BoardValues["h2"]=-20
    BoardValues["h3"]=-12
    BoardValues["h4"]=-8
    BoardValues["h5"]=-4
    BoardValues["h6"]=-2
    BoardValues["h7"]=0
    BoardValues["h8"]=0
    return BoardValues


if __name__ == '__main__':
    BW = bishopBoardValuesWhite()
    with open('bishopWhite.txt','w') as file:
        file.write(json.dumps(BW))

    BB = bishopBoardValuesBlack()
    with open('bishopBlack.txt','w') as file:
        file.write(json.dumps(BB))

    KW = knightBoardValuesWhite()
    with open('knightWhite.txt','w') as file:
        file.write(json.dumps(KW))

    KB = knightBoardValuesBlack()
    with open('knightBlack.txt','w') as file:
        file.write(json.dumps(KB))

    RW = rookBoardValuesWhite()
    with open('rookWhite.txt','w') as file:
        file.write(json.dumps(RW))

    RB = rookBoardValuesBlack()
    with open('rookBlack.txt','w') as file:
        file.write(json.dumps(RB))

    QW = queenBoardValuesWhite()
    with open('queenWhite.txt','w') as file:
        file.write(json.dumps(QW))

    QB = queenBoardValuesBlack()
    with open('queenBlack.txt','w') as file:
        file.write(json.dumps(QB))

    KWE = kingBoardValuesWhiteEarly()
    with open('kingEarlyWhite.txt','w') as file:
        file.write(json.dumps(KWE))

    KBE = kingBoardValuesBlackEarly()
    with open('kingEarlyBlack.txt','w') as file:
        file.write(json.dumps(KBE))

    KWL = kingBoardValuesWhiteLate()
    with open('kingLateWhite.txt','w') as file:
        file.write(json.dumps(KWL))

    KBL = kingBoardValuesBlackLate()
    with open('kingLateBlack.txt','w') as file:
        file.write(json.dumps(KBL))

    PW = pawnBoardValuesWhite()
    with open('pawnWhite.txt','w') as file:
        file.write(json.dumps(PW))

    PB = pawnBoardValuesBlack()
    with open('pawnBlack.txt','w') as file:
        file.write(json.dumps(PB))