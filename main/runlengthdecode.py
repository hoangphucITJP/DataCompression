def runlengthdecode_func(Str):
    t = iter(Str)
    Str = ' '.join(a+b for a,b in zip(t, t))

    Str += ' '
    n = 3
    tmp0 = [Str[i:i + n - 1] for i in range(0, len(Str), n)]
    print(tmp0)
    tmp0 = [i[1]*int(i[0]) for i in tmp0]
    tmp0 = ''.join(tmp0)
    print(tmp0)

    return tmp0