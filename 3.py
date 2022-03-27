def lengthOfLongestSubstring(s: str) -> int:

    mydict = {}
    st =0
    end =0
    maxs = ""
    curs = ""
    for i, v in enumerate(s):
        curs = curs+i
        if i in mydict:
            mydict[i]
        else:
            mydict[i] = v



str = "pwwkew"

assert lengthOfLongestSubstring(str) == "wke"