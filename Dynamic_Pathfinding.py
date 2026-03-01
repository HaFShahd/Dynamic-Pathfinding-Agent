import tkinter as tk
import random
import time
import heapq
import math

CELL_SIZE = 25


class Node:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f
