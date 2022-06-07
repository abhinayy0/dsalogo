# out=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
    [1]
   [1,1]
  [1,2,1]
0,1,3,3,1
1,4,6,4,1

00,01,02,03,04
10,11,12,12,14
20,21,22,23,24
30,31,32,33,34
40,41,42,43,44

41 = 31+32
42=32+33

ncr

n!
r!(n-r)!

4c2

2!

2! * 2!

row
col

row-1 C col-1

"""


def calcfact(n, r):
    res = 1
    rest = 1
    while r > 0:
        res = res * (n)
        rest = rest * (r)
        n = n - 1
        r = r - 1
    return res // rest


print(calcfact(4, 2))


z = 5

i, j = 0, 0
while i < 5:
    j = 0
    while j < 5:
        print("*", end="")
        j += 1
    print()
    i += 1


def getsol(numRows):

    res = [[1]]

    for _ in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


x = getsol(5)
print(x)
