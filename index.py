# Tetris

# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . .[] . . . . .!>
# <! . . .[][][] . . . .!>          item cords {right top most block cords, type, rotation}
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . .[] . . . .!>
# <! . . . . .[][][] . .!>           bottom Item [ {x , y} ... ]
# <!********************!>
#  \/\/\/\/\/\/\/\/\/\/\/

# main logic:
# setup -> |move()-| -> draw() -> checkForRules() -> draw() --> |move-|


from board import makeBoard
from drawShape import getCordsOfShape

# declair scalar constants:
WIDTH_OF_BOARD = 10
HEIGHT_OF_BOARD = 21


# setUp
BOARD = makeBoard(HEIGHT_OF_BOARD, WIDTH_OF_BOARD)









#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


##UPDATE!!!!!!!!
# work on array consisting of 1, 0
#turn said array into " ." and "[]" in draw


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!











def sketch():

    a = getCordsOfShape(1, {"x": 1, "y": 1}, 2)["cords"] #get 'cords' of the object given from the function

    for el in a: #go throught each cords from a
        # print(el)
        for i in range(len(BOARD)): #y
            for j in range(2, WIDTH_OF_BOARD*2, 2): #x
                
                it = BOARD[i][j] + BOARD[i][j+1]
                
                print(it)

                # if i == el["y"] and j == el["x"]: #check if y and x match the cords

                #     # BOARD[i][j] = "8" # change said cords to 8
                #     print(BOARD[i][j])


def draw():  # final draw of what is on the board

    for el in BOARD:
        print(el)


sketch()
draw()
