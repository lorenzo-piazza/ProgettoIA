#!/usr/bin/env python3

from itertools import combinations
from queue import PriorityQueue

import time
import functools
import numpy as np

M = 5;
n = 5;

grid = np.array([[1,0,0,0,0],
                 [2,0,0,0,0],
                 [3,0,0,0,0],
                 [4,0,0,0,0],
                 [5,0,0,0,0]]);

# M = 3;
# n = 3;

# grid = np.array([[1,0,0], [2,0,0], [3,0,0]]);


colors = ['\033[0;32m', '\033[0;31m', '\033[0;33m', '\x1b[35m', '\033[0;36m']
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def print_matrix(arr):
    for x in arr:
        print("[", end="")
        for y in x:
            if y != 0:
                print(colors[int(y) % len(colors)] + str(int(y)) + ENDC, end=" ")
            else:
                print(int(y), end=" ")
        print("\b]")

def print_pos(pos, n):
    arr = np.zeros((n,n))
    count = 0;
    for i in pos:
        count += 1
        (x,y) = i;
        arr[x][y] = count;
    print_matrix(arr);
    print("")

def Manhattan_distance(pos, i):
    (x,y) = pos;
    return abs(x - (n-i)) + abs(y - (n-1));

@functools.total_ordering
class Node:
    def __init__(self, positions, parent, g = 0):
        self.positions = positions;
        self.parent = parent;

        self.g = g;   ## PATH-COST
        self.h = 0;   ## HEURISTIC

        self.neighbors = [];

    def __gt__(self, other):
        return self.g + self.h > other.g + other.h;

    def __eq__(self, other):
        return self.g + self.h == other.g + other.h;

    def __repr__(self):
        return str(id(self)) + " - " + str(self.g) + " " +  str(self.h) + " " + \
               str(None if self.parent is None else id(self.parent)) + " " + str(self.positions);

    def four_adj(self, pos):
        x,y = pos;
        adj = []
        if x > 0 and grid[x-1][y]:
            adj.append(1);
        if y < n-1 and grid[x][y+1]:
            adj.append(2);
        if x < n-1 and grid[x+1][y]:
            adj.append(3);
        if y > 0 and grid[x][y-1]:
            adj.append(4);
        return adj;

    def append_impossible(self, toadd, pos, i, cost):
        if(pos in toadd):
            return True;
        else:
            toadd[i] = pos;
            self.cost += cost;
            return False

    def add_neighbors(self, grid, n, M):

        # 0 fermi
        # 1 Su
        # 2 Destra
        # 3 Giu
        # 4 Sinistra

        comb = [0 for x in range(M)]; comb[0] = -1;
        end = [4 for x in range(M)];

        while comb != end:
            comb[0] += 1; riporto = 0;

            for i in range(len(comb)):
                if(riporto):
                    comb[i] += 1;
                    riporto = 0;

                if(comb[i]==5):
                    comb[i] = 0;
                    riporto = 1;
                else:
                    break

            inplace = []; toadd = [None for x in range(M)];  arr_adj = [];
            self.cost = 0;

            for i in range(len(self.positions)):
                if(comb[i] == 0):
                    inplace.append(self.positions[i]);
                    toadd[i] = self.positions[i];

            for i in range(len(self.positions)):
                (x,y) = self.positions[i];

                match comb[i]:
                    case 1:
                        if x > 0:
                            adj = self.four_adj(self.positions[i]);
                            add = (x - 1, y);
                            if 1 in adj:
                                if add not in arr_adj and add in inplace and x - 1 > 0:
                                    if self.append_impossible(toadd, (x - 2, y), i, 2): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i, 1): break;
                            else:
                                if self.append_impossible(toadd, add, i, 1): break;
                        else:
                            break;

                    case 2:
                        if y < n-1:
                            adj = self.four_adj(self.positions[i]);
                            add = (x, y + 1)
                            if 2 in adj:
                                if add not in arr_adj and add in inplace and y + 1 < n-1:
                                    if self.append_impossible(toadd, (x, y + 2), i, 2): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i, 1): break;
                            else:
                                if self.append_impossible(toadd, add, i, 1): break;
                        else:
                            break;

                    case 3:
                        if x < n-1:
                            adj = self.four_adj(self.positions[i]);
                            add = (x + 1, y)
                            if 3 in adj:
                                if add not in arr_adj and add in inplace and x + 1 < n-1:
                                    if self.append_impossible(toadd, (x + 2, y), i, 2): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i, 1): break;
                            else:
                                if self.append_impossible(toadd, add, i, 1): break;
                        else:
                            break;

                    case 4:
                        if y > 0:
                            adj = self.four_adj(self.positions[i]);
                            add = (x, y - 1)
                            if 4 in adj:
                                if add not in arr_adj and add in inplace and y - 1 > 0:
                                    if self.append_impossible(toadd, (x, y - 2), i, 2): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i, 1): break;
                            else:
                                if self.append_impossible(toadd, add, i, 1): break;
                        else:
                            break;

                    case _:
                        pass;
            else:
                if(toadd != self.positions):
                    no = Node(tuple(toadd), self, self.cost + self.g);
                    self.neighbors.append(no);
