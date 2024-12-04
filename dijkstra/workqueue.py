from collections import deque

class WorkQueue:
    def __init__(self):
        self.queue = deque()

    def put(self, node):
        self.queue.append(node)

    def get(self):
        if self.is_empty():
            raise IndexError("Cannot get from an empty queue.")
        return self.queue.popleft()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def clear(self):
        self.queue.clear()
