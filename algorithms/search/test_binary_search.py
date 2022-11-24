from binary_search_iteratively import binarySearch

def test_correct_index_found():
    array = [1,2,3,4,5,6,7,8,9]
    assert 5 == binarySearch(array=array,target = 6)

def test_target_not_in_array():
    array = [1,2,3,4,5,6,7,8,9]
    assert -1 == binarySearch(array=array, target = 10)


