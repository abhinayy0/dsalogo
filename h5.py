# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
from collections import Counter
def check_perm(str1, str2):
    letter_counter1 = Counter(str1)
    letter_counter2 = Counter(str2)
    print(letter_counter1)
    print(letter_counter2)
    for k,v in letter_counter1.items():
        if k not in letter_counter2 or v!= letter_counter2[k]:
            return False
    return True

def fun(arr, pat):

    window_start =0 
    K = len(pat)
    for window_end in range(len(arr)):

        if window_end >= K-1:
            print(window_end)
            if check_perm(arr[window_start:window_end+1], pat) == True:
                return True
            window_start +=1
    return False

print(fun("ab", "eidbaooo"))

# "ab"
# "eidbaooo"