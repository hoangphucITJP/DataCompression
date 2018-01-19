from .huffman_decode import huffman_decode_func
from .LZW_decode import LZW_decode_func
from .shano_fanon_decode import shano_fanon_decode_func
from .runlengthdecode import runlengthdecode_func
from .binary_converter import LoadFromBin

dispatcher = {'huffman': huffman_decode_func, 'LZW': LZW_decode_func, 'run_length': runlengthdecode_func,
              'shano_fanon': shano_fanon_decode_func}

def Decode(source, destination, algo):
    str = None
    if algo in ['run_length', 'LZW']:
        file = open(source, mode='r', encoding='utf-8')
        str = file.read()
        file.close()
    else:
        str = LoadFromBin(source)
    tmp = str.split("!~!")

    Str = tmp[0]
    List = tmp[1]

    if algo == 'run_length':
        result = dispatcher[algo](Str)
        file = open(destination, 'w', encoding='utf-8')
        file.write(result)
        file.close()
    elif algo == 'LZW':
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