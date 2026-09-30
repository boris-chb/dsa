class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check if full then resize to capacity * 2
        if self.size == self.capacity:
            self.resize()
        # otherwise just add
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        target = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return target

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newArr = [0] * newCapacity
        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr
        self.capacity = newCapacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


if __name__ == "__main__":
    dd = DynamicArray(10)
    print(dd.arr)
    for i in range(25):
        dd.pushback(i)
        print(dd.arr)
