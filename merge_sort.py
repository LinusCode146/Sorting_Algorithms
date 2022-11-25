from typing import List


def merge_sort(unsorted_list: List[int or float]) -> List[int or float]:
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and divide the unsorted list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            del left_half[0]
        else:
            res.append(right_half[0])
            del right_half[0]
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


if __name__ == "__main__":
    pass