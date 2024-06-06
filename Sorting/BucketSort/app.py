

def BucketSort(array: list[int]) -> None:
    sorted_array = [0] * (max(array)+1)

    for index, value in enumerate(array):
        sorted_array[value] += 1

    return sorted_array


def BucketSort1(array: list[int]) -> None:
    sorted_array = [0] * (max(array)+1)

    for index, value in enumerate(array):
        sorted_array[value] += 1

    array = []
    for index, value in enumerate(sorted_array):
        array.extend([index]*value)
        # for j in range(1,value+1):
        #     array.append(index)

    return array


A = [1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5]
A = BucketSort(A)
# A = BucketSort1(A)
print(A)
