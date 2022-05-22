# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

def fun(n, k):
    
    window_start = 0
    window_sum=0
    sub_arr_size = float("inf")

    for window_end in range(len(n)):
        window_sum += n[window_end]
        while window_sum >= k:
            sub_arr_size = min(sub_arr_size, window_end -window_start +1)
            window_sum -= n[window_start]
            window_start+=1
        
    if sub_arr_size == float("inf"):
        return 0
    return sub_arr_size






n=[1,1,1,1,1,1]
S=11
print(fun(n,S))