from .huffman import huffman_func
from .LZW import LZW_func
from .runlengthcoding import runlengthcoding_func
from .shano_fanon import shano_fanon_func
from .binary_converter import SaveToBin

dispatcher = {'huffman': huffman_func, 'LZW': LZW_func, 'run_length': runlengthcoding_func, 'shano_fanon': shano_fanon_func}

def Encode(source, destination, algo):
    file = open(source, encoding='utf-8')
    Str = file.read()
    file.close()
    print('origin: ', Str)
    result = dispatcher[algo](Str)
    print('result: ', result)
    if algo in ['run_length', 'LZW']:
        file = open(destination, 'w', encoding='utf-8')
        file.write(result)
        file.close()
    else:
        SaveToBin(result, destination)