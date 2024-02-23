#!/usr/bin/env python3
from utility import *

class Astar:
	def H(self, nodo: Node) -> float:
		pos = nodo.positions;
		return sum((self.distance(x, i, self.n) for (i, x) in zip(self.indices, pos)));

	def __init__(self, s: Node, distance: Callable, n: int, M: int, W: float = 1):
		self.n = n; self.M = M;
		self.distance = distance;
		self.frontier: PriorityQueue = PriorityQueue();
		self.reached: set = set();
		self.indices = [x+1  for (x,y) in s.positions];
		self.nodo = s;
		self.W = W
		#print("sss", s);
		self.nodo.h = self.W * self.H(self.nodo);

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
						x.h = self.W * self.H(x);
						self.frontier.put(x);
		return None
