#!/usr/bin/env python3

from Astar import *
import numpy as np;

print(grid, "\n");

position = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0)];

print(len(position))

nodo = Node(tuple(position), None);

ss = Astar(nodo, Manhattan_distance, grid , n, M)

result = ss.search();

print("++++ \n", result, "\n");

print_pos(result.positions, n);

p = result;

while not p.parent is None:
    p = p.parent;
    print("----- \n", p);
    print_pos(p.positions, n)
