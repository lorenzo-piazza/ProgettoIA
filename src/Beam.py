#!/usr/bin/env python3

from utility import *
import heapq;

class PQueue:
	def __init__(self, maxsize: int = 10):
		self.maxsize = maxsize;
		self.size = 0;
		self.heap: list = [];

	def push(self, value: Node, reached: set):
		if(self.size < self.maxsize):
			heapq.heappush(self.heap, value);
			self.size += 1;
		elif(self.size == self.maxsize):
			heapq.heappush(self.heap, value);
			val = self.heap.pop();
			reached.remove(val.positions);
			del val;

	def pop(self) -> Node:
		self.size -= 1;
		return heapq.heappop(self.heap)

	def notempty(self) -> bool:
		return bool(self.heap);

	def __len__(self) -> int:
		return self.size;

class Beam:
	def H(self, nodo: Node) -> float:
		pos = nodo.positions;
		return sum((self.distance(x, i, self.n) for (i, x) in zip(self.indices, pos)));

	def __init__(self, s: Node, distance: Callable, n: int, M: int, W: float = 1, size: int = 1000, *args):
		self.n = n; self.M = M;
		self.distance = distance;
		self.frontier = PQueue(size);
		self.reached: set = set();
		self.indices = [x+1  for (x,y) in s.positions];
		self.nodo = s;
		self.W = W;
		self.nodo.h = self.W * self.H(self.nodo);

		self.frontier.push(self.nodo, self.reached);

	def search(self) -> Optional[Node]:
		while self.frontier.notempty():
			self.nodo = self.frontier.pop();

			if(self.nodo.h == 0):   ## GOAL
				return self.nodo;
			else:
				for x in self.nodo.get_neighbors(self.n, self.M):
					if(x.positions not in self.reached):
						self.reached.add(x.positions)
						x.h = self.W * self.H(x);
						self.frontier.push(x, self.reached);
		return None
