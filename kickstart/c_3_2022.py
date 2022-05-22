
def fall_order(arr, N, L):

    new_arr=[0] *L

    for idx, row in enumerate(arr):
        p, d = row
        new_arr[p] ={idx: d}
        
    




if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):     
    N,L= map(int, input().split())
    arr=[]
    for _ in range(N):
        P, D = map(int, input().split())
        arr.append([P,D])

                 
    # h_index_scores , vals= range_partition(N,X,Y)
    # if h_index_scores =="IMPOSSIBLE":
    #     print("Case #" + str(test_case) + ": " +(str(h_index_scores)))