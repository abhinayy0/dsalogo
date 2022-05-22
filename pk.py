from typing import List
def twoSum( nums: List[int], target: int) -> List[int]:
    mydict = {}
    
    for i, v in enumerate(nums):
        print("i", i, " v ", v)
        diff = target - v
        if diff in mydict:
            return [mydict[diff], i]
        mydict[diff] =i
    return
                
A=[2,7,11,15]
B=9
z=twoSum(A,B)
print(z)