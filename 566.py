from typing import List
def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:

    order_of_mat = len(mat) *len(mat[0]) 
    rows = len(mat)
    colm = len(mat[0])

    target_order = r*c
    

    if target_order != order_of_mat:
        print(mat)
        return mat
    output=[]

    i,j=0,0

    while i < rows:
        j=0
        while j<colm:
            output.append(mat[i][j])
            j+=1
        i=i+1

    i,j =0,0
    sec_output = [[0 for i in range(c)] for j in range(r)]
    while i< r:
        j=0
        while j< c:
            print(sec_output)
            sec_output[i][j] = output.pop(0)
            j+=1
        i+=1
    print(sec_output)

mat ,r,c= [[1,2],[3, 4]],  4, 1
result = [[1,2,3,4]]
matrixReshape(mat,r,c)