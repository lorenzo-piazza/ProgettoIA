#!/usr/bin/env python3

from IDAstar import *
from Astar import *
from Beam import *
from timeit import default_timer as timer

import numpy as np;

print(grid, "\n");

position = [(0,0), (1,0), (2,0)];

print(len(position))

start = timer();

nodo = Node(tuple(position), None);

ss = IDAstar(nodo, Manhattan_distance, grid , n, M)

result = ss.search();

end = timer();

print("time elapsed IDA*", end - start)

print("++++ \n", result, "\n");

print_pos(result.positions, n);

p = result;

count = 1;
while not p.parent is None:
    p = p.parent;
    print(str(count) + " ---------\n", p);
    print_pos(p.positions, n)
    count+=1;
