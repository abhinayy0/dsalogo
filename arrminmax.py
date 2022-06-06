__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"
__question__ = "Find min and max in array"

from typing import List


def arr_min_max(arr: List):
    """Find min and max element in arrray

    Args:
        arr (List): List from which min and max needs to be found

    Returns:
        list: List with first element as minimum and second as maximum
    """
    if len(arr) <= 0:
        return []

    arr_min = arr[0]
    arr_max = arr[0]

    for ele in arr:
        if arr_min > ele:
            arr_min = ele
        if arr_max < ele:
            arr_max = ele

    return [arr_min, arr_max]


assert arr_min_max([1, 2, 3, 4]) == [1, 4]  # even length array

assert arr_min_max([1, 2, 3, 4, 5]) == [1, 5]  # odd length array

assert arr_min_max([-1, 0, 3, 4, 0]) == [-1, 4]  # random test

assert arr_min_max([1]) == [1, 1]  # one element

assert arr_min_max([]) == []  # empty element
