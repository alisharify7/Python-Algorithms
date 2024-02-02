import os
import random

"""

"""


def insertion_sort(base_arr: list) -> bool:
    for k in range(1, len(base_arr)):
        item = base_arr[k]
        i = k
        print(i)
        while i > 0 and base_arr[i-1] > item:
            base_arr[i] = base_arr[i-1]
            i -= 1
            print(i, end=" ")
        base_arr[i] = item
        print()
        # print(base_arr)


def main():
    # random.randint(1, 1)
    array = [each for each in range(10, -1, -1)]
    print(array)
    insertion_sort(array)


if __name__ ==  "__main__":
    main()

