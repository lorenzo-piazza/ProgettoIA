#!/usr/bin/env python3

from Astar_nomatch import *
import numpy as np;


def H(nodo):
    pos = nodo.positions;
    return sum((Manhattan_distance(x, i+1) for (i, x) in enumerate(pos)));

grid = np.array([[0, 0, 3],
                 [0, 2, 0],
                 [0, 0, 1]])

print(grid, "\n");

position = [(0,2), (1,1), (0,2)];

print(len(position))

nodo = Node(position, None);

nodo.add_neighbors(grid, n, M);

#ss = Astar(nodo, Manhattan_distance, grid , n, M)

#result = ss.search();

#print(result);


for x in nodo.neighbors:
    x.h = H(x);
    print(x)
    print_pos(x.positions, n)
