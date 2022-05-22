def findMaxAverage( nums, k) -> float:
    
    max_avg, curr_sum, window_start =0.0, 0, 0
    for window_end  in range(len(nums)):
        
        curr_sum += nums[window_end]
        if window_end >= k-1:
            
            max_avg = max(max_avg, curr_sum/k)
            # print(f"sum {curr_sum}")
            curr_sum -= nums[window_start]
            window_start+=1
            # print(f"avg   {curr_avg}")
    print(max_avg)
    return max_avg

nums = [1,12,-5,-6,50,3]
k=4

findMaxAverage(nums,k)