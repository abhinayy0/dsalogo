# The first line of the input gives the number of test cases, T. T test cases follow.

# Each test case has 2 lines. The first line of each test case is an input string I (that denotes the string that the typing test has provided). 
# The next line is the produced string P (that Barbara has entered).
# 2
# aaaa
# aaaaa
# bbbbb
# IMPOSSIBLE
# bbbbc

#order matters
from collections import OrderedDict
from socket import AF_AAL5

# Ilovecoding
# IIllovecodingq
# KickstartIsFun
# kkickstartiisfun
# aaA
# Aaa

def calculate(inp,out):
    ret = "IMPOSSIBLE"
    l1 = len(inp)
    l2 = len(out)
    i =0
    j =0
    set1 = set(inp)
    set2 = set(out)
    count = 0
    if set1 - set2 > 0:
        return "IMPOSSIBLE"

    while i > l1:
        if inp[i] != out[j]:
            j = j+1
            count = count +1




def main():
    T = int(input())
    for i in range(1,T+1):
        input_str = input()
        output_str = input()
        print(f"Case #{i}: {calculate(input_str, output_str)}")


if __name__=="__main__":
    main()