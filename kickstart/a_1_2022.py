# At least 7 characters.
# At least one uppercase English alphabet letter.
# At least one lowercase English alphabet letter.
# At least one digit.
# At least one special character. There are four special characters: #, @, *, and &.

def new_password(string, n):
    
    specials =  ["#","@", "*","&"]
    upper=False
    lower=False
    digit=False
    special=False
    # letters, digits, and special characters
    for char in string:
        if char.isupper():
            upper=True
        if char in specials:
            special=True
        if char.islower():
            lower=True
        if char.isdigit():
            digit=True
    newstring=string
    if not lower:
        newstring= string +"a"
    if not upper:
        newstring=newstring+"A"
    if not digit:
        newstring =newstring+"1"
    if not special:
        newstring =newstring+"@"

    while len(newstring) <7:
        newstring =newstring+"@"
    return newstring




if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):                 
    string_len = input()
    string = input()
    h_index_scores = new_password(string, string_len)
    print("Case #" + str(test_case) + ": " +(str(h_index_scores)))
