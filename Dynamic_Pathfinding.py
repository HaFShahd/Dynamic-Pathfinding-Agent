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

        tk.Label(frame, text="Rows:").pack(side=tk.LEFT)
        self.rows_var = tk.StringVar(value=str(self.rows))
        tk.Entry(frame, textvariable=self.rows_var, width=5).pack(side=tk.LEFT)

        tk.Label(frame, text="Cols:").pack(side=tk.LEFT)
        self.cols_var = tk.StringVar(value=str(self.cols))
        tk.Entry(frame, textvariable=self.cols_var, width=5).pack(side=tk.LEFT)

        tk.Label(frame, text="Density %:").pack(side=tk.LEFT)
        self.density_var = tk.StringVar(value="30")
        tk.Entry(frame, textvariable=self.density_var, width=5).pack(side=tk.LEFT)

        tk.Button(frame, text="Random Map", command=self.random_map_user).pack(side=tk.LEFT)
        tk.Button(frame, text="Start Search", command=self.start_search).pack(side=tk.LEFT)
        tk.Button(frame, text="Toggle Dynamic", command=self.toggle_dynamic).pack(side=tk.LEFT)
        tk.Button(frame, text="Use GBFS", command=lambda: self.set_algo("GBFS")).pack(side=tk.LEFT)
        tk.Button(frame, text="Use A*", command=lambda: self.set_algo("A*")).pack(side=tk.LEFT)
        tk.Button(frame, text="Manhattan", command=lambda: self.set_heuristic("Manhattan")).pack(side=tk.LEFT)
        tk.Button(frame, text="Euclidean", command=lambda: self.set_heuristic("Euclidean")).pack(side=tk.LEFT)
        tk.Button(frame, text="Set Start", command=lambda: self.set_mode("start")).pack(side=tk.LEFT)
        tk.Button(frame, text="Set Goal", command=lambda: self.set_mode("goal")).pack(side=tk.LEFT)
        tk.Button(frame, text="Draw Walls", command=lambda: self.set_mode("wall")).pack(side=tk.LEFT)

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


    def random_map_user(self):
        try:
            rows = int(self.rows_var.get())
            cols = int(self.cols_var.get())
            density = float(self.density_var.get()) / 100.0
            if rows <= 0 or cols <= 0 or not (0 <= density <= 1):
                raise ValueError
        except ValueError:
            self.info.config(text="Invalid input! Rows, Cols > 0, Density 0-100.")
            return

        self.rows = rows
        self.cols = cols
        self.start = (0, 0)
        self.goal = (rows - 1, cols - 1)
        self.agent_pos = self.start
        self.grid = [[0 for i in range(cols)] for i in range(rows)]

        # Resize canvas
        self.canvas.config(width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE)

        # Fill random obstacles
        for r in range(rows):
            for c in range(cols):
                if (r, c) != self.start and (r, c) != self.goal:
                    if random.random() < density:
                        self.grid[r][c] = 1

        self.draw_grid()
        self.info.config(text=f"Random map {rows}x{cols}, density {density*100:.0f}%")
    def heuristic(self, a, b):
        if self.heuristic_type == "Euclidean":
            return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        else:
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def neighbors(self, r, c):
        result = []

        if r+1 < self.rows and self.grid[r+1][c] == 0:
            result.append((r+1, c))
        if r-1 >= 0 and self.grid[r-1][c] == 0:
            result.append((r-1, c))
        if c+1 < self.cols and self.grid[r][c+1] == 0:
            result.append((r, c+1))
        if c-1 >= 0 and self.grid[r][c-1] == 0:
            result.append((r, c-1))

        return result

    # ================= SEARCH =================
    def search(self, start_pos):
        start_time = time.time()

        nodes = {}
        open_list = []
        visited = set()

        def get_node(pos):
            if pos not in nodes:
                nodes[pos] = Node(pos[0], pos[1])
            return nodes[pos]

        start_node = get_node(start_pos)
        start_node.g = 0
        start_node.h = self.heuristic(start_pos, self.goal)

        if self.algorithm == "GBFS":
            start_node.f = start_node.h
        else:
            start_node.f = start_node.g + start_node.h

        heapq.heappush(open_list, start_node)

        while len(open_list) > 0:
            current = heapq.heappop(open_list)
            pos = (current.r, current.c)

            if pos in visited:
                continue
            visited.add(pos)

            if pos != self.start and pos != self.goal:
                self.color_cell(pos, "blue")

            if pos == self.goal:
                path = []
                temp = current
                while temp is not None:
                    path.insert(0, (temp.r, temp.c))
                    temp = temp.parent

                exec_time = (time.time() - start_time) * 1000
                return path, len(visited), exec_time

            nbrs = self.neighbors(current.r, current.c)

            i = 0
            while i < len(nbrs):
                nbr = nbrs[i]
                neighbor = get_node(nbr)

                tentative_g = current.g + 1

                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(nbr, self.goal)
                    neighbor.parent = current

                    if self.algorithm == "GBFS":
                        neighbor.f = neighbor.h
                    else:
                        neighbor.f = neighbor.g + neighbor.h

                    heapq.heappush(open_list, neighbor)

                    if nbr != self.start and nbr != self.goal:
                        self.color_cell(nbr, "yellow")

                i += 1

            self.root.update()
            time.sleep(0.01)

        return None, len(visited), 0

    def color_cell(self, pos, color):
        r = pos[0]
        c = pos[1]
        self.canvas.create_rectangle(
            c * CELL_SIZE, r * CELL_SIZE,
            (c + 1) * CELL_SIZE, (r + 1) * CELL_SIZE,
            fill=color, outline="gray"
        )
