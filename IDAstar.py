#!/usr/bin/env python3

from utility import *
import os, psutil
import math
import time
process = psutil.Process()


class IDAstar():
    __slots__ = ("grid", "distance", "frontier", "reached", "nodo", "threshold" ,"n", "M")

    def H(self, nodo):
        pos = nodo.positions;
        return sum((self.distance(x, i+1) for (i, x) in enumerate(pos)));

    def __init__(self, s, distance, grid, n, M):
        self.grid = grid; self.n = n; self.M = M;
        self.distance = distance;
        self.nodo = s;
        #print("sss", s);
        self.nodo.h = self.H(self.nodo);

    def search(self):
        self.threshold = self.nodo.g + self.nodo.h;
        while(True):
            self.frontier = [self.nodo];
            self.reached = set();
            result = self.search_rec(self.threshold);

            if(isinstance(result, Node)):
                return result;
            else:
                self.threshold = result;

            print(str(self.threshold) +  " \n ----------------- \n" + str(self.nodo))
            time.sleep(1)


    def search_rec(self, threshold):
        valmin = float("inf");
        while self.frontier:
            node = self.frontier.pop();

            #print(len(self.frontier), threshold, process.memory_info().rss);
            #print(node)
            #print_pos(node.positions, self.n);
            #time.sleep(1)

            if(node.h == 0):   ## GOAL
                return node;
            elif(node.g + node.h > threshold):
                if(node.g + node.h < valmin):
                    valmin = node.g + node.h;
            else:
                node.neighbors = [];
                node.add_neighbors(self.n, self.M);
                for x in node.neighbors:
                    if (x.positions not in self.reached):
                        x.h = self.H(x);
                        self.reached.add(x.positions)
                        #print(x);
                        if(x.g + x.h > threshold):
                            if(x.g + x.h < valmin):
                                valmin = x.g + x.h;
                        else:
                            self.frontier.append(x);
        return valmin
