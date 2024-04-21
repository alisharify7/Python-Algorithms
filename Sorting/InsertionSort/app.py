"""

"""


def InsertionSort1(base_arr: list):
    for k in range(1, len(base_arr)):
        item = base_arr[k]
        i = k
        while i > 0 and item < base_arr[i - 1]:
            base_arr[i] = base_arr[i - 1]
            i -= 1
            base_arr[i] = item

def InsertionSort2(array:list) -> None:
    length = len(array)
    for i in range(1, length):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j-=1



def InsertionSort3(array:list) -> None:
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                     array[j], array[j-1] = array[j-1], array[j]
                else:
                    break


def main():
    # random.randint(1, 1)
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    InsertionSort1(array)
    print(array)


if __name__ == "__main__":
    main()
