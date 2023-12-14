class Stack:
    def __init__(self, items=None, limit=100):
        self.items = [] if items is None else items
        self.limit = limit

    def push(self, item):
        if self.full():
            # raise Exception("Cannot add item, stack is full")
            return None
        self.items.append(item)

    def pop(self):
        return None if self.isEmpty() else self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):  # renamed from 'empty' to 'isEmpty'
        return len(self.items) == 0

    def full(self):
        return (len(self.items) >= self.limit)

    def search(self, value):
        if value in self.items:
            return len(self.items) - self.items.index(value) - 1
        else:
            return -1
