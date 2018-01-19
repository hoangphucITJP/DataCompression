def LZW_func(Str):
	#----------------frequency of each character----------

	my_dict = []


	for i in Str:
		if i not in my_dict:
			my_dict += [i]

	my_dict.sort()
	ori_dict = my_dict
	ori_dict = str(ori_dict)

	#----------------LZW------------
	P=""
	result = ""
	for i in Str:
		C = i
		if P+C in my_dict:
			P = P+C
		else:
			result += str(my_dict.index(P) + 1) + " "
			my_dict += [P+C]
			P = C

	result += str(my_dict.index(P) + 1)

	result += "!~!"
	result += ori_dict
	return result

