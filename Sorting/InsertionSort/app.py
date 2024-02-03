

"""

"""


def insertion_sort(base_arr: list):
    for k in range(1, len(base_arr)):
        item = base_arr[k]
        i = k
        while i > 0 and item < base_arr[i - 1] :
            base_arr[i] = base_arr[i-1]
            i -= 1
            base_arr[i] = item

def main():
    # random.randint(1, 1)
    array = [10,9,8,7,6,5,4,3,2,1]
    insertion_sort(array)
    print(array)


if __name__ ==  "__main__":
    main()

