#!/usr/bin/env python3

from Astar import *
import numpy as np;


def print_pos(pos, n):
    arr = np.zeros((n,n))
    count = 0;
    for i in pos:
        count += 1
        (x,y) = i;
        arr[x][y] = count;
    print(arr);
    print("")

print(grid, "\n");

position = [(1,1), (1,0), (0,1)];

print(len(position))

nodo = Node(position);

nodo.add_neigbors(grid, n , M)

print(len(nodo.neighbors));

print(nodo.neighbors);


for x in nodo.neighbors:
    print_pos(x, n)
