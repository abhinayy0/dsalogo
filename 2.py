# 3
# 5
# 33
2
# 12121
#   12921
#   129212
#   122921
#   121212
1

0 

30789

12122

112122

121122

121221
def sod(num):

    sum = 0

    for i in str(num):
        sum = sum + int(i)
    return sum
def calculate(num):
    num_sum = sod(num)
   
    digit = num_sum % 9
    if digit == 0:
        x  = str(num)[0]
        y = str(num)[1:]
        new_num = x + str(0) + y
        return int(new_num)
    rem_digit = 9 - digit
    new_num = ""
    pos = 0
    if rem_digit == 0:
        x  = str(num)[0]
        y = str(num)[1:]
        new_num = x + str(rem_digit) + y
        return int(new_num)

    for char in (str(num)):
        if int(char) <= rem_digit:
            pos = pos+1
        else:
            break
              
    x = str(num)[:pos]
    y = str(num)[pos:]
    new_num = x + str(rem_digit) + y
    return int(new_num)

def main():
    T = int(input())
    for i in range(1,T+1):
        input_str = input()
        # input_str = 344565
        print(f"Case #{i}: {calculate(input_str)}")


if __name__=="__main__":
    main()