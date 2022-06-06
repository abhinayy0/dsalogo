def lengthOfLongestSubstring(s: str) -> int:

    mydict = {}
    curs = ""
    for i, v in enumerate(s):
        curs = curs + i
        if i in mydict:
            mydict[i]
        else:
            mydict[i] = v


str = "pwwkew"

assert lengthOfLongestSubstring(str) == "wke"
