# 3
# 1 3
# 3 4 3
# 1 3
# 3 0 0
# 3 3
# 0 0 0
# 0 2 0
# 0 0 0



def rabbit_house(grid, R,C):
    
    i =0
    while i <4:
        j=0
        while j<4:
            grid[i][j]
        grid[i][j]
        grid[i][j+1]
        grid[i+1][j]



if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):                 
    R, C= map(int, input().split()) 
    # grid=[[0 for i in range(C)] for j in range(R)]
    grid=[]
    
    for _ in  range(1, C):
        row = list(map(int, input().split()))
        grid.append(row)
    print(grid)
    out=rabbit_house(grid, R,C)
    print("Case #" + str(test_case) + ": " +(str(out)))
