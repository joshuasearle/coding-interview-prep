class AbstractHeap(object):
    """
    Stores the min item at root
    """
    def __init__(self):
        self.array = []
        self.length = 0
    
    def __len__(self): return len(self.array)
    
    def parent_index(self, i): return (i - 1) // 2
    
    def left_index(self, i): return 2 * i + 1

    def right_index(self, i): return 2 * i + 2

    def parent(self, i): return self.array[self.parent_index(i)]
    
    def left(self, i): return self.array[self.left_index(i)]

    def right(self, i): return self.array[self.right_index(i)]

    def has_parent(self, i): return self.parent_index(i) >= 0

    def has_left(self, i): return self.left_index(i) < len(self)

    def has_right(self, i): return self.right_index(i) < len(self)
    
    def swap(self, i1, i2):
        tmp = self.array[i1]
        self.array[i1] = self.array[i2]
        self.array[i2] = tmp
    
    def peek(self):
        if len(self) == 0: raise IndexError()
        return self.array[0]

    def poll(self):
        if len(self) == 0: raise IndexError()
        item = self.array[0]
        # Swap last in first, then remove last
        self.array[0] = self.array[len(self) - 1]
        self.array.pop()
        self.heapify_down()
        return item
    
    def add(self, value):
        self.array.append(value)
        self.heapify_up()
    
    def heapify_up(self):
        raise NotImplementedError()

    def heapify_down(self):
        raise NotImplementedError()