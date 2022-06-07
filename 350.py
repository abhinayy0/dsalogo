def intersect(nums1, nums2):

    mydict = {}
    for i in nums1:
        mydict[i] = mydict.get(i, 0) + 1

    mydict2 = {}
    for i in nums2:
        mydict2[i] = mydict2.get(i, 0) + 1

    output = []
    for k, v in mydict2.items():
        myval = mydict.get(k, None)
        if myval:
            for i in range(min(v, myval)):
                output.append(k)

    print(output)


intersect([1, 2, 2, 1], [2, 2])
