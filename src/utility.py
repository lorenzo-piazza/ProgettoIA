#!/usr/bin/env python3

from itertools import combinations
from queue import PriorityQueue

import time
import functools
import math
import numpy as np

ENDC = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\x1b[3m'
UNDERLINE = '\033[4m'
colors = [UNDERLINE, "\x1b[32m", "\x1b[31m", "\x1b[33m", "\x1b[34m", "\x1b[35m", "\x1b[36m", BOLD, ITALIC]


def print_path(node, n , M):
	print("PATH --------------- PATH\n")
	for i in range(M):
		p = node;
		pos = dict()
		old = None;
		while not p is None:
			if old is not None:
				xo, yo = p.positions[i];
				x , y = old
				if x - xo > 0:
					pos[p.positions[i]] = "▾"
				elif x - xo < 0:
					pos[p.positions[i]] = "▴"
				elif y - yo > 0:
					pos[p.positions[i]] = "▸"
				elif y - yo < 0:
					pos[p.positions[i]] = "◂"
				else:
					pos[p.positions[i]] = "·";
			else:
				pos[p.positions[i]] = "×";

			old = p.positions[i];

			p = p.parent;

		arr = np.zeros((n,n)); cont = 0;
		for x in range(n):
			print("[", end="")
			for y in range(n):
				if (x,y) in pos:
					cont += 1;
					print(colors[int(i+1) % len(colors)] + pos[(x,y)] + ENDC, end=" ")
				else:
					print(0, end=" ")
			print("\b]")

		print("");

def print_matrix(arr):
	for x in arr:
		print("[", end="")
		for y in x:
			if y != 0:
				print(colors[int(y) % len(colors)] + str(int(y)) + ENDC, end=" ")
			else:
				print(int(y), end=" ")
		print("\b]")

def print_pos(pos, n):
	arr = np.zeros((n,n))
	count = 0;
	for i in pos:
		count += 1
		(x,y) = i;
		arr[x][y] = count;
	print_matrix(arr);
	print("")

def Manhattan_distance(pos, i, n):
	(x,y) = pos;
	return (abs(x - (n-i)) + abs(y - (n-1)));

def Chebyshev_distance(pos, i, n):
	(x,y) = pos;
	return max(abs(x - (n-i)), abs(y - (n-1)));

def Euclidean_distance(pos, i, n):
	(x,y) = pos;
	return math.sqrt((x - (n-i))**2 + (y - (n-1))**2);

@functools.total_ordering
class Node:
	__slots__ = ("positions", "parent", "g", "h", "cost", "d")

	def __init__(self, positions, parent, g = 0):
		self.positions = positions;
		self.parent = parent;

		self.g = g;   ## PATH-COST
		self.h = 0;   ## HEURISTIC

	def __gt__(self, other):
		return self.g + self.h > other.g + other.h;

	def __lt__(self, other):
		return self.g + self.h < other.g + other.h;

	def __eq__(self, other):
		return self.g + self.h == other.g + other.h;

	def __repr__(self):
		return str(id(self)) + " - " + str(self.g) + " " +  str(self.h) + " " + \
			   str(None if self.parent is None else id(self.parent)) + " " + str(self.positions);

	def four_adj(self, pos, n):
		x,y = pos;

		if x > 0 and (x-1, y) in self.positions:
			return 1;
		if y < n-1 and (x, y+1) in self.positions:
			return 2;
		if x < n-1 and (x + 1, y) in self.positions:
			return 3;
		if y > 0 and (x, y - 1) in self.positions:
			return 4;

	def append_impossible(self, toadd, pos, i, cost):
		if(pos in toadd):
			return True;
		else:
			toadd[i] = pos;
			self.cost += cost;
			return False

	def get_neighbors(self, n, M):
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
			self.cost = 0;

			for i in range(len(self.positions)):
				if(comb[i] == 0):
					self.cost += 1;
					inplace.append(self.positions[i]);
					toadd[i] = self.positions[i];

			for i in range(len(self.positions)):
				(x,y) = self.positions[i];
				if comb[i] == 1:
					if x > 0:
						adj = self.four_adj(self.positions[i], n);
						add = (x - 1, y);
						if 1 == adj:
							if add not in arr_adj and add in inplace and x - 1 > 0:
								if self.append_impossible(toadd, (x - 2, y), i, 1): break;
								arr_adj.append(add)
							else:
								if self.append_impossible(toadd, add, i, 1): break;
						else:
							if self.append_impossible(toadd, add, i, 1): break;
					else:
						break;

				if comb[i] == 2:
					if y < n-1:
						adj = self.four_adj(self.positions[i], n);
						add = (x, y + 1)
						if 2 == adj:
							if add not in arr_adj and add in inplace and y + 1 < n-1:
								if self.append_impossible(toadd, (x, y + 2), i, 1): break;
								arr_adj.append(add)
							else:
								if self.append_impossible(toadd, add, i, 1): break;
						else:
							if self.append_impossible(toadd, add, i, 1): break;
					else:
						break;

				if comb[i] == 3:
					if x < n-1:
						adj = self.four_adj(self.positions[i], n);
						add = (x + 1, y)
						if 3 == adj:
							if add not in arr_adj and add in inplace and x + 1 < n-1:
								if self.append_impossible(toadd, (x + 2, y), i, 1): break;
								arr_adj.append(add)
							else:
								if self.append_impossible(toadd, add, i, 1): break;
						else:
							if self.append_impossible(toadd, add, i, 1): break;
					else:
						break;

				if comb[i] == 4:
					if y > 0:
						adj = self.four_adj(self.positions[i], n);
						add = (x, y - 1)
						if 4 == adj:
							if add not in arr_adj and add in inplace and y - 1 > 0:
								if self.append_impossible(toadd, (x, y - 2), i, 1): break;
								arr_adj.append(add)
							else:
								if self.append_impossible(toadd, add, i, 1): break;
						else:
							if self.append_impossible(toadd, add, i, 1): break;
					else:
						break;
			else:
				toadd = tuple(toadd);
				if(toadd != self.positions):
					yield Node(toadd, self, self.cost + self.g);

	# def add_neighbors(self, n, M):
	#     self.neighbors = list(self.get_neighbors(n, M));
