#!/usr/bin/env python3

from IDAstar import *
from Astar import *
from Beam import *
from Astar_DW import *
from timeit import default_timer as timer

import numpy as np;

# M = 4;  #NUMERO DI VEICOLI
# n = 5;  #GRANDEZZAA DELLA MATRICE

M = int(input("Inserisci M>>>"));  #NUMERO DI VEICOLI
n = int(input("Inserisci n>>>"));  #GRANDEZZAA DELLA MATRICE


position = list(zip(range(M), [0 for x in range(M)]))
#position = [(0,0), (1,0), (2,0), (3,0)];

print(len(position))

start = timer();

nodo = Node(tuple(position), None);

ss = Beam(nodo, Manhattan_distance, n, M, 1, 10);

result = ss.search();

end = timer();

print("time elapsed IDA*", end - start)

print("++++ \n", result, "\n");

print_pos(result.positions, n);

p = result;

count = 1;
while not p.parent is None:
    p = p.parent;
    print(str(count) + " ---------\n" + str(p));
    print_pos(p.positions, n)
    count+=1;

print_path(result, n, M);
