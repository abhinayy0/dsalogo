# Alan and Barbara suddenly felt like playing with numbers. 
# Alan chooses a non-empty subset from the set of first N positive 
# integers (1,2,…,N). Barbara takes the rest of the numbers (if any)
#  from the set. And then they both calculate the sum of the elements 
#  in their respective sets.

# Alan believes in a magic ratio, which is X:Y. Hence, 
# Alan wants to choose the subset in such a way that the ratio
#  between the sum of Alan's subset and the sum of Barbara's subset is exactly X:Y.
# 3 1 2
# 1 2 3 
import math

from itertools import combinations
  
def subsetSum(li, comb, sums):
    # Iterating through all subsets of
    # list li from length 0 to length of li:
    for i in range(len(li)+1):
        for subset in combinations(li, i):
              
            # Storing all the subsets in list comb:
            comb.append(list(subset))
              
            # Storing the subset sums in list sums:
            sums.append(sum(subset))
  
  
def calcSubsets(n, arr, x):
    
    # Dividing the list arr into two lists
    # arr1 and arr2 of about equal sizes
    # by slicing list arr about index n//2:
    arr1, arr2 = arr[:n//2], arr[n//2:]
      
    # Creating empty lists comb1 and sums1
    # to run the subsetSum function and
    # store subsets of arr1 in comb1
    # and the subset sums in sums1:
    comb1, sums1 = [], []
    subsetSum(arr1, comb1, sums1)
      
    # Creating empty lists comb2 and sums2
    # to run the subsetSum function and
    # store subsets of arr2 in comb2
    # and the subset sums in sums2:
    comb2, sums2 = [], []
    subsetSum(arr2, comb2, sums2)
      
    # Iterating i through the indices of sums1:
    ans =[]
    for i in range(len(sums1)):
          
        # Iterating j through the indices of sums2:
        for j in range(len(sums2)):
              
            # If two elements (one from sums1
            # and one from sums2) add up to x,
            # the combined list of elements from
            # corresponding subsets at index i in comb1
            # and j in comb2 gives us the required answer:
            if sums1[i] + sums2[j] == x:
                ans.append(comb1[i] + comb2[j])
    return ans


def range_partition(N,X,Y):
    sum_n = (N*(N+1))//2
    if X+Y>sum_n:
        return "IMPOSSIBLE", ""
    num=math.gcd(X,Y)
    if sum_n % (X+Y) != 0:
        return "IMPOSSIBLE", ""
    arr = [i for i in range(1,N+1) ]
    val=2
    origX, origY = X,Y
    while X+Y <=sum_n:
        arr1 = calcSubsets(N, arr,X)
        arr2 = calcSubsets(N, arr,Y)
        for row in arr1:
            set1 = set(row)
            for row2 in arr2:
                set2 = set(row2)
                if set1.intersection(set2) == set():
                    return "POSSIBLE", set2
        X = origX * val
        Y = origY * val
        val+=1
    return "IMPOSSIBLE", ""



if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):     
    N,X, Y= map(int, input().split())             
    h_index_scores , vals= range_partition(N,X,Y)
    if h_index_scores =="IMPOSSIBLE":
        print("Case #" + str(test_case) + ": " +(str(h_index_scores)))
    else:
        print("Case #" + str(test_case) + ": " +(str(h_index_scores)))
        print(len(vals))
        for i in vals:
            print(i, end=" ")
        print()

