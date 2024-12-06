class WorkQueue:
    def __init__(self):
        self.queue = []

    def put(self, node):
        """
        Adds a node to the end of the queue.
        """
        self.queue.append(node)

    def get(self):
        """
        Removes and returns the node from the front of the queue.
        Raises an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot get from an empty queue.")
        return self.queue.pop(0)  # Remove the first element (O(n))

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        """
        return len(self.queue) == 0

    def clear(self):
        """
        Clears all elements from the queue.
        """
        self.queue = []  # Reinitialize as an empty list

