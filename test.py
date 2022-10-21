

import numpy as np
from rich import print


board = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
])

print(board)


board = np.rot90(board)
print(board)

board = np.rot90(board)
print(board)