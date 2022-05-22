def solve(A, B):
   
    prefix=[A[0]]
    suffix = [A[-1]]
    for i, v in enumerate(A[1:]):
        prefix.append(prefix[i]+v)
    newlst = A[::-1]
    for i, v in enumerate(newlst[1:]):
        suffix.append(suffix[i]+v)
    maxsum = 0
    N= len(A)-1
    for i in range(B):
        currsum = prefix[i] + suffix[N-(B-i)]
        if currsum > maxsum:
            maxsum= currsum
    print(prefix)
    print(suffix)
    print(maxsum)
    return maxsum

A = [5, -2, 3 , 1, 2]    
solve(A, 3)