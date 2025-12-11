class HeapSort:
    @staticmethod
    def __swap(arr: list, left: int, right: int):
        arr[left], arr[right] = arr[right], arr[left]

    @staticmethod
    def __min_heapify(arr: list, ind: int, size: int):
        left = (ind << 1) + 1
        right = (ind << 1) + 2
        smallest = ind
        if left < size and arr[left] < arr[smallest]:
            smallest = left
        if right < size and arr[right] < arr[smallest]:
            smallest = right
        if smallest != ind:
            HeapSort.__swap(arr, smallest, ind)
            HeapSort.__min_heapify(arr, smallest, size)

    @staticmethod
    def __max_heapify(arr: list, index: int, size: int):
        left = (index << 1) + 1
        right = (index << 1) + 2
        largest = index
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        if index != largest:
            HeapSort.__swap(arr, largest, index)
            HeapSort.__max_heapify(arr, largest, size)

    @staticmethod
    def build_max_heap(arr: list):
        size = len(arr)
        mid = (size >> 1)
        for i in range(mid, -1, -1):
            HeapSort.__max_heapify(arr, i, size)

    @staticmethod
    def build_min_heap(arr: list):
        size = len(arr)
        mid = (size >> 1)
        for i in range(mid, -1, -1):
            HeapSort.__min_heapify(arr, i, size)

    @staticmethod
    def heap_sort(arr: list):
        size = len(arr)
        HeapSort.build_max_heap(arr)
        for i in range(size - 1, 0, -1):
            HeapSort.__swap(arr, 0, i)
            HeapSort.__max_heapify(arr, 0, i)

    @staticmethod
    def heap_sort_desc(arr: list):
        size = len(arr)
        HeapSort.build_min_heap(arr)
        for i in range(size -1, 0, -1):
            HeapSort.__swap(arr, 0, i)
            HeapSort.__min_heapify(arr, 0, i)


if __name__ == "__main__":
    arr = [4, 1, 7, 2, 24, 23, 8, 3]
    HeapSort.build_max_heap(arr)
    print("Max Heap: ",arr)
    arr = [4, 1, 7, 2, 24, 23, 8, 3]
    HeapSort.heap_sort(arr)
    print("Sorted Ascending: ", arr)

    arr = [4, 1, 7, 2, 24, 23, 8, 3]
    HeapSort.build_min_heap(arr)
    print("Min Heap: ",arr)
    HeapSort.heap_sort_desc(arr)
    print("Sorted Descending: ", arr)


