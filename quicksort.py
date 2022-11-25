from typing import List


def quicksort(n: List[int or float]) -> List[int or float]:
    if len(n) < 2: return n
    pivot = n.pop()
    return quicksort([i for i in n if i <= pivot]) + [pivot] + quicksort([i for i in n if i > pivot])


if __name__ == "__main__":
    pass