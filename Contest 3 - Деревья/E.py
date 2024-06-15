# E-Хипуй! Сортируй!

class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.size = len(arr)

    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

    def heap_sort(self):
        self.build_heap()
        for i in range(self.size - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.size -= 1
            self.heapify(0)


n = int(input())
arr = list(map(int, input().split()))

max_heap = Heap(arr)
max_heap.heap_sort()

print(" ".join(map(str, max_heap.heap)))
