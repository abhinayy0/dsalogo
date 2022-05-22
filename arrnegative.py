__author__ = "Abhinay Yadav"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Abhinay Yadav"
__email__ = "abhinayy0@gamil.com"
__status__ = "Development"

from typing import List

"""
Move all the negative elements to one side of the array 
"""

def arr_negative(arr: List):
    """[summary]

    Args:
        arr (List): [description]

    Returns:
        [type]: [description]
    """

    start_index = 0
    end_index = len(arr) -1
    count= 0
    while start_index <= end_index:
        count= count +1
        if arr[start_index] < 0 and arr[end_index] < 0:
            start_index = start_index + 1
           
        elif arr[start_index] >0 and arr[end_index] < 0:
            arr[start_index], arr[end_index] =  arr[end_index], arr[start_index]
            start_index = start_index + 1 
            end_index = end_index - 1
        
        elif arr[start_index] > 0  and arr[end_index] > 0:
            end_index = end_index - 1

        else:
            start_index = start_index + 1
            end_index = end_index - 1
    print(count)
    print(arr)
    return arr


assert arr_negative([-1,1,2,3,-1,-2,3,4,2,-5]) == [2,1,2,3,4,3,-2,-1,-1,-5]



