import string
digit_2_letter = {}

count = 1
digit = 2
for letter in string.ascii_lowercase:
    
    

    if digit in digit_2_letter:
        digit_2_letter[digit].append(letter)
    else:
        digit_2_letter[digit] = [letter]
    if count %3 == 0:
        if digit in [7 , 9]:
            if count %4 == 0:
                digit+=1
        else:
            digit+=1
        
    count+=1
print(digit_2_letter)