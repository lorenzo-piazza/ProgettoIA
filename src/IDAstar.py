#!/usr/bin/env python3

from utility import *
import os, psutil
import math
import time
process = psutil.Process()


class IDAstar():
    __slots__ = ("grid", "distance", "frontier", "indices", "reached", "nodo", "threshold" ,"n", "M", "W")

    def H(self, nodo):
        pos = nodo.positions;
        return sum((self.distance(x, i) for (i, x) in zip(self.indices, pos)));

    def __init__(self, s, distance, n, M, W=1):
        self.n = n; self.M = M;
        self.distance = distance;
        self.indices = [x+1 for (x,y) in s.positions];
        self.nodo = s;
        self.W = W;
        #print("sss", s);
        self.nodo.h = self.W * self.H(self.nodo);

    def search(self):
        self.threshold = self.nodo.g + self.W * self.nodo.h;
        while(True):
            self.frontier = [self.nodo];
            self.reached = set();
            result = self.search_rec(self.threshold);

            if(isinstance(result, Node)):
                return result;
            else:
                self.threshold = result;

            print(str(self.threshold) +  " \n ----------------- \n" + str(self.nodo))


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
                node.add_neighbors(self.n, self.M);
                for x in node.neighbors:
                    x.h = self.H(x);
                    #print(x);
                    self.frontier.append(x);
        return valmin
