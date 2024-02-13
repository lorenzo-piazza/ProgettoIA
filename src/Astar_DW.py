#!/usr/bin/env python3

from utility import *

class Astar_DW():
    def H(self, nodo):
        pos = nodo.positions;
        return sum((self.distance(x, i) for (i, x) in zip(self.indices, pos)));

    def PESO(self, d):
        if (d <= self.N):
            return 1 - (d/ self.N)
        else:
            return 0;

    def __init__(self, s, distance, n, M, W = 1):
        self.n = n; self.M = M;
        self.distance = distance;
        self.frontier = PriorityQueue();
        self.reached = set();
        self.indices = [x+1  for (x,y) in s.positions];
        self.nodo = s;
        self.W = W
        self.N = (n*2 - 2)+5;
        #print("sss", s);
        self.nodo.d = 0;
        self.nodo.h = (1 + self.W * self.PESO(0)) * self.H(self.nodo);

        self.frontier.put(self.nodo);

    def search(self):
        while not self.frontier.empty():
            self.nodo = self.frontier.get();

            #print(self.frontier.qsize());
            #print(self.nodo)
            #print_pos(self.nodo.positions, self.n);
            #time.sleep(0.5)
            if(self.nodo.h == 0):   ## GOAL
                return self.nodo;
            else:
                self.nodo.add_neighbors(self.n, self.M);
                for x in self.nodo.neighbors:
                    if(x.positions not in self.reached):
                        self.reached.add(x.positions)
                        x.d = self.nodo.d + 1;
                        x.h = (1 + self.W * self.PESO(x.d)) * self.H(x);
                        #print(x);
                        self.frontier.put(x);
