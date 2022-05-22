# 2
# 5 1
# ABCAA
# 4 2
# ABAA

def goodness_score(string, K):

    n = len(string)

    i =0
    j = n -1
    score=0
    case_change_possible =0

    while i < j:
        
        if string[i] != string[j]:
            score +=1
        i+=1
        j-=1
    if score==K:
        return 0
    
    return abs(score -K)


if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):                 
    n, K= map(int, input().split()) 
    string = input()
    h_index_scores = goodness_score(string, K)
    print("Case #" + str(test_case) + ": " +(str(h_index_scores)))
