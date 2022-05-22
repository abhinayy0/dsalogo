__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"
__question__="Rotate the array"

"""
Write a program to cyclically rotate an array by one.
"""

def rotate( arr, n):
    """Rotate last element of array

    Args:
        arr ([type]): [description]
        n ([type]): [description]

    Returns:
        List: Rotated array
    """
    i = n-1
    while i > 0:
        arr[i], arr[i-1] = arr[i-1], arr[i]
        i = i - 1
    return arr

rotate([1,2], 2)