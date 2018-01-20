from .huffman import huffman_func
from .LZW import LZW_func
from .runlengthcoding import runlengthcoding_func
from .shano_fanon import shano_fanon_func
from .binary_converter import SaveToBin
from numpy import array, dtype
import numpy as np

dispatcher = {'huffman': huffman_func, 'LZW': LZW_func, 'run_length': runlengthcoding_func, 'shano_fanon': shano_fanon_func}

def Encode(source, destination, algo):
    file = open(source, encoding='utf-8')
    Str = file.read()
    file.close()
    print('origin: ', Str)
    result = dispatcher[algo](Str)
    print('result: ', result)
    if algo == 'run_length':
        file = open(destination, 'w', encoding='utf-8')
        file.write(result)
        file.close()
    elif algo == 'LZW':
        Dict = result[0]
        Dict = ''.join(Dict)
        Dict = (Dict + '\0').encode(encoding='utf-8')
        data = result[1]
        intType = np.min_scalar_type(max(data))
        print(max(data))
        print(intType)
        data = array(data).astype(intType)
        Type = {dtype('uint8'): 8, dtype('uint16'): 16, dtype('uint32'): 32, dtype('uint64'): 64}

        file = open(destination, 'wb')
        file.write(Type[intType].to_bytes(1, 'big'))
        file.write(Dict)
        file.write(data.tobytes())
        file.close()
    else:
        SaveToBin(result, destination)