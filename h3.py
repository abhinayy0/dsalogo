# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

def fun(arr, k):

    window_start = 0
    myset = set()
    max_len =0

    for window_end in range(len(arr)):
        myset.add(arr[window_end])
        while len(myset) > k:
            myset.remove(arr[window_start])
            window_start +=1
        
        max_len = max(max_len, window_end- window_start+1)
    return max_len

print(fun("araaci", 2))

