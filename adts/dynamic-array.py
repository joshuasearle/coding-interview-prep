class DynamicArray(object):
    """
    Array class that resizes dynamically.
    Will treat the python array as a static array.
    """
    initial_capacity = 8

    @staticmethod
    def generate_empty_array(n):
        return [None for _ in range(n)]

    def __init__(self):
        self.capacity = DynamicArray.initial_capacity
        self.array = DynamicArray.generate_empty_array(self.capacity)
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def full(self):
        return len(self) == self.capacity
    
    def double_capacity(self):
        new_capacity = self.capacity * 2
        longer_array = DynamicArray.generate_empty_array(new_capacity)
        for i in range(self.length):
            value = self.array[i]
            longer_array[i] = value
        self.array = longer_array
        self.capacity = new_capacity
    
    def halve_capacity(self):
        # Always multiple of two, so no edge case
        new_capacity = self.capacity // 2
        shorter_array = DynamicArray.generate_empty_array(new_capacity)
        for i in range(self.length):
            value = self.array[i]
            shorter_array[i] = value
        self.array = shorter_array
        self.capacity = new_capacity
    
    def swap(self, key1, key2):
        tmp = self.array[key1]
        self.array[key1] = self.array[key2]
        self.array[key2] = tmp

    def ensure_space(self):
        if self.full(): self.double_capacity()
    
    def remove_wasted_space(self):
        if self.capacity <= 2: return
        if self.capacity >= len(self) * 2: self.halve_capacity()

    def __setitem__(self, key, value):
        if key >= self.length: raise IndexError()
        self.ensure_space()
        self.array[key] = value
    
    def __getitem__(self, key):
        if key >= self.length: raise IndexError()
        return self.array[key]
    
    def append(self, value):
        self.ensure_space()
        self.array[len(self)] = value
        self.length += 1
    
    def pop(self):
        value = self.array[len(self) - 1]
        self.length -= 1
        self.remove_wasted_space()
        return value
    
    def remove(self, key):
        if key >= self.length: raise IndexError()
        value = self.array[key]
        # Swap the elements after the removed element down one
        for i in range(key + 1, len(self)):
            self.swap(i, i - 1)
        self.length -= 1
        self.remove_wasted_space()
        return value
    
    def __str__(self):
        # Using dynamic array just to have nice outputs
        output = []
        for i in range(len(self)):
            output.append(self.array[i])
        return str(output)
    
    def __repr__(self):
        return str(self)


x = DynamicArray()

for i in range(9):
    x.append(i)

print(x)

print(x.remove(3))

print(x)