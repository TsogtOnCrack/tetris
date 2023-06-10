#Tetris

# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . .[] . . . . .!>
# <! . . .[][][] . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . . . . . . .!>
# <! . . . . .[] . . . .!>
# <! . . . . .[][][] . .!>
# <!********************!>
#  \/\/\/\/\/\/\/\/\/\/\/


# SETUP
# SKETCH
# DRAW
main = []
list = {}

lists = [[1,2],[4,3],[1,2]]

def makeList():
    global lists
    
    for el in lists:
        list[el[0]] = []

    for el in lists:
        list[el[0]].append(el[1])
        
    print(list) 

def setUp():
    
    width = 10
    height = 21
    
    global main
    
    for y in  range(height):
        line = ""
        
        for x in range(width):
            line += " ."
        
        main.append(line)
        
def sketch():
    global list
    global main
    
    for i in range(main):
        print(list[i])
        
def draw():
    global main
    for el in main:
        
        print("<!"+el+"!>")
        
            
        
        
    
    
    
setUp()
sketch()
draw()
     





