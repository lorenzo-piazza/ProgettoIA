#!/usr/bin/env python3

# A*
# Greedy-Seach
# UCS

from itertools import combinations
import numpy as np

# M = 7;
# n = 7;

# grid = np.array([[1,0,0,0,0,0,0],
#                  [2,0,0,0,0,0,0],
#                  [3,0,0,0,0,0,0],
#                  [4,0,0,0,0,0,0],
#                  [5,0,0,0,0,0,0],
#                  [6,0,0,0,0,0,0],
#                  [7,0,0,0,0,0,0]]);

M = 3;
n = 3;

grid = np.array([[0,3,0], [2,1,0], [0,0,0]]);

class Node:
    def __init__(self, positions):

        self.positions = positions;

        self.g = 0;   ## PATH-COST
        self.h = 0;   ## HEURISTIC

        self.neighbors = [];

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

    def append_impossible(self, toadd, pos, i):
        if(pos in toadd):
            return True;
        else:
            toadd[i] = pos;
            return False

    def add_neigbors(self, grid, n, M):

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
            for i in range(len(self.positions)):
                if(comb[i] == 0):
                    inplace.append(self.positions[i]);
                    toadd[i] = self.positions[i];

            #print("inplace --- ",comb, inplace)

            for i in range(len(self.positions)):
                (x,y) = self.positions[i];

                match comb[i]:
                    case 1:
                        if x > 0:
                            adj = self.four_adj(self.positions[i]);
                            add = (x - 1, y);
                            if 1 in adj:
                                if add not in arr_adj and add in inplace and x - 1 > 0:
                                    if self.append_impossible(toadd, (x - 2, y), i): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i): break;
                            else:
                                if self.append_impossible(toadd, add, i): break;
                        else:
                            break;

                    case 2:
                        if y < n-1:
                            adj = self.four_adj(self.positions[i]);
                            add = (x, y + 1)
                            if 2 in adj:
                                if add not in arr_adj and add in inplace and y + 1 < n-1:
                                    if self.append_impossible(toadd, (x, y + 2), i): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i): break;
                            else:
                                if self.append_impossible(toadd, add, i): break;
                        else:
                            break;

                    case 3:
                        if x < n-1:
                            adj = self.four_adj(self.positions[i]);
                            add = (x + 1, y)
                            if 3 in adj:
                                if add not in arr_adj and add in inplace and x + 1 < n-1:
                                    if self.append_impossible(toadd, (x + 2, y), i): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i): break;
                            else:
                                if self.append_impossible(toadd, add, i): break;
                        else:
                            break;

                    case 4:
                        if y > 0:
                            adj = self.four_adj(self.positions[i]);
                            add = (x, y - 1)
                            if 4 in adj:
                                if add not in arr_adj and add in inplace and y - 1 > 0:
                                    if self.append_impossible(toadd, (x, y - 2), i): break;
                                    arr_adj.append(add)
                                else:
                                    if self.append_impossible(toadd, add, i): break;
                            else:
                                if self.append_impossible(toadd, add, i): break;
                        else:
                            break;

                    case _:
                        pass;
            else:
                self.neighbors.append(toadd);



class Astar():
    pass
