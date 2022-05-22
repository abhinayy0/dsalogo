def minJumps( arr, n):
    #code here
    
    i =0 
    count = 0
    while i < n-1:
        # print("ele",arr[i])
        count = count +1
        # print("count", count)
        if arr[i] <= 0  :
            return -1
        
        if arr[i] >= n-1:
            return count
        
        i = i + arr[i]
        print(i)
        if i >=n-1:
            return count
    
    return count

# 2 1 1 2 2 1
qw= [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
z=minJumps(qw, len(qw))

print("len", len(qw))

# yz=[2, 3, 1, 1, 2, 4, 2, 0, 1, 1]


# q=minJumps(yz, len(yz))

print(z)
# print(q)