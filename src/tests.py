#!/usr/bin/env python3

from IDAstar import *
from Astar import *
from Beam import *
from Astar_DW import *
from timeit import default_timer as timer

import numpy as np;

position = [(0,0), (1,0), (2,0), (3,0), (9,0), (7,0), (4,0), (5,0), (8,0)];

print(len(position))

start = timer();

nodo = Node(tuple(position), None);

ss = Beam(nodo, Manhattan_distance, n, M, 20, 2);

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
