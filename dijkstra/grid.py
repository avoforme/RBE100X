from dijkstra.node import Node
# from node import Node
class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.nodes = [[Node(row, col) for col in range(cols)] for row in range(rows)]

    def get_node_at(self, position: tuple[int, int]) -> Node:
        row, col = position
        return self.nodes[row][col]

    def set_blocked(self, position: tuple[int, int], blocked: bool = True):
        node = self.get_node_at(position)
        node.blocked = blocked

    def reset(self):
        for row in self.nodes:
            for node in row:
                node.distance = float('inf')
                node.previous = None

    def connect_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                node = self.get_node_at((row, col))
                if not node.blocked:
                    # Add neighbors if within grid bounds
                    if row > 0:
                        node.add_neighbor(self.get_node_at((row - 1, col)))
                    if row < self.rows - 1:
                        node.add_neighbor(self.get_node_at((row + 1, col)))
                    if col > 0:
                        node.add_neighbor(self.get_node_at((row, col - 1)))
                    if col < self.cols - 1:
                        node.add_neighbor(self.get_node_at((row, col + 1)))

    def print(self):
        print("\n ", end='')
        for col in range(self.cols):
            print(f'{col:3}', end='')
        print('\n' + '-' * (4 * self.cols + 1))
        for row in range(self.rows):
            print(f'{row:2}| ', end='')
            for col in range(self.cols):
                n = self.get_node_at((row, col))
                if n.blocked:
                    print(f' X ', end='')
                else:
                    d = n.distance
                    print(f'{d:3}' if d < float('inf') else ' ∞ ', end='')
            print()
