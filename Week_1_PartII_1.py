class SortedArray:
    def __init__(self):
        self.array = []
    
    def get_array(self, length):
        self.array = []
        for i in range(length):
            element = int(input(f"Enter element {i+1}: "))
            self.array.append(element)
        self.array.sort()
        return self.array
sorted_array = SortedArray()
array_length = int(input("Enter length of array: "))
sorted_array.get_array(array_length)
print(sorted_array.array)