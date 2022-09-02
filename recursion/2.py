# Use the following mathematical identity to solve this problem: (n-1)^2 = n^2 - 2n + 1(n−1)
# ​2
# ​​ =n
# ​2
# ​​ −2n+1.

def testSq(n):
    if n <=0:
        return 0
    
    return testSq(n-1)  + 2*n - 1

print(testSq(5))