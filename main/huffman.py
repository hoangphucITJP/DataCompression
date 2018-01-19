import operator
from sympy import sympify


# ----------------frequency of each character----------

def huffman_func(Str):
    print('enter huffman')
    my_dict = {}
    element_dict = {i for i in my_dict}

    for i in Str:
        if not {i}.issubset(element_dict):
            my_dict[i] = 1
            element_dict.add(i)
        else:
            my_dict[i] += 1


        # Sort dictionary
        # --convert tu list tuple to sort
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))  # --convert again to dict
    my_dict = dict((x, y) for x, y in sorted_dict)

    # ----------------Build Tree------------
    element_mydict = [i for i in my_dict]
    while len(my_dict) > 1:
        if "[" in element_mydict[0]:
            tmp = [sympify(element_mydict[0])]
        else:
            tmp = [element_mydict[0]]
        if "[" in element_mydict[1]:
            tmp += [sympify(element_mydict[1])]
        else:
            tmp += [element_mydict[1]]

        my_dict[str(tmp)] = my_dict[element_mydict[0]] + my_dict[element_mydict[1]]
        element_mydict += [tmp]
        # remove the first two element
        my_dict.pop(element_mydict[0])
        my_dict.pop(element_mydict[1])
        # element_mydict.remove(element_mydict[0])
        # element_mydict.remove(element_mydict[0])

        # --Sort dictionary
        sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
        my_dict = dict((x, y) for x, y in sorted_dict)
        element_mydict = [i for i in my_dict]

    Tree = sympify(element_mydict[0])

    global dict_bin
    dict_bin = {}
    global tmp2
    tmp2 = ''

    # from tree return to dictionary binary
    def BinFunc(my_list):
        global dict_bin
        global tmp2
        for i in my_list:

            tmp3 = tmp2
            tmp2 += str(my_list.index(i))
            if type(i) is list:
                # tmp2 += str(my_list.index(i))
                BinFunc(i)
            else:
                # tmp3 = tmp2

                # tmp2 += str(my_list.index(i))
                dict_bin[str(i)] = tmp2
            tmp2 = tmp3
        return dict_bin

    dict_bin2 = BinFunc(Tree)

    result = ""
    for i in Str:
        result += dict_bin2[i]

    result += "!~!"
    result += str(Tree)
    print('Tree: ', Tree)
    return result  # return result and dictionary of result
