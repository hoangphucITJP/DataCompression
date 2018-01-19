def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def SaveToBin(str, filename):
    str = str.split('!~!')

    data = str[0]
    zeroCount = 0
    i = 0
    while data[i] == '0':
        i += 1
        zeroCount += 1

    data = bitstring_to_bytes(data)

    tree = str[1]
    tree += '\0'
    tree = tree.encode('utf-8')

    file = open(filename, 'wb')
    file.write(tree)
    file.write(zeroCount.to_bytes(1, 'big'))
    file.write(data)
    file.close()

def LoadFromBin(filename):
    file = open(filename, 'rb')
    FileData = file.read()
    file.close()
    FileData = FileData.split(b'\0')
    tree = FileData[0].decode('utf-8')
    data = bytes(b'\0'.join(FileData[1:]))
    zeroCount = data[0]
    #print('zero count: ', zeroCount)
    data = data[1:]
    #print('length: ', len(data))

    #print(tree)
    bitsArray = []
    for i in data:
        bits = "{0:b}".format(i)
        bits = '0' * (8 - len(bits)) + bits
        #print(bits)
        bitsArray.append(bits)

    bitsArray[0] = '0' * zeroCount + bitsArray[0].lstrip('0')
    bitsString = ''.join(bitsArray)
    ret = bitsString + '!~!' + tree
    return ret