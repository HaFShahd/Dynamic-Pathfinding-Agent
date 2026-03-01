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

class PathfindingApp:
    def __init__(self, root, rows=20, cols=20):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.dynamic_mode = False
        self.algorithm = "A*"
        self.heuristic_type = "Manhattan"
        self.edit_mode = "wall"

        self.canvas = tk.Canvas(root,
                                width=cols * CELL_SIZE,
                                height=rows * CELL_SIZE)
        self.canvas.pack()

        self.info = tk.Label(root, text="Ready")
        self.info.pack()

        self.grid = []
        r = 0
        while r < rows:
            row = []
            c = 0
            while c < cols:
                row.append(0)
                c += 1
            self.grid.append(row)
            r += 1

        self.start = (0, 0)
        self.goal = (rows - 1, cols - 1)
        self.agent_pos = self.start

        self.canvas.bind("<Button-1>", self.toggle_wall)

        self.draw_grid()
        self.create_buttons()


    def draw_grid(self):
        self.canvas.delete("all")

        r = 0
        while r < self.rows:
            c = 0
            while c < self.cols:
                color = "white"

                if self.grid[r][c] == 1:
                    color = "black"

                if (r, c) == self.start:
                    color = "orange"

                if (r, c) == self.goal:
                    color = "purple"

                self.canvas.create_rectangle(
                    c * CELL_SIZE, r * CELL_SIZE,
                    (c + 1) * CELL_SIZE, (r + 1) * CELL_SIZE,
                    fill=color, outline="gray"
                )
                c += 1
            r += 1
