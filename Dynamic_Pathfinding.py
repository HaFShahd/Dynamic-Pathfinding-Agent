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


    def toggle_wall(self, event):
        r = event.y // CELL_SIZE
        c = event.x // CELL_SIZE

        if self.edit_mode == "wall":
            if (r, c) != self.start and (r, c) != self.goal:
                if self.grid[r][c] == 0:
                    self.grid[r][c] = 1
                else:
                    self.grid[r][c] = 0

        elif self.edit_mode == "start":
            if (r, c) != self.goal and self.grid[r][c] == 0:
                self.start = (r, c)
                self.agent_pos = self.start

        elif self.edit_mode == "goal":
            if (r, c) != self.start and self.grid[r][c] == 0:
                self.goal = (r, c)

        self.draw_grid()


    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Random Map",
                  command=self.random_map).pack(side=tk.LEFT)

        tk.Button(frame, text="Start Search",
                  command=self.start_search).pack(side=tk.LEFT)

        tk.Button(frame, text="Toggle Dynamic",
                  command=self.toggle_dynamic).pack(side=tk.LEFT)

        tk.Button(frame, text="Use GBFS",
                  command=lambda: self.set_algo("GBFS")).pack(side=tk.LEFT)

        tk.Button(frame, text="Use A*",
                  command=lambda: self.set_algo("A*")).pack(side=tk.LEFT)

        tk.Button(frame, text="Manhattan",
                  command=lambda: self.set_heuristic("Manhattan")).pack(side=tk.LEFT)

        tk.Button(frame, text="Euclidean",
                  command=lambda: self.set_heuristic("Euclidean")).pack(side=tk.LEFT)

        tk.Button(frame, text="Set Start",
                  command=lambda: self.set_mode("start")).pack(side=tk.LEFT)

        tk.Button(frame, text="Set Goal",
                  command=lambda: self.set_mode("goal")).pack(side=tk.LEFT)

        tk.Button(frame, text="Draw Walls",
                  command=lambda: self.set_mode("wall")).pack(side=tk.LEFT)


    def set_algo(self, algo):
        self.algorithm = algo
        self.info.config(text="Algorithm: " + algo)

    def set_heuristic(self, h):
        self.heuristic_type = h
        self.info.config(text="Heuristic: " + h)

    def toggle_dynamic(self):
        self.dynamic_mode = not self.dynamic_mode
        self.info.config(text="Dynamic Mode: " + str(self.dynamic_mode))

    def set_mode(self, mode):
        self.edit_mode = mode
        self.info.config(text="Edit Mode: " + mode)
