from abc import ABC, abstractmethod

class Algorithm(ABC):
    @abstractmethod
    def calculate(self, data):
        pass

class BubbleSort(Algorithm):
    def calculate(self, data):
        for i in range(len(data)):
            for j in range(len(data) - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class QuickSort(Algorithm):
    def calculate(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.calculate(left) + middle + self.calculate(right)

class Strategy:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def execute(self, data):
        return self.algorithm.calculate(data)

if __name__ == "__main__":
    data = [5, 2, 8, 1, 9]
    bubble_sort = BubbleSort()
    quick_sort = QuickSort()
    bubble_sort_strategy = Strategy(bubble_sort)
    quick_sort_strategy = Strategy(quick_sort)
    print(bubble_sort_strategy.execute(data))
    print(quick_sort_strategy.execute(data))