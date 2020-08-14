WIDTH = 600
HEIGHT = 600

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (96, 216, 232)

# Boards
testBoard = [[0 for x in range(9)] for x in range(9)]
testBoard2 = [[0,6,0,2,0,0,8,3,1],
              [0,0,0,0,8,4,0,0,0],
              [0,0,7,6,0,3,0,4,9],
              [0,4,6,8,0,2,1,0,0],
              [0,0,3,0,9,6,0,0,0],
              [1,2,0,7,0,5,0,0,6],
              [7,3,0,0,0,1,0,2,0],
              [8,1,5,0,2,9,7,0,0],
              [0,0,0,0,7,0,0,1,5]]

# Positions and sizes
gridPos = (75,100)
cellSize = 50
gridSize = cellSize*9