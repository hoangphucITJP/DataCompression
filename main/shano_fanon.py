import operator
from sympy import sympify

Str="aaabaccdeddfffgggggg---+++;;\n"

def shano_fanon_func(Str):
	#----------------frequency of each character----------

	my_dict = {}
	element_dict = {i for i in my_dict}

	for i in Str:
		if not {i}.issubset(element_dict):
			my_dict[i] = 1
			element_dict.add(i)
		else:
			my_dict[i] += 1


	#Sort dictionary
		#--convert tu list tuple to sort
	sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
		#--convert again to dict
	my_dict = dict((x, y) for x, y in sorted_dict)





	#----------------Build Tree------------
	element_mydict = [i for i in my_dict]

	def SH(in_dict):
		element_in_dict = [i for i in in_dict]
		if len(element_in_dict) == 1:
			if "[" in element_in_dict[0]:
				return sympify(element_in_dict[0])
			else:
				return element_in_dict[0]
		else:
			sub_dict1 = {}
			sub_dict2 = {}
			for i in element_in_dict:
				if sum(sub_dict1.values()) < sum(sub_dict2.values()):
					sub_dict1[i] = in_dict[i]
				else:
					sub_dict2[i] = in_dict[i]

			return [SH(sub_dict1),SH(sub_dict2)]
		#print("------------")
		#print(sub_dict1)
		#print(sub_dict2)

	Tree = SH(my_dict)





	global dict_bin
	dict_bin = {}
	global tmp2
	tmp2 = ''

	#from tree return to dictionary binary
	def BinFunc(my_list):
		global dict_bin
		global tmp2
		for i in my_list:

			tmp3 = tmp2
			tmp2 += str(my_list.index(i))
			if type(i) is list:
				#tmp2 += str(my_list.index(i))
				BinFunc(i)
			else:
				#tmp3 = tmp2

				#tmp2 += str(my_list.index(i))
				dict_bin[str(i)] = tmp2

			tmp2 = tmp3
		return 	dict_bin



	dict_bin2 = BinFunc(Tree)



	result = ""

	for i in Str:
		result += dict_bin2[i]
	result += "!~!"
	result += str(Tree)
	return(result)




