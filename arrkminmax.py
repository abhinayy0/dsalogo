__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"
__question__="Find kth min and max in array"

"""
Given an array arr[] and an integer K where K is smaller than size of array, the task is to
 find the Kth smallest element in the given array. It is given that all array elements are distinct.
"""


from typing import List

def arr_kmin_max(arr: List, k: int):
    """[summary]

    Args:
        arr (List): [description]
        k (int): [description]

    Returns:
        [type]: [description]
    """
    if len(arr) <=0:
        return []
    
    arr_min = [arr[0]] * k
    arr_max = [arr[0]] * k
    
    print(arr_min)
    print(arr_max)
    for ele in arr:
        if arr_min[k-1] > ele:
            arr_min.pop(0)
            arr_min.append(ele)
        if arr_max[k-1] < ele:
            arr_max.pop(0)
            arr_max.append(ele)
    
    return [arr_min], [arr_max]



d=arr_kmin_max([1,26,77,9,98,3,4,5],2)
print(d)