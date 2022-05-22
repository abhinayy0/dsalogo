def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    i=0
    print(len(matrix))
    while i < len(matrix):
        j=0
        while j < len(matrix[0]):
            print(matrix[i][j])
            
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
                print("******")
            j+=1
        i+=1
    
    i=0
        
    while i < len(matrix):
        j=0
        while j < len(matrix[0]):
            if i in rows:
                matrix[i][j] =0
            if j in cols:
                matrix[i][j] =0
            j+=1
        i+=1

    print("rows set", rows)
    print("cols set", cols)
    return matrix

def printmat(z):

    for row in z:
        for ele in row:
            print(ele,end=" ")
        print()
z=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# printmat(z)
print()
# setZeroes(z)
printmat(setZeroes(z))