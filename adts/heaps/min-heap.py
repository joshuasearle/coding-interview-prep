from heap import AbstractHeap

class MinHeap(AbstractHeap):
    """
    Stores the min item at root
    """    
    def heapify_up(self):
        current_index = len(self) - 1
        while self.has_parent(current_index) and self.parent(current_index) > self.array[current_index]:
            self.swap(self.parent_index(current_index), current_index)
            current_index = self.parent_index(current_index)
    
    def heapify_down(self):
        current_index = 0
        while self.has_left(current_index):
            smaller_child_index = self.left_index(current_index)
            if self.has_right(current_index and self.right(current_index) < self.left(current_index)):
                smaller_child_index = self.right_index(current_index)
            if self.array[current_index] < self.array[smaller_child_index]:
                break
            self.swap(current_index, smaller_child_index)
            current_index = smaller_child_index
 