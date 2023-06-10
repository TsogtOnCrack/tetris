# BLOCKS:

# {}[][][]  type 1 = {cords: {1: {x: x, y: y}, 2: {x: x+1, y: y}, 3: {x: x+2, y: y}, 4: {x: x+3, y: y}}, bottomY: y}


# {}[]       type 2 = {cords: {1: {x: x, y: y}, 2: {x: x+1, y: y}, 3: {x: x, y: y-1}, 4: {x: x+1, y: y -1}}, bottomY: y -1}
# [][]

# {}         type 3 = {cords: {1: {x: x, y: y}, 2: {x: x, y: y-1}, 3: {x: x + 1, y: y-1}, 4: {x: x + 2, y: y -1}}, bottomY: y -1}
# [][][]

#    {}     type 4 = {cords: {1: {x: x, y: y}, 2: {x: x -2 , y: y-1}, 3: {x: x - 1, y: y-1}, 4: {x: x, y: y -1}}, bottomY: y -1}
# [][][]

# {}[]       type 5 = {cords: {1: {x: x, y: y}, 2: {x: x + 1, y: y}, 3: {x: x + 1, y: y-1}, 4: {x: x + 2, y: y -1}}, bottomY: y -1}
#  [][]

#  {}[]     type 6 = {cords: {1: {x: x, y: y}, 2: {x: x + 1, y: y}, 3: {x: x - 1, y: y-1}, 4: {x: x , y: y -1}}, bottomY: y -1}
# [][]

#  {}       type 7 = {cords: {1: {x: x, y: y}, 2: {x: x - 1, y: y-1}, 3: {x: x , y: y-1}, 4: {x: x + 1, y: y -1}}, bottomY: y -1}
# [][][]


# in: t, c, r   out: 4cords of the item
def getCordsOfShape(type, coordinates, rotation):
    x = coordinates["x"]
    y = coordinates["y"]

    types = [{"cords": [{"x": x, "y": y}, {"x": x+1, "y": y}, {"x": x+2, "y": y}, {"x": x+3, "y": y}], "bottomY": y},
             {"cords": [{"x": x, "y": y}, {"x": x+1, "y": y},  {"x": x, "y": y-1}, {"x": x+1, "y": y - 1}], "bottomY": y - 1},
             {"cords": [{"x": x, "y": y}, {"x": x, "y": y-1}, {"x": x + 1, "y": y-1}, {"x": x + 2, "y": y - 1}], "bottomY": y - 1},
             {"cords": [{"x": x, "y": y}, {"x": x - 2, "y": y-1}, {"x": x - 1, "y": y-1}, {"x": x, "y": y - 1}], "bottomY": y - 1},
             {"cords": [{"x": x, "y": y}, {"x": x + 1, "y": y},  {"x": x + 1, "y": y-1}, {"x": x + 2, "y": y - 1}], "bottomY": y - 1},
             {"cords": [{"x": x, "y": y}, {"x": x + 1, "y": y}, {"x": x - 1, "y": y-1}, {"x": x, "y": y - 1}], "bottomY": y - 1},
             {"cords": [{"x": x, "y": y}, {"x": x - 1, "y": y-1},  {"x": x, "y": y-1}, {"x": x + 1, "y": y - 1}], "bottomY": y - 1},
            ]

    return types[type - 1]
