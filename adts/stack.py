class StackNode(object):
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev


class Stack(object):
    def __init__(self):
        self.top = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def push(self, value):
        node_to_push = StackNode(value, self.top)
        self.top = node_to_push
        self.length +=1 
    
    def pop(self):
        if self.top is None: raise IndexError()
        value = self.top.value
        self.top = self.top.prev
        self.length -= 1
        return value
    
    def peek(self):
        if self.top is None: raise IndexError()
        return self.top.value


