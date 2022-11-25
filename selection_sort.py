from typing import List

def selection_sort(n: List[int or float]) -> List[int or float]:
    sorted_list = []
    for _ in range(len(n)):
        sorted_list.append(min(n))
        n.remove(min(n))
    return sorted_list

if __name__ == "__main__":
    pass