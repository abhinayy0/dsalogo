#subsets

def subsets(nums):
    all_sets = [[]]
    for ele in nums:
        n = len(all_sets)
        for i in range(n):

            temp_set = list(all_sets[i]) 
            temp_set.append(ele)
            all_sets.append(temp_set)
    print(all_sets)

subsets([1,2,3])