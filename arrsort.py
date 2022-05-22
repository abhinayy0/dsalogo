__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"

from typing import List

"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
"""

def arr_sort(arr: List):
    """Function to sort array of 0s,1s and 2s

    Args:
        arr (List): [description]

    Returns:
        [type]: [description]
    """
    arr_map = {}

    for i in arr:
        arr_map[i] = arr_map.get(i, 0) + 1
    zero_index = arr_map[0]
    one_index = arr_map[1] + arr_map[0]
    size = len(arr)
    i=0
    while i < size:
        if i < zero_index:
            arr[i] = 0
        elif i < one_index:
            arr[i] = 1
        else:
            arr[i] = 2
        i = i+1
    return arr



assert arr_sort([1,0,0,0,2,0,2,2,2,1,0,1,1,1,1]) ==sorted([1,0,0,0,2,0,2,2,2,1,0,1,1,1,1])
