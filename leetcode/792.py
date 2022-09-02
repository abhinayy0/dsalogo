def issubsequence(s, t):
    
    if len(t)  > len(s):
        return False
    
    i = 0
    j = 0
    
    while j < len(t) and i < len(s):
        
        if s[i] == t[j]:
            j+=1
        i+=1
    print(j, i)
    if j!= len(t):
        return False
    
    return True

print(issubsequence("abcdef", "bb"))