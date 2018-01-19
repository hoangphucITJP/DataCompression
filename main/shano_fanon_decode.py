from sympy import sympify

Tree = '[[d, [a, e]], [[g, c], [f, b]]]'
Tree = sympify(Tree)
#Str="aaabaccdeddfffgggggg"

Str="010010010111010101101000110000110110110100100100100100100"

#----------------frequency of each character----------

def shano_fanon_decode_func(Str, Tree):

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


