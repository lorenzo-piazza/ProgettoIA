#!/usr/bin/env python3

from utility import *

class IDAstar():
    def H(self, nodo):
        pos = nodo.positions;
        return sum((self.distance(x, i+1) for (i, x) in enumerate(pos)));

    def __init__(self, s, distance, grid, n, M):
        self.grid = grid; self.n = n; self.M = M;
        self.distance = distance;
        self.frontier = PriorityQueue();
        self.reached = set();
        self.nodo = s;
        #print("sss", s);
        self.nodo.h = self.H(self.nodo);

        self.frontier.put(self.nodo);

    def search(self):
        while not self.frontier.empty():
            self.nodo = self.frontier.get();

            print(self.frontier.qsize());
            #print(self.nodo)
            #print_pos(self.nodo.positions, self.n);
            #time.sleep(1)
            if(self.nodo.h == 0):   ## GOAL
                return self.nodo;
            else:
                self.nodo.add_neighbors(self.grid, self.n, self.M);
                for x in self.nodo.neighbors:
                    if(x.positions not in self.reached):
                        self.reached.add(x.positions)
                        x.h = self.H(x);
                        #print(x);
                        self.frontier.put(x);
