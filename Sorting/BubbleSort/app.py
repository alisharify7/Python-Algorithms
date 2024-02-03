"""Sorts a list of numbers in ascending order using the bubble sort algorithm."""


def bubble_sort(base_arr: list):
    for i in range(len(base_arr)):
        is_swap = False
        for j in range(len(base_arr) - 1, i, -1):
            if j > 0 and base_arr[j] < base_arr[j - 1]:
                base_arr[j], base_arr[j - 1] = base_arr[j - 1], base_arr[j]
                is_swap = True
        if not is_swap:
            break


def main():
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    bubble_sort(array)


if __name__ == "__main__":
    main()
