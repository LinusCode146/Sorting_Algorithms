from typing import List

def insertion_sort(n: List[int or float]) -> List[int or float]:
    for i in range(1, len(n)):
        while n[i - 1] > n[i] and i > 0:
            n[i], n[i - 1] = n[i - 1], n[i]
            i -= 1
    return n


if __name__ == "__main__":
    pass

