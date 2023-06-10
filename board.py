def makeBoard(height, length):
    board = []
    for i in range(height):

        line = "<!"
        for j in range(length):
            line = line + " ."
        line += "!>"

        board.append(line)

    # lastLine = "<!"
    # for i in range(length):
    #     lastLine += "**"
    # lastLine += "!>"

    # board.append(lastLine)

    return board


# theboard = makeBoard(21, 10)

# for el in theboard:
#     print(el)
