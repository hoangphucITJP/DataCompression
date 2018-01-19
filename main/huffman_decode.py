import operator
from sympy import sympify


'''
file = open('bin', 'rb')
b = file.read()
c = int.from_bytes(b, 'little')
print('integer: ', c)
binary = "{0:b}".format(c)
print('bits: ', binary)

Tree = '[[a, [c, [b, e]]], [g, [d, f]]]'
Tree = sympify(Tree)
#Str="aaabaccdeddfffgggggg"
'''





#----------------decode----------

def huffman_decode_func(Str, Tree):

	Tree = sympify(Tree)
	tmp = Tree
	result = ""
	for i in Str:
		if type(tmp[sympify(i)]) == list:
			tmp = tmp[sympify(i)]
		else:
			result += str(tmp[sympify(i)])
			tmp = Tree

	return result


