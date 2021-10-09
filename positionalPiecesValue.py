import json

#White Methods
def bishopBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"] = -53
    BoardValues["a2"] = -15
    BoardValues["a3"] = -7
    BoardValues["a4"] = -5
    BoardValues["a5"] = -12
    BoardValues["a6"] = -16
    BoardValues["a7"] = -17
    BoardValues["a8"] = -48

    BoardValues["b1"] = -5
    BoardValues["b2"] = 8
    BoardValues["b3"] = 21
    BoardValues["b4"] = 11
    BoardValues["b5"] = 29
    BoardValues["b6"] = 6
    BoardValues["b7"] = -14
    BoardValues["b8"] = 1

    BoardValues["c1"] = -8
    BoardValues["c2"] = 19
    BoardValues["c3"] = -5
    BoardValues["c4"] = 25
    BoardValues["c5"] = 22
    BoardValues["c6"] = 1
    BoardValues["c7"] = 5
    BoardValues["c8"] = -14

    BoardValues["d1"] = -23
    BoardValues["d2"] = 4
    BoardValues["d3"] = 17
    BoardValues["d4"] = 39
    BoardValues["d5"] = 31
    BoardValues["d6"] = 11
    BoardValues["d7"] = 6
    BoardValues["d8"] = -23

    BoardValues["e1"]=-23
    BoardValues["e2"]=4
    BoardValues["e3"]=17
    BoardValues["e4"]=39
    BoardValues["e5"]=31
    BoardValues["e6"]=11
    BoardValues["e7"]=4
    BoardValues["e8"]=-23

    BoardValues["f1"]=-8
    BoardValues["f2"]=19
    BoardValues["f3"]=-5
    BoardValues["f4"]=25
    BoardValues["f5"]=22
    BoardValues["f6"]=1
    BoardValues["f7"]=5
    BoardValues["f8"]=-14

    BoardValues["g1"]=-5
    BoardValues["g2"]=8
    BoardValues["g3"]=21
    BoardValues["g4"]=11
    BoardValues["g5"]=29
    BoardValues["g6"]=6
    BoardValues["g7"]=-14
    BoardValues["g8"]=1

    BoardValues["h1"]=-53
    BoardValues["h2"]=-15
    BoardValues["h3"]=-7
    BoardValues["h4"]=-5
    BoardValues["h5"]=-12
    BoardValues["h6"]=-16
    BoardValues["h7"]=-17
    BoardValues["h8"]=-48
    return BoardValues

def bishopValueEndGameWhite():
    BoardValues={}   
    BoardValues["a1"] = -57
    BoardValues["a2"] = -37
    BoardValues["a3"] = -16
    BoardValues["a4"] = -20
    BoardValues["a5"] = -17
    BoardValues["a6"] = -30
    BoardValues["a7"] = -31
    BoardValues["a8"] = -46

    BoardValues["b1"] = -30
    BoardValues["b2"] = -13
    BoardValues["b3"] = -1
    BoardValues["b4"] = -6
    BoardValues["b5"] = -1
    BoardValues["b6"] = 6
    BoardValues["b7"] = -20
    BoardValues["b8"] = -42

    BoardValues["c1"] = -37
    BoardValues["c2"] = -17
    BoardValues["c3"] = -2
    BoardValues["c4"] = 37
    BoardValues["c5"] = -14
    BoardValues["c6"] = 4
    BoardValues["c7"] = -1
    BoardValues["c8"] = -37

    BoardValues["d1"] = -12
    BoardValues["d2"] = 1
    BoardValues["d3"] = 10
    BoardValues["d4"] = 17
    BoardValues["d5"] = 15
    BoardValues["d6"] = 6
    BoardValues["d7"] = 1
    BoardValues["d8"] = -24

    BoardValues["e1"]=-12
    BoardValues["e2"]=1
    BoardValues["e3"]=10
    BoardValues["e4"]=17
    BoardValues["e5"]=15
    BoardValues["e6"]=6
    BoardValues["e7"]=1
    BoardValues["e8"]=-24

    BoardValues["f1"]=-37
    BoardValues["f2"]=-17
    BoardValues["f3"]=-2
    BoardValues["f4"]=0
    BoardValues["f5"]=-14
    BoardValues["f6"]=4
    BoardValues["f7"]=-1
    BoardValues["f8"]=-37

    BoardValues["g1"]=-30
    BoardValues["g2"]=-13
    BoardValues["g3"]=-1
    BoardValues["g4"]=-6
    BoardValues["g5"]=-1
    BoardValues["g6"]=6
    BoardValues["g7"]=-20
    BoardValues["g8"]=-42

    BoardValues["h1"]=-57
    BoardValues["h2"]=-37
    BoardValues["h3"]=-16
    BoardValues["h4"]=-20
    BoardValues["h5"]=-17
    BoardValues["h6"]=-30
    BoardValues["h7"]=-31
    BoardValues["h8"]=-46
    return BoardValues



def knightBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=-175
    BoardValues["a2"]=-77
    BoardValues["a3"]=-61
    BoardValues["a4"]=-35
    BoardValues["a5"]=-34
    BoardValues["a6"]=-9
    BoardValues["a7"]=-67
    BoardValues["a8"]=-201

    BoardValues["b1"]=-92
    BoardValues["b2"]=-42
    BoardValues["b3"]=-17
    BoardValues["b4"]=8
    BoardValues["b5"]=13
    BoardValues["b6"]=22
    BoardValues["b7"]=-27
    BoardValues["b8"]=-83

    BoardValues["c1"]=-74
    BoardValues["c2"]=-27
    BoardValues["c3"]=6
    BoardValues["c4"]=40
    BoardValues["c5"]=44
    BoardValues["c6"]=58
    BoardValues["c7"]=4
    BoardValues["c8"]=-56

    BoardValues["d1"]=-73
    BoardValues["d2"]=-15
    BoardValues["d3"]=12
    BoardValues["d4"]=49
    BoardValues["d5"]=51
    BoardValues["d6"]=53
    BoardValues["d7"]=37
    BoardValues["d8"]=-26

    BoardValues["e1"]=-73
    BoardValues["e2"]=-15
    BoardValues["e3"]=12
    BoardValues["e4"]=49
    BoardValues["e5"]=51
    BoardValues["e6"]=53
    BoardValues["e7"]=37
    BoardValues["e8"]=-26

    BoardValues["f1"]=-74
    BoardValues["f2"]=-27
    BoardValues["f3"]=6
    BoardValues["f4"]=40
    BoardValues["f5"]=44
    BoardValues["f6"]=58
    BoardValues["f7"]=4
    BoardValues["f8"]=-56

    BoardValues["g1"]=-92
    BoardValues["g2"]=-41
    BoardValues["g3"]=-17
    BoardValues["g4"]=8
    BoardValues["g5"]=13
    BoardValues["g6"]=22
    BoardValues["g7"]=-27
    BoardValues["g8"]=-83

    BoardValues["h1"]=-175
    BoardValues["h2"]=-77
    BoardValues["h3"]=-61
    BoardValues["h4"]=-35
    BoardValues["h5"]=-34
    BoardValues["h6"]=-9
    BoardValues["h7"]=-67
    BoardValues["h8"]=-201

    return BoardValues

def knightValueEndGameWhite():
    BoardValues={}   
    BoardValues["a1"]=-96
    BoardValues["a2"]=-67
    BoardValues["a3"]=-40
    BoardValues["a4"]=-35
    BoardValues["a5"]=-45
    BoardValues["a6"]=-51
    BoardValues["a7"]=-67
    BoardValues["a8"]=-100

    BoardValues["b1"]=-65
    BoardValues["b2"]=-54
    BoardValues["b3"]=-27
    BoardValues["b4"]=-2
    BoardValues["b5"]=-16
    BoardValues["b6"]=-44
    BoardValues["b7"]=-50
    BoardValues["b8"]=-88

    BoardValues["c1"]=-49
    BoardValues["c2"]=-18
    BoardValues["c3"]=-8
    BoardValues["c4"]=13
    BoardValues["c5"]=9
    BoardValues["c6"]=-16
    BoardValues["c7"]=-51
    BoardValues["c8"]=-56

    BoardValues["d1"]=-21
    BoardValues["d2"]=8
    BoardValues["d3"]=29
    BoardValues["d4"]=28
    BoardValues["d5"]=39
    BoardValues["d6"]=17
    BoardValues["d7"]=12
    BoardValues["d8"]=-17

    BoardValues["e1"]=-21
    BoardValues["e2"]=8
    BoardValues["e3"]=29
    BoardValues["e4"]=28
    BoardValues["e5"]=39
    BoardValues["e6"]=17
    BoardValues["e7"]=12
    BoardValues["e8"]=-17

    BoardValues["f1"]=-49
    BoardValues["f2"]=-18
    BoardValues["f3"]=-8
    BoardValues["f4"]=13
    BoardValues["f5"]=9
    BoardValues["f6"]=-16
    BoardValues["f7"]=-51
    BoardValues["f8"]=-56

    BoardValues["g1"]=-65
    BoardValues["g2"]=-54
    BoardValues["g3"]=-27
    BoardValues["g4"]=-2
    BoardValues["g5"]=-16
    BoardValues["g6"]=-44
    BoardValues["g7"]=-50
    BoardValues["g8"]=-88

    BoardValues["h1"]=-96
    BoardValues["h2"]=-67
    BoardValues["h3"]=-40
    BoardValues["h4"]=-35
    BoardValues["h5"]=-45
    BoardValues["h6"]=-51
    BoardValues["h7"]=-69
    BoardValues["h8"]=-100

    return BoardValues


def rookBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=-31
    BoardValues["a2"]=-21
    BoardValues["a3"]=-25
    BoardValues["a4"]=-13
    BoardValues["a5"]=-27
    BoardValues["a6"]=-22
    BoardValues["a7"]=-2
    BoardValues["a8"]=-17

    BoardValues["b1"]=-20
    BoardValues["b2"]=-13
    BoardValues["b3"]=-11
    BoardValues["b4"]=-5
    BoardValues["b5"]=-15
    BoardValues["b6"]=-2
    BoardValues["b7"]=12
    BoardValues["b8"]=-19

    BoardValues["c1"]=-14
    BoardValues["c2"]=-8
    BoardValues["c3"]=-1
    BoardValues["c4"]=-4
    BoardValues["c5"]=-4
    BoardValues["c6"]=6
    BoardValues["c7"]=16
    BoardValues["c8"]=-1

    BoardValues["d1"]=-5
    BoardValues["d2"]=6
    BoardValues["d3"]=3
    BoardValues["d4"]=-6
    BoardValues["d5"]=3
    BoardValues["d6"]=12
    BoardValues["d7"]=18
    BoardValues["d8"]=8

    BoardValues["e1"]=-5
    BoardValues["e2"]=6
    BoardValues["e3"]=3
    BoardValues["e4"]=-6
    BoardValues["e5"]=3
    BoardValues["e6"]=12
    BoardValues["e7"]=18
    BoardValues["e8"]=9

    BoardValues["f1"]=-14
    BoardValues["f2"]=-8
    BoardValues["f3"]=-1
    BoardValues["f4"]=-4
    BoardValues["f5"]=-4
    BoardValues["f6"]=6
    BoardValues["f7"]=16
    BoardValues["f8"]=-1

    BoardValues["g1"]=-20
    BoardValues["g2"]=-13
    BoardValues["g3"]=-11
    BoardValues["g4"]=-5
    BoardValues["g5"]=-15
    BoardValues["g6"]=-2
    BoardValues["g7"]=12
    BoardValues["g8"]=-19

    BoardValues["h1"]=-31
    BoardValues["h2"]=-21
    BoardValues["h3"]=-25
    BoardValues["h4"]=-13
    BoardValues["h5"]=-27
    BoardValues["h6"]=-22
    BoardValues["h7"]=-2
    BoardValues["h8"]=-17
    return BoardValues

def rookValueEndGameWhite():
    BoardValues={}   
    BoardValues["a1"]=-9
    BoardValues["a2"]=-12
    BoardValues["a3"]=6
    BoardValues["a4"]=-6
    BoardValues["a5"]=-5
    BoardValues["a6"]=6
    BoardValues["a7"]=4
    BoardValues["a8"]=18

    BoardValues["b1"]=-13
    BoardValues["b2"]=-9
    BoardValues["b3"]=-8
    BoardValues["b4"]=1
    BoardValues["b5"]=8
    BoardValues["b6"]=1
    BoardValues["b7"]=5
    BoardValues["b8"]=18

    BoardValues["c1"]=-10
    BoardValues["c2"]=-1
    BoardValues["c3"]=-2
    BoardValues["c4"]=-9
    BoardValues["c5"]=7
    BoardValues["c6"]=-7
    BoardValues["c7"]=20
    BoardValues["c8"]=19

    BoardValues["d1"]=-9
    BoardValues["d2"]=-2
    BoardValues["d3"]=-6
    BoardValues["d4"]=7
    BoardValues["d5"]=-6
    BoardValues["d6"]=10
    BoardValues["d7"]=-5
    BoardValues["d8"]=13

    BoardValues["e1"]=-9
    BoardValues["e2"]=-2
    BoardValues["e3"]=-6
    BoardValues["e4"]=7
    BoardValues["e5"]=-6
    BoardValues["e6"]=10
    BoardValues["e7"]=-5
    BoardValues["e8"]=13

    BoardValues["f1"]=-10
    BoardValues["f2"]=-1
    BoardValues["f3"]=-2
    BoardValues["f4"]=-9
    BoardValues["f5"]=7
    BoardValues["f6"]=-7
    BoardValues["f7"]=20
    BoardValues["f8"]=19

    BoardValues["g1"]=-13
    BoardValues["g2"]=-9
    BoardValues["g3"]=-8
    BoardValues["g4"]=1
    BoardValues["g5"]=8
    BoardValues["g6"]=1
    BoardValues["g7"]=5
    BoardValues["g8"]=5

    BoardValues["h1"]=-9
    BoardValues["h2"]=-12
    BoardValues["h3"]=6
    BoardValues["h4"]=-6
    BoardValues["h5"]=-5
    BoardValues["h6"]=6
    BoardValues["h7"]=4
    BoardValues["h8"]=18
    return BoardValues


def queenBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"] = 3
    BoardValues["a2"] = -3
    BoardValues["a3"] =  -3
    BoardValues["a4"] = 4
    BoardValues["a5"] = 8
    BoardValues["a6"] = -4
    BoardValues["a7"] = -5
    BoardValues["a8"] = -2

    BoardValues["b1"] = -5
    BoardValues["b2"] = 5
    BoardValues["b3"] = 6
    BoardValues["b4"] = 5
    BoardValues["b5"] = 14
    BoardValues["b6"] = 10
    BoardValues["b7"] = 6
    BoardValues["b8"] = -2

    BoardValues["c1"] = -5
    BoardValues["c2"] = 8
    BoardValues["c3"] = 13
    BoardValues["c4"] = 9
    BoardValues["c5"] = 12
    BoardValues["c6"] = 6
    BoardValues["c7"] = 10
    BoardValues["c8"] = 1

    BoardValues["d1"] = 4
    BoardValues["d2"] = 12
    BoardValues["d3"] = 7
    BoardValues["d4"] = 8
    BoardValues["d5"] = 5
    BoardValues["d6"] = 8
    BoardValues["d7"] = 8
    BoardValues["d8"] = -2

    BoardValues["e1"] = 4
    BoardValues["e2"] = 12
    BoardValues["e3"] = 7
    BoardValues["e4"] = 8
    BoardValues["e5"] = 5
    BoardValues["e6"] = 8
    BoardValues["e7"] = 8
    BoardValues["e8"] = -2

    BoardValues["f1"] = -5
    BoardValues["f2"] = 8
    BoardValues["f3"] = 13
    BoardValues["f4"] = 9
    BoardValues["f5"] = 12
    BoardValues["f6"] = 6
    BoardValues["f7"] = 10
    BoardValues["f8"] = 1

    BoardValues["g1"] = -5
    BoardValues["g2"] = 5
    BoardValues["g3"] = 6
    BoardValues["g4"] = 5
    BoardValues["g5"] = 14
    BoardValues["g6"] = 10
    BoardValues["g7"] = 6
    BoardValues["g8"] = -2

    BoardValues["h1"] = 3
    BoardValues["h2"] = -3
    BoardValues["h3"] = -3
    BoardValues["h4"] = 4
    BoardValues["h5"] = -4
    BoardValues["h6"] = -4
    BoardValues["h7"] = -5
    BoardValues["h8"] = -2
    return BoardValues


def queenValueEndGameWhite():
    BoardValues={}   
    BoardValues["a1"] = -69
    BoardValues["a2"] = -55
    BoardValues["a3"] = -39
    BoardValues["a4"] = -23
    BoardValues["a5"] = -29
    BoardValues["a6"] = -38
    BoardValues["a7"] = -50
    BoardValues["a8"] = -75

    BoardValues["b1"] = -57
    BoardValues["b2"] = -31
    BoardValues["b3"] = -18
    BoardValues["b4"] = -3
    BoardValues["b5"] = -6
    BoardValues["b6"] = -18
    BoardValues["b7"] = -27
    BoardValues["b8"] = -52

    BoardValues["c1"] = -47
    BoardValues["c2"] = -22
    BoardValues["c3"] = -9
    BoardValues["c4"] = 13
    BoardValues["c5"] = 9
    BoardValues["c6"] = -12
    BoardValues["c7"] = -24
    BoardValues["c8"] = -43

    BoardValues["d1"] = -26
    BoardValues["d2"] = -4
    BoardValues["d3"] = 3
    BoardValues["d4"] = 24
    BoardValues["d5"] = 21
    BoardValues["d6"] = 1
    BoardValues["d7"] = -8
    BoardValues["d8"] = -36

    BoardValues["e1"] = -26
    BoardValues["e2"] = -4
    BoardValues["e3"] = 3
    BoardValues["e4"] = 24
    BoardValues["e5"] = 21
    BoardValues["e6"] = 1
    BoardValues["e7"] = -8
    BoardValues["e8"] = -36

    BoardValues["f1"] = -47
    BoardValues["f2"] = -22
    BoardValues["f3"] = -9
    BoardValues["f4"] = 13
    BoardValues["f5"] = 9
    BoardValues["f6"] = -12
    BoardValues["f7"] = -24
    BoardValues["f8"] = -43

    BoardValues["g1"] = -57
    BoardValues["g2"] = -31
    BoardValues["g3"] = -18
    BoardValues["g4"] = -3
    BoardValues["g5"] = -6
    BoardValues["g6"] = -18
    BoardValues["g7"] = -27
    BoardValues["g8"] = -52

    BoardValues["h1"] = -69
    BoardValues["h2"] = -55
    BoardValues["h3"] = -39
    BoardValues["h4"] = -23
    BoardValues["h5"] = -29
    BoardValues["h6"] = -38
    BoardValues["h7"] = -50
    BoardValues["h8"] = -75
    return BoardValues


def kingBoardValuesWhiteEarly():
    BoardValues={}   
    BoardValues["a1"]=271
    BoardValues["a2"]=278
    BoardValues["a3"]=195
    BoardValues["a4"]=164
    BoardValues["a5"]=154
    BoardValues["a6"]=123
    BoardValues["a7"]=88
    BoardValues["a8"]=59

    BoardValues["b1"] = 327
    BoardValues["b2"] = 303
    BoardValues["b3"] = 258
    BoardValues["b4"] = 190
    BoardValues["b5"] = 179
    BoardValues["b6"] = 145
    BoardValues["b7"] = 120
    BoardValues["b8"] = 89

    BoardValues["c1"] = 271
    BoardValues["c2"] = 234
    BoardValues["c3"] = 169
    BoardValues["c4"] = 138
    BoardValues["c5"] = 105
    BoardValues["c6"] = 81
    BoardValues["c7"] = 65
    BoardValues["c8"] = 45

    BoardValues["d1"] = 198
    BoardValues["d2"] = 179
    BoardValues["d3"] = 120
    BoardValues["d4"] = 98
    BoardValues["d5"] = 70
    BoardValues["d6"] = 31
    BoardValues["d7"] = 33
    BoardValues["d8"] = -1

    BoardValues["e1"] = 198
    BoardValues["e2"] = 179
    BoardValues["e3"] = 120
    BoardValues["e4"] = 98
    BoardValues["e5"] = 70
    BoardValues["e6"] = 31
    BoardValues["e7"] = 33
    BoardValues["e8"] = -1

    BoardValues["f1"] = 271
    BoardValues["f2"] = 234
    BoardValues["f3"] = 169
    BoardValues["f4"] = 138
    BoardValues["f5"] = 105
    BoardValues["f6"] = 81
    BoardValues["f7"] = 65
    BoardValues["f8"] = 45

    BoardValues["g1"] = 327
    BoardValues["g2"] = 303
    BoardValues["g3"] = 258
    BoardValues["g4"] = 190
    BoardValues["g5"] = 179
    BoardValues["g6"] = 145
    BoardValues["g7"] = 120
    BoardValues["g8"] = 89

    BoardValues["h1"] = 271 
    BoardValues["h2"] = 278
    BoardValues["h3"] = 195
    BoardValues["h4"] = 164
    BoardValues["h5"] = 154
    BoardValues["h6"] = 123
    BoardValues["h7"] = 88
    BoardValues["h8"] = 59
    return BoardValues

def kingBoardValuesWhiteLate():
    BoardValues={}   
    BoardValues["a1"] = 1
    BoardValues["a2"] = 53
    BoardValues["a3"] = 88
    BoardValues["a4"] = 103
    BoardValues["a5"] = 96
    BoardValues["a6"] = 92
    BoardValues["a7"] = 47
    BoardValues["a8"] = 11

    BoardValues["b1"] = 45
    BoardValues["b2"] = 100
    BoardValues["b3"] = 130
    BoardValues["b4"] = 156
    BoardValues["b5"] = 166
    BoardValues["b6"] = 172
    BoardValues["b7"] = 121
    BoardValues["b8"] = 59

    BoardValues["c1"] = 85
    BoardValues["c2"] = 133
    BoardValues["c3"] = 169
    BoardValues["c4"] = 172
    BoardValues["c5"] = 199
    BoardValues["c6"] = 184
    BoardValues["c7"] = 116
    BoardValues["c8"] = 73

    BoardValues["d1"] = 76
    BoardValues["d2"] =  135
    BoardValues["d3"] = 175
    BoardValues["d4"] = 172
    BoardValues["d5"] = 199
    BoardValues["d6"] = 191
    BoardValues["d7"] = 131
    BoardValues["d8"] = 78

    BoardValues["e1"] = 76
    BoardValues["e2"] = 135
    BoardValues["e3"] = 175
    BoardValues["e4"] = 172
    BoardValues["e5"] = 199
    BoardValues["e6"] = 191
    BoardValues["e7"] = 131
    BoardValues["e8"] = 78

    BoardValues["f1"] = 85
    BoardValues["f2"] = 133
    BoardValues["f3"] = 169
    BoardValues["f4"] = 172
    BoardValues["f5"] = 199
    BoardValues["f6"] = 184
    BoardValues["f7"] = 116
    BoardValues["f8"] = 73

    BoardValues["g1"] = 45
    BoardValues["g2"] = 100
    BoardValues["g3"] = 130
    BoardValues["g4"] = 156
    BoardValues["g5"] = 166
    BoardValues["g6"] = 172
    BoardValues["g7"] = 121
    BoardValues["g8"] = 59

    BoardValues["h1"] = 1
    BoardValues["h2"] = 53
    BoardValues["h3"] = 88
    BoardValues["h4"] = 103
    BoardValues["h5"] = 96
    BoardValues["h6"] = 92
    BoardValues["h7"] = 47
    BoardValues["h8"] = 11
    return BoardValues

def pawnBoardValuesWhite():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=3
    BoardValues["a3"]=-9
    BoardValues["a4"]=-4
    BoardValues["a5"]=13
    BoardValues["a6"]=5
    BoardValues["a7"]=-7
    BoardValues["a8"]=0

    BoardValues["b1"]=0
    BoardValues["b2"]=3
    BoardValues["b3"]=-15
    BoardValues["b4"]=-23
    BoardValues["b5"]=-2
    BoardValues["b6"]=-12
    BoardValues["b7"]=7
    BoardValues["b8"]=0

    BoardValues["c1"]=0
    BoardValues["c2"]=10
    BoardValues["c3"]=11
    BoardValues["c4"]=6
    BoardValues["c5"]=-13
    BoardValues["c6"]=-7
    BoardValues["c7"]=-3
    BoardValues["c8"]=0

    BoardValues["d1"]=0
    BoardValues["d2"]=19
    BoardValues["d3"]=15
    BoardValues["d4"]=20
    BoardValues["d5"]=1
    BoardValues["d6"]=22
    BoardValues["d7"]=-13
    BoardValues["d8"]=0

    BoardValues["e1"]=0
    BoardValues["e2"]=16
    BoardValues["e3"]=32
    BoardValues["e4"]=40
    BoardValues["e5"]=11
    BoardValues["e6"]=-8
    BoardValues["e7"]=5
    BoardValues["e8"]=0

    BoardValues["f1"]=0
    BoardValues["f2"]=19
    BoardValues["f3"]=22
    BoardValues["f4"]=17
    BoardValues["f5"]=-2
    BoardValues["f6"]=-5
    BoardValues["f7"]=-16
    BoardValues["f8"]=0

    BoardValues["g1"]=0
    BoardValues["g2"]=7
    BoardValues["g3"]=5
    BoardValues["g4"]=4
    BoardValues["g5"]=-13
    BoardValues["g6"]=-15
    BoardValues["g7"]=10
    BoardValues["g8"]=0

    BoardValues["h1"]=0
    BoardValues["h2"]=-5
    BoardValues["h3"]=-22
    BoardValues["h4"]=-8
    BoardValues["h5"]=5
    BoardValues["h6"]=-8
    BoardValues["h7"]=-5
    BoardValues["h8"]=0
    return BoardValues

def pawnValueEndGameWhite():
    BoardValues={}   
    BoardValues["a1"]=0
    BoardValues["a2"]=-10
    BoardValues["a3"]=-10
    BoardValues["a4"]=6
    BoardValues["a5"]=10
    BoardValues["a6"]=28
    BoardValues["a7"]=1
    BoardValues["a8"]=0

    BoardValues["b1"]=0
    BoardValues["b2"]=-6
    BoardValues["b3"]=-10
    BoardValues["b4"]=-2
    BoardValues["b5"]=5
    BoardValues["b6"]=20
    BoardValues["b7"]=-11
    BoardValues["b8"]=0

    BoardValues["c1"]=0
    BoardValues["c2"]=10
    BoardValues["c3"]=-10
    BoardValues["c4"]=-8
    BoardValues["c5"]=4
    BoardValues["c6"]=21
    BoardValues["c7"]=12
    BoardValues["c8"]=0

    BoardValues["d1"]=0
    BoardValues["d2"]=0
    BoardValues["d3"]=4
    BoardValues["d4"]=-4
    BoardValues["d5"]=-5
    BoardValues["d6"]=28
    BoardValues["d7"]=21
    BoardValues["d8"]=0

    BoardValues["e1"]=0
    BoardValues["e2"]=14
    BoardValues["e3"]=4
    BoardValues["e4"]=-13
    BoardValues["e5"]=-5
    BoardValues["e6"]=30
    BoardValues["e7"]=25
    BoardValues["e8"]=0

    BoardValues["f1"]=0
    BoardValues["f2"]=7
    BoardValues["f3"]=3
    BoardValues["f4"]=-12
    BoardValues["f5"]=-5
    BoardValues["f6"]=7
    BoardValues["f7"]=19
    BoardValues["f8"]=0

    BoardValues["g1"]=0
    BoardValues["g2"]=-5
    BoardValues["g3"]=-6
    BoardValues["g4"]=-10
    BoardValues["g5"]=14
    BoardValues["g6"]=6
    BoardValues["g7"]=4
    BoardValues["g8"]=0

    BoardValues["h1"]=0
    BoardValues["h2"]=-19
    BoardValues["h3"]=-4
    BoardValues["h4"]=-9
    BoardValues["h5"]=9
    BoardValues["h6"]=13
    BoardValues["h7"]=7
    BoardValues["h8"]=0
    return BoardValues





#Black Methods
def bishopBoardValuesBlack():
    BoardValues={}   
    BoardValues["a8"] = -53
    BoardValues["a7"] = -15
    BoardValues["a6"] = -7
    BoardValues["a5"] = -5
    BoardValues["a4"] = -12
    BoardValues["a3"] = -16
    BoardValues["a2"] = -17
    BoardValues["a1"] = -48

    BoardValues["b8"] = -5
    BoardValues["b7"] = 8
    BoardValues["b6"] = 21
    BoardValues["b5"] = 11
    BoardValues["b4"] = 29
    BoardValues["b3"] = 6
    BoardValues["b2"] = -14
    BoardValues["b1"] = 1

    BoardValues["c8"] = -8
    BoardValues["c7"] = 19
    BoardValues["c6"] = -5
    BoardValues["c5"] = 25
    BoardValues["c4"] = 22
    BoardValues["c3"] = 1
    BoardValues["c2"] = 5
    BoardValues["c1"] = -14

    BoardValues["d8"] = -23
    BoardValues["d7"] = 4
    BoardValues["d6"] = 17
    BoardValues["d5"] = 39
    BoardValues["d4"] = 31
    BoardValues["d3"] = 11
    BoardValues["d2"] = 6
    BoardValues["d1"] = -23

    BoardValues["e8"]=-23
    BoardValues["e7"]=4
    BoardValues["e6"]=17
    BoardValues["e5"]=39
    BoardValues["e4"]=31
    BoardValues["e3"]=11
    BoardValues["e2"]=4
    BoardValues["e1"]=-23

    BoardValues["f8"]=-8
    BoardValues["f7"]=19
    BoardValues["f6"]=-5
    BoardValues["f5"]=25
    BoardValues["f4"]=22
    BoardValues["f3"]=1
    BoardValues["f2"]=5
    BoardValues["f1"]=-14

    BoardValues["g8"]=-5
    BoardValues["g7"]=8
    BoardValues["g6"]=21
    BoardValues["g5"]=11
    BoardValues["g4"]=29
    BoardValues["g3"]=6
    BoardValues["g2"]=-14
    BoardValues["g1"]=1

    BoardValues["h8"]=-53
    BoardValues["h7"]=-15
    BoardValues["h6"]=-7
    BoardValues["h5"]=-5
    BoardValues["h4"]=-12
    BoardValues["h3"]=-16
    BoardValues["h2"]=-17
    BoardValues["h1"]=-48
    return BoardValues

def bishopValueEndGameBlack():
    BoardValues={}   
    BoardValues["a8"] = -57
    BoardValues["a7"] = -37
    BoardValues["a6"] = -16
    BoardValues["a5"] = -20
    BoardValues["a4"] = -17
    BoardValues["a3"] = -30
    BoardValues["a2"] = -31
    BoardValues["a1"] = -46

    BoardValues["b8"] = -30
    BoardValues["b7"] = -13
    BoardValues["b6"] = -1
    BoardValues["b5"] = -6
    BoardValues["b4"] = -1
    BoardValues["b3"] = 6
    BoardValues["b2"] = -20
    BoardValues["b1"] = -42

    BoardValues["c8"] = -37
    BoardValues["c7"] = -17
    BoardValues["c6"] = -2
    BoardValues["c5"] = 37
    BoardValues["c4"] = -14
    BoardValues["c3"] = 4
    BoardValues["c2"] = -1
    BoardValues["c1"] = -37

    BoardValues["d8"] = -12
    BoardValues["d7"] = 1
    BoardValues["d6"] = 10
    BoardValues["d5"] = 17
    BoardValues["d4"] = 15
    BoardValues["d3"] = 6
    BoardValues["d2"] = 1
    BoardValues["d1"] = -24

    BoardValues["e8"]=-12
    BoardValues["e7"]=1
    BoardValues["e6"]=10
    BoardValues["e5"]=17
    BoardValues["e4"]=15
    BoardValues["e3"]=6
    BoardValues["e2"]=1
    BoardValues["e1"]=-24

    BoardValues["f8"]=-37
    BoardValues["f7"]=-17
    BoardValues["f6"]=-2
    BoardValues["f5"]=0
    BoardValues["f4"]=-14
    BoardValues["f3"]=4
    BoardValues["f2"]=-1
    BoardValues["f1"]=-37

    BoardValues["g8"]=-30
    BoardValues["g7"]=-13
    BoardValues["g6"]=-1
    BoardValues["g4"]=-6
    BoardValues["g3"]=-1
    BoardValues["g2"]=6
    BoardValues["g2"]=-20
    BoardValues["g1"]=-42

    BoardValues["h8"]=-57
    BoardValues["h7"]=-37
    BoardValues["h6"]=-16
    BoardValues["h5"]=-20
    BoardValues["h4"]=-17
    BoardValues["h3"]=-30
    BoardValues["h2"]=-31
    BoardValues["h1"]=-46
    return BoardValues



def knightBoardValuesBlack():
    BoardValues={}   
    BoardValues["a8"]=-175
    BoardValues["a7"]=-77
    BoardValues["a6"]=-61
    BoardValues["a5"]=-35
    BoardValues["a4"]=-34
    BoardValues["a3"]=-9
    BoardValues["a2"]=-67
    BoardValues["a1"]=-201

    BoardValues["b8"]=-92
    BoardValues["b7"]=-42
    BoardValues["b6"]=-17
    BoardValues["b5"]=8
    BoardValues["b4"]=13
    BoardValues["b3"]=22
    BoardValues["b2"]=-27
    BoardValues["b1"]=-83

    BoardValues["c8"]=-74
    BoardValues["c7"]=-27
    BoardValues["c6"]=6
    BoardValues["c5"]=40
    BoardValues["c4"]=44
    BoardValues["c3"]=58
    BoardValues["c2"]=4
    BoardValues["c1"]=-56

    BoardValues["d8"]=-73
    BoardValues["d7"]=-15
    BoardValues["d6"]=12
    BoardValues["d5"]=49
    BoardValues["d4"]=51
    BoardValues["d3"]=53
    BoardValues["d2"]=37
    BoardValues["d1"]=-26

    BoardValues["e8"]=-73
    BoardValues["e7"]=-15
    BoardValues["e6"]=12
    BoardValues["e5"]=49
    BoardValues["e4"]=51
    BoardValues["e3"]=53
    BoardValues["e2"]=37
    BoardValues["e1"]=-26

    BoardValues["f8"]=-74
    BoardValues["f7"]=-27
    BoardValues["f6"]=6
    BoardValues["f5"]=40
    BoardValues["f4"]=44
    BoardValues["f3"]=58
    BoardValues["f2"]=4
    BoardValues["f1"]=-56

    BoardValues["g8"]=-92
    BoardValues["g7"]=-41
    BoardValues["g6"]=-17
    BoardValues["g5"]=8
    BoardValues["g4"]=13
    BoardValues["g3"]=22
    BoardValues["g2"]=-27
    BoardValues["g1"]=-83

    BoardValues["h8"]=-175
    BoardValues["h7"]=-77
    BoardValues["h6"]=-61
    BoardValues["h5"]=-35
    BoardValues["h4"]=-34
    BoardValues["h3"]=-9
    BoardValues["h2"]=-67
    BoardValues["h1"]=-201
    return BoardValues

def knightValueEndGameBlack():
    BoardValues={}   
    BoardValues["a8"]=-96
    BoardValues["a7"]=-67
    BoardValues["a6"]=-40
    BoardValues["a5"]=-35
    BoardValues["a4"]=-45
    BoardValues["a3"]=-51
    BoardValues["a2"]=-67
    BoardValues["a1"]=-100

    BoardValues["b8"]=-65
    BoardValues["b7"]=-54
    BoardValues["b6"]=-27
    BoardValues["b5"]=-2
    BoardValues["b4"]=-16
    BoardValues["b3"]=-44
    BoardValues["b2"]=-50
    BoardValues["b1"]=-88

    BoardValues["c8"]=-49
    BoardValues["c7"]=-18
    BoardValues["c6"]=-8
    BoardValues["c5"]=13
    BoardValues["c4"]=9
    BoardValues["c3"]=-16
    BoardValues["c2"]=-51
    BoardValues["c1"]=-56

    BoardValues["d8"]=-21
    BoardValues["d7"]=8
    BoardValues["d6"]=29
    BoardValues["d5"]=28
    BoardValues["d4"]=39
    BoardValues["d3"]=17
    BoardValues["d2"]=12
    BoardValues["d1"]=-17

    BoardValues["e8"]=-21
    BoardValues["e7"]=8
    BoardValues["e6"]=29
    BoardValues["e5"]=28
    BoardValues["e4"]=39
    BoardValues["e3"]=17
    BoardValues["e2"]=12
    BoardValues["e1"]=-17

    BoardValues["f8"]=-49
    BoardValues["f7"]=-18
    BoardValues["f6"]=-8
    BoardValues["f5"]=13
    BoardValues["f4"]=9
    BoardValues["f3"]=-16
    BoardValues["f2"]=-51
    BoardValues["f1"]=-56

    BoardValues["g8"]=-65
    BoardValues["g7"]=-54
    BoardValues["g6"]=-27
    BoardValues["g5"]=-2
    BoardValues["g4"]=-16
    BoardValues["g3"]=-44
    BoardValues["g2"]=-50
    BoardValues["g1"]=-88

    BoardValues["h8"]=-96
    BoardValues["h7"]=-67
    BoardValues["h6"]=-40
    BoardValues["h5"]=-35
    BoardValues["h4"]=-45
    BoardValues["h3"]=-51
    BoardValues["h2"]=-69
    BoardValues["h1"]=-100

    return BoardValues




def rookBoardValuesBlack():
    BoardValues={}   
    BoardValues["a8"]=-31
    BoardValues["a7"]=-21
    BoardValues["a6"]=-25
    BoardValues["a5"]=-13
    BoardValues["a4"]=-27
    BoardValues["a3"]=-22
    BoardValues["a2"]=-2
    BoardValues["a1"]=-17

    BoardValues["b8"]=-20
    BoardValues["b7"]=-13
    BoardValues["b6"]=-11
    BoardValues["b5"]=-5
    BoardValues["b4"]=-15
    BoardValues["b3"]=-2
    BoardValues["b2"]=12
    BoardValues["b1"]=-19

    BoardValues["c8"]=-14
    BoardValues["c7"]=-8
    BoardValues["c6"]=-1
    BoardValues["c5"]=-4
    BoardValues["c4"]=-4
    BoardValues["c3"]=6
    BoardValues["c2"]=16
    BoardValues["c1"]=-1

    BoardValues["d8"]=-5
    BoardValues["d7"]=6
    BoardValues["d6"]=3
    BoardValues["d5"]=-6
    BoardValues["d4"]=3
    BoardValues["d3"]=12
    BoardValues["d2"]=18
    BoardValues["d1"]=8

    BoardValues["e8"]=-5
    BoardValues["e7"]=6
    BoardValues["e6"]=3
    BoardValues["e5"]=-6
    BoardValues["e4"]=3
    BoardValues["e3"]=12
    BoardValues["e2"]=18
    BoardValues["e1"]=9

    BoardValues["f8"]=-14
    BoardValues["f7"]=-8
    BoardValues["f6"]=-1
    BoardValues["f5"]=-4
    BoardValues["f4"]=-4
    BoardValues["f3"]=6
    BoardValues["f2"]=16
    BoardValues["f1"]=-1

    BoardValues["g8"]=-20
    BoardValues["g7"]=-13
    BoardValues["g6"]=-11
    BoardValues["g5"]=-5
    BoardValues["g4"]=-15
    BoardValues["g3"]=-2
    BoardValues["g2"]=12
    BoardValues["g1"]=-19

    BoardValues["h8"]=-31
    BoardValues["h7"]=-21
    BoardValues["h6"]=-25
    BoardValues["h5"]=-13
    BoardValues["h4"]=-27
    BoardValues["h3"]=-22
    BoardValues["h2"]=-2
    BoardValues["h1"]=-17
    return BoardValues


def rookValueEndGameBlack():
    BoardValues={}   
    BoardValues["a8"]=-9
    BoardValues["a7"]=-12
    BoardValues["a6"]=6
    BoardValues["a5"]=-6
    BoardValues["a4"]=-5
    BoardValues["a3"]=6
    BoardValues["a2"]=4
    BoardValues["a1"]=18

    BoardValues["b8"]=-13
    BoardValues["b7"]=-9
    BoardValues["b6"]=-8
    BoardValues["b5"]=1
    BoardValues["b4"]=8
    BoardValues["b3"]=1
    BoardValues["b2"]=5
    BoardValues["b1"]=18

    BoardValues["c8"]=-10
    BoardValues["c7"]=-1
    BoardValues["c6"]=-2
    BoardValues["c5"]=-9
    BoardValues["c4"]=7
    BoardValues["c3"]=-7
    BoardValues["c2"]=20
    BoardValues["c1"]=19

    BoardValues["d8"]=-9
    BoardValues["d7"]=-2
    BoardValues["d6"]=-6
    BoardValues["d5"]=7
    BoardValues["d4"]=-6
    BoardValues["d3"]=10
    BoardValues["d2"]=-5
    BoardValues["d1"]=13

    BoardValues["e8"]=-9
    BoardValues["e7"]=-2
    BoardValues["e6"]=-6
    BoardValues["e5"]=7
    BoardValues["e4"]=-6
    BoardValues["e3"]=10
    BoardValues["e2"]=-5
    BoardValues["e1"]=13

    BoardValues["f8"]=-10
    BoardValues["f7"]=-1
    BoardValues["f6"]=-2
    BoardValues["f5"]=-9
    BoardValues["f4"]=7
    BoardValues["f3"]=-7
    BoardValues["f2"]=20
    BoardValues["f1"]=19

    BoardValues["g8"]=-13
    BoardValues["g7"]=-9
    BoardValues["g6"]=-8
    BoardValues["g5"]=1
    BoardValues["g4"]=8
    BoardValues["g3"]=1
    BoardValues["g2"]=5
    BoardValues["g1"]=5

    BoardValues["h8"]=-9
    BoardValues["h7"]=-12
    BoardValues["h6"]=6
    BoardValues["h5"]=-6
    BoardValues["h4"]=-5
    BoardValues["h3"]=6
    BoardValues["h2"]=4
    BoardValues["h1"]=18
    return BoardValues




def queenBoardValuesBlack():
    BoardValues={}   
    BoardValues["a8"] = 3
    BoardValues["a7"] = -3
    BoardValues["a6"] =  -3
    BoardValues["a5"] = 4
    BoardValues["a4"] = 8
    BoardValues["a3"] = -4
    BoardValues["a2"] = -5
    BoardValues["a1"] = -2

    BoardValues["b8"] = -5
    BoardValues["b7"] = 5
    BoardValues["b6"] = 6
    BoardValues["b5"] = 5
    BoardValues["b4"] = 14
    BoardValues["b3"] = 10
    BoardValues["b2"] = 6
    BoardValues["b1"] = -2

    BoardValues["c8"] = -5
    BoardValues["c7"] = 8
    BoardValues["c6"] = 13
    BoardValues["c5"] = 9
    BoardValues["c4"] = 12
    BoardValues["c3"] = 6
    BoardValues["c2"] = 10
    BoardValues["c1"] = 1

    BoardValues["d8"] = 4
    BoardValues["d7"] = 12
    BoardValues["d6"] = 7
    BoardValues["d5"] = 8
    BoardValues["d4"] = 5
    BoardValues["d3"] = 8
    BoardValues["d2"] = 8
    BoardValues["d1"] = -2

    BoardValues["e8"] = 4
    BoardValues["e7"] = 12
    BoardValues["e6"] = 7
    BoardValues["e5"] = 8
    BoardValues["e4"] = 5
    BoardValues["e3"] = 8
    BoardValues["e2"] = 8
    BoardValues["e1"] = -2

    BoardValues["f8"] = -5
    BoardValues["f7"] = 8
    BoardValues["f6"] = 13
    BoardValues["f5"] = 9
    BoardValues["f4"] = 12
    BoardValues["f3"] = 6
    BoardValues["f2"] = 10
    BoardValues["f1"] = 1

    BoardValues["g8"] = -5
    BoardValues["g7"] = 5
    BoardValues["g6"] = 6
    BoardValues["g5"] = 5
    BoardValues["g4"] = 14
    BoardValues["g3"] = 10
    BoardValues["g2"] = 6
    BoardValues["g1"] = -2

    BoardValues["h8"] = 3
    BoardValues["h7"] = -3
    BoardValues["h6"] = -3
    BoardValues["h5"] = 4
    BoardValues["h4"] = -4
    BoardValues["h3"] = -4
    BoardValues["h2"] = -5
    BoardValues["h1"] = -2
    return BoardValues

def queenValueEndGameBlack():
    BoardValues={}   
    BoardValues["a8"] = -69
    BoardValues["a7"] = -55
    BoardValues["a6"] = -39
    BoardValues["a5"] = -23
    BoardValues["a4"] = -29
    BoardValues["a3"] = -38
    BoardValues["a2"] = -50
    BoardValues["a1"] = -75

    BoardValues["b8"] = -57
    BoardValues["b7"] = -31
    BoardValues["b6"] = -18
    BoardValues["b5"] = -3
    BoardValues["b4"] = -6
    BoardValues["b3"] = -18
    BoardValues["b2"] = -27
    BoardValues["b1"] = -52

    BoardValues["c8"] = -47
    BoardValues["c7"] = -22
    BoardValues["c6"] = -9
    BoardValues["c5"] = 13
    BoardValues["c4"] = 9
    BoardValues["c3"] = -12
    BoardValues["c2"] = -24
    BoardValues["c1"] = -43

    BoardValues["d8"] = -26
    BoardValues["d7"] = -4
    BoardValues["d6"] = 3
    BoardValues["d5"] = 24
    BoardValues["d4"] = 21
    BoardValues["d3"] = 1
    BoardValues["d2"] = -8
    BoardValues["d1"] = -36

    BoardValues["e8"] = -26
    BoardValues["e7"] = -4
    BoardValues["e6"] = 3
    BoardValues["e5"] = 24
    BoardValues["e4"] = 21
    BoardValues["e3"] = 1
    BoardValues["e2"] = -8
    BoardValues["e1"] = -36

    BoardValues["f8"] = -47
    BoardValues["f7"] = -22
    BoardValues["f6"] = -9
    BoardValues["f5"] = 13
    BoardValues["f4"] = 9
    BoardValues["f3"] = -12
    BoardValues["f2"] = -24
    BoardValues["f1"] = -43

    BoardValues["g8"] = -57
    BoardValues["g7"] = -31
    BoardValues["g6"] = -18
    BoardValues["g5"] = -3
    BoardValues["g4"] = -6
    BoardValues["g3"] = -18
    BoardValues["g2"] = -27
    BoardValues["g1"] = -52

    BoardValues["h8"] = -69
    BoardValues["h7"] = -55
    BoardValues["h6"] = -39
    BoardValues["h5"] = -23
    BoardValues["h4"] = -29
    BoardValues["h3"] = -38
    BoardValues["h2"] = -50
    BoardValues["h1"] = -75
    return BoardValues



def kingBoardValuesBlackEarly():
    BoardValues={}   
    BoardValues["a8"]=271
    BoardValues["a7"]=278
    BoardValues["a6"]=195
    BoardValues["a5"]=164
    BoardValues["a4"]=154
    BoardValues["a3"]=123
    BoardValues["a2"]=88
    BoardValues["a1"]=59

    BoardValues["b8"] = 327
    BoardValues["b7"] = 303
    BoardValues["b6"] = 258
    BoardValues["b5"] = 190
    BoardValues["b4"] = 179
    BoardValues["b3"] = 145
    BoardValues["b2"] = 120
    BoardValues["b1"] = 89

    BoardValues["c8"] = 271
    BoardValues["c7"] = 234
    BoardValues["c6"] = 169
    BoardValues["c5"] = 138
    BoardValues["c4"] = 105
    BoardValues["c3"] = 81
    BoardValues["c2"] = 65
    BoardValues["c1"] = 45

    BoardValues["d8"] = 198
    BoardValues["d7"] = 179
    BoardValues["d6"] = 120
    BoardValues["d5"] = 98
    BoardValues["d4"] = 70
    BoardValues["d3"] = 31
    BoardValues["d2"] = 33
    BoardValues["d1"] = -1

    BoardValues["e8"] = 198
    BoardValues["e7"] = 179
    BoardValues["e6"] = 120
    BoardValues["e5"] = 98
    BoardValues["e4"] = 70
    BoardValues["e3"] = 31
    BoardValues["e2"] = 33
    BoardValues["e1"] = -1

    BoardValues["f8"] = 271
    BoardValues["f7"] = 234
    BoardValues["f6"] = 169
    BoardValues["f5"] = 138
    BoardValues["f4"] = 105
    BoardValues["f3"] = 81
    BoardValues["f2"] = 65
    BoardValues["f1"] = 45

    BoardValues["g8"] = 327
    BoardValues["g7"] = 303
    BoardValues["g6"] = 258
    BoardValues["g5"] = 190
    BoardValues["g4"] = 179
    BoardValues["g3"] = 145
    BoardValues["g2"] = 120
    BoardValues["g1"] = 89

    BoardValues["h8"] = 271 
    BoardValues["h7"] = 278
    BoardValues["h6"] = 195
    BoardValues["h5"] = 164
    BoardValues["h4"] = 154
    BoardValues["h3"] = 123
    BoardValues["h2"] = 88
    BoardValues["h1"] = 59
    return BoardValues

def kingBoardValuesBlackLate():
    BoardValues={}   
    BoardValues["a8"] = 1
    BoardValues["a7"] = 53
    BoardValues["a6"] = 88
    BoardValues["a5"] = 103
    BoardValues["a4"] = 96
    BoardValues["a3"] = 92
    BoardValues["a2"] = 47
    BoardValues["a1"] = 11

    BoardValues["b8"] = 45
    BoardValues["b7"] = 100
    BoardValues["b6"] = 130
    BoardValues["b5"] = 156
    BoardValues["b4"] = 166
    BoardValues["b3"] = 172
    BoardValues["b2"] = 121
    BoardValues["b1"] = 59

    BoardValues["c8"] = 85
    BoardValues["c7"] = 133
    BoardValues["c6"] = 169
    BoardValues["c5"] = 172
    BoardValues["c4"] = 199
    BoardValues["c3"] = 184
    BoardValues["c2"] = 116
    BoardValues["c1"] = 73

    BoardValues["d8"] = 76
    BoardValues["d7"] =  135
    BoardValues["d6"] = 175
    BoardValues["d5"] = 172
    BoardValues["d4"] = 199
    BoardValues["d3"] = 191
    BoardValues["d2"] = 131
    BoardValues["d1"] = 78

    BoardValues["e8"] = 76
    BoardValues["e7"] = 135
    BoardValues["e6"] = 175
    BoardValues["e5"] = 172
    BoardValues["e4"] = 199
    BoardValues["e3"] = 191
    BoardValues["e2"] = 131
    BoardValues["e1"] = 78

    BoardValues["f8"] = 85
    BoardValues["f7"] = 133
    BoardValues["f6"] = 169
    BoardValues["f5"] = 172
    BoardValues["f4"] = 199
    BoardValues["f3"] = 184
    BoardValues["f2"] = 116
    BoardValues["f1"] = 73

    BoardValues["g8"] = 45
    BoardValues["g7"] = 100
    BoardValues["g6"] = 130
    BoardValues["g5"] = 156
    BoardValues["g4"] = 166
    BoardValues["g3"] = 172
    BoardValues["g2"] = 121
    BoardValues["g1"] = 59

    BoardValues["h8"] = 1
    BoardValues["h7"] = 53
    BoardValues["h6"] = 88
    BoardValues["h5"] = 103
    BoardValues["h4"] = 96
    BoardValues["h3"] = 92
    BoardValues["h2"] = 47
    BoardValues["h1"] = 11
    return BoardValues




def pawnBoardValuesBlack():
    BoardValues={} 
    BoardValues["a8"]=0
    BoardValues["a7"]=3
    BoardValues["a6"]=-9
    BoardValues["a5"]=-4
    BoardValues["a4"]=13
    BoardValues["a3"]=5
    BoardValues["a2"]=-7
    BoardValues["a1"]=0

    BoardValues["b8"]=0
    BoardValues["b7"]=3
    BoardValues["b6"]=-15
    BoardValues["b5"]=-23
    BoardValues["b4"]=-2
    BoardValues["b3"]=-12
    BoardValues["b2"]=7
    BoardValues["b1"]=0

    BoardValues["c8"]=0
    BoardValues["c7"]=10
    BoardValues["c6"]=11
    BoardValues["c5"]=6
    BoardValues["c4"]=-13
    BoardValues["c3"]=-7
    BoardValues["c2"]=-3
    BoardValues["c1"]=0

    BoardValues["d8"]=0
    BoardValues["d7"]=19
    BoardValues["d6"]=15
    BoardValues["d5"]=20
    BoardValues["d4"]=1
    BoardValues["d3"]=22
    BoardValues["d2"]=-13
    BoardValues["d1"]=0

    BoardValues["e8"]=0
    BoardValues["e7"]=16
    BoardValues["e6"]=32
    BoardValues["e5"]=40
    BoardValues["e4"]=11
    BoardValues["e3"]=-8
    BoardValues["e2"]=5
    BoardValues["e1"]=0

    BoardValues["f8"]=0
    BoardValues["f7"]=19
    BoardValues["f6"]=22
    BoardValues["f5"]=17
    BoardValues["f4"]=-2
    BoardValues["f3"]=-5
    BoardValues["f2"]=-16
    BoardValues["f1"]=0

    BoardValues["g8"]=0
    BoardValues["g7"]=7
    BoardValues["g6"]=5
    BoardValues["g5"]=4
    BoardValues["g4"]=-13
    BoardValues["g3"]=-15
    BoardValues["g2"]=10
    BoardValues["g1"]=0

    BoardValues["h8"]=0
    BoardValues["h7"]=-5
    BoardValues["h6"]=-22
    BoardValues["h5"]=-8
    BoardValues["h4"]=5
    BoardValues["h3"]=-8
    BoardValues["h2"]=-5
    BoardValues["h1"]=0
    return BoardValues


def pawnValueEndGameBlack():
    BoardValues={}   
    BoardValues["a8"]=0
    BoardValues["a7"]=-10
    BoardValues["a6"]=-10
    BoardValues["a5"]=6
    BoardValues["a4"]=10
    BoardValues["a3"]=28
    BoardValues["a2"]=1
    BoardValues["a1"]=0

    BoardValues["b8"]=0
    BoardValues["b7"]=-6
    BoardValues["b6"]=-10
    BoardValues["b5"]=-2
    BoardValues["b4"]=5
    BoardValues["b3"]=20
    BoardValues["b2"]=-11
    BoardValues["b1"]=0

    BoardValues["c8"]=0
    BoardValues["c7"]=10
    BoardValues["c6"]=-10
    BoardValues["c5"]=-8
    BoardValues["c4"]=4
    BoardValues["c3"]=21
    BoardValues["c2"]=12
    BoardValues["c1"]=0

    BoardValues["d8"]=0
    BoardValues["d7"]=0
    BoardValues["d6"]=4
    BoardValues["d5"]=-4
    BoardValues["d4"]=-5
    BoardValues["d3"]=28
    BoardValues["d2"]=21
    BoardValues["d1"]=0

    BoardValues["e8"]=0
    BoardValues["e7"]=14
    BoardValues["e6"]=4
    BoardValues["e5"]=-13
    BoardValues["e4"]=-5
    BoardValues["e3"]=30
    BoardValues["e2"]=25
    BoardValues["e1"]=0

    BoardValues["f8"]=0
    BoardValues["f7"]=7
    BoardValues["f6"]=3
    BoardValues["f5"]=-12
    BoardValues["f4"]=-5
    BoardValues["f3"]=7
    BoardValues["f2"]=19
    BoardValues["f1"]=0

    BoardValues["g8"]=0
    BoardValues["g7"]=-5
    BoardValues["g6"]=-6
    BoardValues["g5"]=-10
    BoardValues["g4"]=14
    BoardValues["g3"]=6
    BoardValues["g2"]=4
    BoardValues["g1"]=0

    BoardValues["h8"]=0
    BoardValues["h7"]=-19
    BoardValues["h6"]=-4
    BoardValues["h5"]=-9
    BoardValues["h4"]=9
    BoardValues["h3"]=13
    BoardValues["h2"]=7
    BoardValues["h1"]=0
    return BoardValues





if __name__ == '__main__':
    BW = bishopBoardValuesWhite()
    with open('bishopWhite.txt','w') as file:
        file.write(json.dumps(BW))

    BWE = bishopValueEndGameWhite()
    with open('bishopWhiteEndgame.txt','w') as file:
        file.write(json.dumps(BWE))


    BB = bishopBoardValuesBlack()
    with open('bishopBlack.txt','w') as file:
        file.write(json.dumps(BB))

    BBE = bishopValueEndGameBlack()
    with open('bishopBlackEndGame.txt','w') as file:
        file.write(json.dumps(BBE))



    KW = knightBoardValuesWhite()
    with open('knightWhite.txt','w') as file:
        file.write(json.dumps(KW))

    KWE = knightBoardValuesWhite()
    with open('knightWhiteEndGame.txt','w') as file:
        file.write(json.dumps(KWE))





    KB = knightBoardValuesBlack()
    with open('knightBlack.txt','w') as file:
        file.write(json.dumps(KB))


    KWB = knightBoardValuesBlack()
    with open('knightBlackEndGame.txt','w') as file:
        file.write(json.dumps(KWB))




    RW = rookBoardValuesWhite()
    with open('rookWhite.txt','w') as file:
        file.write(json.dumps(RW))

    RWE = rookValueEndGameWhite()
    with open('rookWhiteEnd.txt','w') as file:
        file.write(json.dumps(RWE))



    RB = rookBoardValuesBlack()
    with open('rookBlack.txt','w') as file:
        file.write(json.dumps(RB))



    RBE = rookValueEndGameBlack()
    with open('rookBlackEnd.txt','w') as file:
        file.write(json.dumps(RBE))



    QW = queenBoardValuesWhite()
    with open('queenWhite.txt','w') as file:
        file.write(json.dumps(QW))


    QWE = queenValueEndGameWhite()
    with open('queenWhiteEnd.txt','w') as file:
        file.write(json.dumps(QWE))


    QB = queenBoardValuesBlack()
    with open('queenBlack.txt','w') as file:
        file.write(json.dumps(QB))

    
    QBE = queenValueEndGameBlack()
    with open('queenBlackEnd.txt','w') as file:
        file.write(json.dumps(QBE))
    
    
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

    PWE = pawnValueEndGameWhite()
    with open('pawnWhiteEnd.txt','w') as file:
        file.write(json.dumps(PWE))


    PB = pawnBoardValuesBlack()
    with open('pawnBlack.txt','w') as file:
        file.write(json.dumps(PB))
    
    PBE = pawnValueEndGameBlack()
    with open('pawnBlackEnd.txt','w') as file:
        file.write(json.dumps(PBE))

    print("Done Making Dicts")