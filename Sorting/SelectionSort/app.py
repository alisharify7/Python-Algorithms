import random

a = [random.randint(0, 11000) for i in range(100)]

def SelectionSort(array:list) -> None:
    length = len(array)
    for index, value in enumerate(array):
        lowest_index = index
        find_least = False
        for j in range(index, length):
            if array[j] < array[lowest_index]:
                lowest_index = j
                find_least = True
        if find_least:
            array[index], array[lowest_index] = array[lowest_index], array[index]

print(a)
SelectionSort(a)
print(a)
