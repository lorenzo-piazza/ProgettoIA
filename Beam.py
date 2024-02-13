#!/usr/bin/env python3

from utility import *
import heapq;
import os, psutil

process = psutil.Process()

class PQueue():
    def __init__(self, maxsize = 10):
        self.maxsize = maxsize;
        self.size = 0;
        self.heap = [];

    def push(self, value, reached):
        if(self.size < self.maxsize):
            heapq.heappush(self.heap, value);
            self.size += 1;
        elif(self.size == self.maxsize):
            heapq.heappush(self.heap, value);
            val = self.heap.pop();
            reached.remove(val.positions);
            del val;

    def pop(self):
        self.size -= 1;
        return heapq.heappop(self.heap)

    def notempty(self):
        return bool(self.heap);

    def __len__(self):
        return self.size;

class Beam():
    def H(self, nodo):
        pos = nodo.positions;
        return sum((self.distance(x, i+1) for (i, x) in enumerate(pos)));

    def __init__(self, s, distance, grid, n, M, size = 100000):
        self.grid = grid; self.n = n; self.M = M;
        self.distance = distance;
        self.frontier = PQueue(size);
        self.reached = set();
        self.nodo = s;
        self.nodo.h = self.H(self.nodo);

        self.frontier.push(self.nodo, self.reached);

    def search(self):
        while self.frontier.notempty():
            self.nodo = self.frontier.pop();

            #print("len --" , len(self.frontier), process.memory_info().rss);
            #print(self.nodo)
            #print_pos(self.nodo.positions, self.n);

            if(self.nodo.h == 0):   ## GOAL
                return self.nodo;
            else:
                self.nodo.add_neighbors(self.n, self.M);
                for x in self.nodo.neighbors:
                    if(x.positions not in self.reached):
                        self.reached.add(x.positions)
                        x.h = self.H(x);
                        #print(x);
                        self.frontier.push(x, self.reached);
