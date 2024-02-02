import os
import random

"""
data should be discrete

data should be countable -> we should can be compare between data 
k = number of inputs
p = number of count-array (buckets)

rule: 
k >> p

"""



def pythonic_count_sort(base_arr:list) -> dict:
    """Count sorting algorithm , pythonic way"""
    counter = {}
    for each in base_arr:
        if each in counter:
            counter[each] += 1
        else:
            counter[each] = 1

    return counter
def count_sort(base_arr:list) -> list:
    """Count sorting algorithm """
    count_array = [0] * len(base_arr) # create new list with same length

    for each in base_arr: # iterate and increase base on index of values
        count_array[each] += 1

    return count_array



def main():
    array = [random.randint(1,1) for each in range(10)]
    print("before")
    print(array)

    print("after, normal count sort")
    count_array_value = count_sort(array)
    for index,value in enumerate(array):
        print(f"{index}: {value}")

    print("after, pythonic count sort")
    count_array_value = pythonic_count_sort(array)
    for each in count_array_value:
        print(f"{each}: {count_array_value[each]}")




if __name__ ==  "__main__":
    main()

