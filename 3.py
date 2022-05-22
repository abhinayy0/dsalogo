# 3
# 5
# 33
2
# 12121
#   12921
#   129212
#   122921
#   121212

def sod(num):

    prod = 1
    sum = 0

    for i in str(num):
        if int(i)==0:
            return True
        prod = prod * int(i)
        sum = sum + int(i)
    if prod % sum == 0:
        return True
    return False

def calculate(num):
    count = 0
    for i in range(num[0], num[1]+1):
        if sod(i):
            count = count +1
    
    return count


def main():
    T = int(input())
    for i in range(1,T+1):
        all_nums = map(int, input().split())
        print(f"Case #{i}: {calculate(all_nums)}")


if __name__=="__main__":
    main()

#     4
# 1 9
# 91 99
# 451 460
# 501 1000
