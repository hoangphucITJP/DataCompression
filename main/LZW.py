def LZW_func(Str):
    # ----------------frequency of each character----------

    my_dict = []

    for i in Str:
        if i not in my_dict:
            my_dict += [i]

    my_dict.sort()
    ori_dict = list(my_dict)

    # ----------------LZW------------
    P = ""
    result = []
    for i in Str:
        C = i
        if P + C in my_dict:
            P = P + C
        else:
            result.append(my_dict.index(P) + 1)
            my_dict += [P + C]
            P = C

    result.append(my_dict.index(P) + 1)


    print(result)
    dictX = ori_dict
    Ret = [None, None]
    Ret[0] = dictX
    Ret[1] = result
    return Ret
