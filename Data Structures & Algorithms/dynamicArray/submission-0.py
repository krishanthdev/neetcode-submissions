class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.new_array = [None] * self.capacity


    def get(self, i: int) -> int:
        return self.new_array[i]


    def set(self, i: int, n: int) -> None:
        self.new_array[i] = n

    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize()

        self.new_array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        
        self.size -= 1
        return self.new_array[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        temp_array = [0] * self.capacity
        for i in range(self.size):
            temp_array[i] = self.new_array[i]
        self.new_array = temp_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:

        return self.capacity
