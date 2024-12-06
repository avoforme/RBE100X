from grid import Grid
from workqueue import WorkQueue

class Dijkstra:
    def __init__(self, grid: Grid):
        self.grid = grid

    def compute(self, source: tuple[int, int]):
        self.grid.reset()
        source_node = self.grid.get_node_at(source)
        source_node.distance = 0

        queue = WorkQueue()
        for row in self.grid.nodes:
            for node in row:
                queue.put(node)

        while not queue.is_empty():
            current_node = min(queue.queue, key=lambda node: node.distance) # type: ignore
            queue.queue.remove(current_node)

            if current_node.distance == float('inf'):
                break

            for neighbor in current_node.neighbors:
                if neighbor in queue.queue:
                    alt = current_node.distance + 1
                    if alt < neighbor.distance:
                        neighbor.distance = alt
                        neighbor.previous = current_node

        distances = {(node.row, node.col): node.distance for row in self.grid.nodes for node in row}
        previous = {(node.row, node.col): (node.previous.row, node.previous.col) if node.previous else None for row in self.grid.nodes for node in row}
        return distances, previous
    
    def compute_path(self, source: tuple[int, int], destination: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Compute the shortest path from the source to the destination.
        
        :param source: The starting node as a tuple (row, col).
        :param destination: The destination node as a tuple (row, col).
        :return: A list of tuples representing the path from source to destination.
        """
        # Run Dijkstra's algorithm to compute distances and previous nodes
        self.compute(source)

        # Retrieve the destination node
        destination_node = self.grid.get_node_at(destination)

        # If the destination is unreachable, return an empty path
        if destination_node.distance == float('inf'):
            print(f"No path found from {source} to {destination}.")
            return []

        # Backtrack from the destination to the source to reconstruct the path
        path = []
        current = destination_node
        while current:
            path.append((current.row, current.col))
            current = current.previous

        # Reverse the path to start from the source
        path.reverse()

        # Print the path
        return path