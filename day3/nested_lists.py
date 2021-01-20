from pprint import pprint
from copy import deepcopy

matrix = [
    #    0, 1, 2
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]
pprint(matrix)

# matrix2 = matrix.copy() # shallow copy
matrix2 = deepcopy(matrix)
matrix2[1][1] = 0

pprint(matrix2)
pprint(matrix)
