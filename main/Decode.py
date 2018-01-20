from .huffman_decode import huffman_decode_func
from .LZW_decode import LZW_decode_func
from .shano_fanon_decode import shano_fanon_decode_func
from .runlengthdecode import runlengthdecode_func
from .binary_converter import LoadFromBin
import numpy as np
from numpy import dtype

dispatcher = {'huffman': huffman_decode_func, 'LZW': LZW_decode_func, 'run_length': runlengthdecode_func,
              'shano_fanon': shano_fanon_decode_func}

def Decode(source, destination, algo):
    Str = None
    List = None
    if algo == 'run_length':
        file = open(source, mode='r', encoding='utf-8')
        Str = file.read()
        file.close()
        tmp = Str.split("!~!")
        Str = tmp[0]
    elif algo == 'LZW':
        file = open(source, 'rb')
        intType = file.read(1)
        intType = int.from_bytes(intType, 'big')
        FileData = file.read()
        file.close()
        FileData = FileData.split(b'\0')
        List = FileData[0].decode('utf-8')
        List = list(List)
        data = b'\0'.join(FileData[1:])
        Type = {8: dtype('uint8'), 16: dtype('uint16'), 32: dtype('uint32'), 64: dtype('uint64')}
        data = np.frombuffer(data, Type[intType])
        data = data.tolist()
        data = [str(i) for i in data]
        Str = ' '.join(data)
        #print(data[0])
    else:
        Str = LoadFromBin(source)
        tmp = Str.split("!~!")
        Str = tmp[0]

    if algo == 'run_length':
        result = dispatcher[algo](Str)
        file = open(destination, 'w', encoding='utf-8')
        file.write(result)
        file.close()
    elif algo == 'LZW':
        print(Str)
        print(List)
        result = dispatcher[algo](Str, List)
        file = open(destination, 'w', encoding='utf-8')
        file.write(result)
        file.close()
    else:
        Tree = tmp[1]
        result = dispatcher[algo](Str, Tree)
        file = open(destination, 'w')
        file.write(result)
        file.close()