class QueueNode(object):
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def enqueue(self, value):
        new_head = QueueNode(value, self.head, None)
        if self.head is None:
            self.tail = new_head
        else:
            self.head.prev = new_head
        self.head = new_head
        self.length += 1

    def dequeue(self):
        if self.tail is None: raise Exception()
        value = self.tail.value
        # If one node
        if self.tail.prev is None:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return value
    
    def __str__(self):
        current = self.head
        output = []
        while current is not None:
            output.append(current.value)
            current = current.next
        return str(' -> '.join(list(map(str, output))))
    
    def __repr__(self):
        return str(self)

