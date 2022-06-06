__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"
__question__ = "Reverse the array"

from typing import List


def arr_rev(arr: List):
    """Reverse given list

    Args:
        arr (List): List that needs to be reversed

    Returns:
        Reversed list
    """

    index = 0
    end = len(arr) - 1
    while index < end:
        arr[index], arr[end] = arr[end], arr[index]
        index = index + 1
        end = end - 1

    return arr


assert arr_rev([1, 2, 3, 4]) == [4, 3, 2, 1]  # even length array

assert arr_rev([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]  # odd length array

assert arr_rev([1, 0, 3, 4, 0]) == [0, 4, 3, 0, 1]  # random test

assert arr_rev([1]) == [1]  # one element

assert arr_rev([]) == []  # empty element
