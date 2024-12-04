class Node:
    def __init__(self, row: int, col: int, blocked: bool = False):
        self.row = row
        self.col = col
        self.blocked = blocked
        self.distance = float('inf')  # For pathfinding
        self.previous = None  # Previous node in shortest path
        self.neighbors = []  # Neighboring nodes

    def add_neighbor(self, neighbor: "Node"):
        if not neighbor.blocked:
            self.neighbors.append(neighbor)
