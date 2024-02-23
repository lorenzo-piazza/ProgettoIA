#!/usr/bin/env python3

from utility import *

import math
import time

class IDAstar:
	def H(self, nodo: Node) -> float:
		pos = nodo.positions;
		return sum((self.distance(x, i, self.n) for (i, x) in zip(self.indices, pos)));

	def __init__(self, s: Node, distance: Callable, n: int, M: int, W: float = 1):
		self.n = n; self.M = M;
		self.distance = distance;
		self.indices = [x+1 for (x,y) in s.positions];
		self.nodo = s;
		self.W = W;
		self.nodo.h = self.W * self.H(self.nodo);

	def search(self) -> Node:
		self.threshold = self.nodo.g + self.W * self.nodo.h;
		while(True):
			self.reached: set = set();
			self.valmin = float("inf");
			self.result: Any = None;
			self.search_rec(self.nodo);

			if(self.result is not None):
				return self.result;
			else:
				self.threshold = self.valmin;

			#print(str(self.threshold) +  " \n ----------------- \n" + str(self.nodo))


	def search_rec(self, node: Node):
		if(node.h == 0):   ## GOAL
			self.result = node;
		elif(node.g + node.h > self.threshold):
			if(node.g + node.h < self.valmin):
				self.valmin = node.g + node.h;
		else:
			for x in node.get_neighbors(self.n, self.M):
				x.h = self.H(x);
				self.search_rec(x);
