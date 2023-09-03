import math
""" 
Sequential Search:
 In this, the list or array is traversed sequentially and every element is checked. 
"""



def main():
    global steps
    steps = 0
    numbers = [number for number in range(26)]
    
    target = 9
    result = binary_search(arr=numbers, target=target)
    print(f"steps: {steps}, {target == result}")


def binary_search(arr:list, target:int, beforIndex=0) -> int:
    """ 
    """
    global steps
    startIndex = round((len(arr)) / 2)
    print("Array: ",arr,"index: ", startIndex)
    
    if len(arr) == 1:
        if arr[-1] == target:
            steps += 1
            return target
        else:
            return -1

    if arr[startIndex] < target:
        steps += 1
        return binary_search(arr=arr[startIndex:], target=target)
    elif arr[startIndex] > target:
        steps += 1
        return binary_search(arr=arr[:startIndex], target=target)
    elif arr[startIndex] == target:
        steps += 1
        return target 
    else:
        return -1



def test_ok():
    ...    

if __name__ == "__main__":
    main()

