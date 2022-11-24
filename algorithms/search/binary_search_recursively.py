#O(log(n)) time | Olog(n) space where n is the size of array


def binarySearch(array,target):
    return binarySearchHelper(array,target,0,len(array-1))

def binarySearchHelper(array,target,left,right):
    if left > right:
        return -1
    middle = (right + left) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array,target,left,middle-1)
    else:
        return binarySearchHelper(array,target,right,middle+1)