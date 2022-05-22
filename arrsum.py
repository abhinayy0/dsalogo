

def arr_sum(arr):

    start = 0
    end = len(arr)

    curr_sum = arr[start]
    sum_now = 0
    start = start + 1

    while start < end:

        sum_now = sum_now + arr[start]
        if sum_now > 0:
            curr_sum = sum_now
        else:
            sum_now = 0

        start = start + 1
    print(curr_sum)
    return curr_sum

# assert arr_sum([-2 ,1 ,-3 ,4, -1 ,2, 1, -5, 4])==6

print(sum([ 4, -1, 2, 1]))