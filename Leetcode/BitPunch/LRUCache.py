from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.deque = deque()

    def get(self, key):
        if key in self.hashmap:
            # Move the accessed key to the end (most recently used)
            self.deque.remove(key)
            self.deque.append(key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.hashmap:
            # If key exists, remove it from deque to update position
            self.deque.remove(key)
        elif len(self.deque) == self.capacity:
            # If cache is full, remove the least recently used item
            oldest_item = self.deque.popleft()
            del self.hashmap[oldest_item]

        # Add the key to the deque and hashmap
        self.hashmap[key] = value
        self.deque.append(key)
