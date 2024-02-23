#!/usr/bin/env python3

from utility import *

class Astar_DW:
	def H(self, nodo: Node) -> float:
		pos = nodo.positions;
		return sum((self.distance(x, i) for (i, x) in zip(self.indices, pos)));

	def PESO(self, d: int) -> float:
		if (d <= self.N):
			return 1 - (d/ self.N)
		else:
			return 0;

	def __init__(self, s: Node, distance: Callable, n: int, M: int, W: float = 1, *args):
		self.n = n; self.M = M;
		self.distance = distance;
		self.frontier: PriorityQueue = PriorityQueue();
		self.reached: set = set();
		self.indices = [x+1  for (x,y) in s.positions];
		self.nodo = s;
		self.W = W
		self.N = (n*2 - 2)+5;

		self.nodo.d = 0;
		self.nodo.h = (1 + self.W * self.PESO(0)) * self.H(self.nodo);

		self.frontier.put(self.nodo);

	def search(self) -> Optional[Node]:
		while not self.frontier.empty():
			self.nodo = self.frontier.get();

			if(self.nodo.h == 0):   ## GOAL
				return self.nodo;
			else:
				for x in self.nodo.get_neighbors(self.n, self.M):
					if(x.positions not in self.reached):
						self.reached.add(x.positions)
						x.h = (1 + self.W * self.PESO(x.d)) * self.H(x);
						self.frontier.put(x);
		return None
