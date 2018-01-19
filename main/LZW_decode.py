from sympy import sympify

#Str="wabbawabba"
#Str_de = "31221461"


#Str="ababbabcababba"
#Str_de = "124523461"


#----------------LZW decode------------
def LZW_decode_func(Str,List):

	Str_de = Str
	my_dict = sympify(List)
	code = [i.strip() for i in Str_de.split(' ')]
	s=""
	result=""

	for i in code:
		k = i
		if len(my_dict) >= sympify(k):
			entry = my_dict[sympify(k)-1]
		else:
			entry = ""

		if entry == "":
			entry = s + s[0]

		result += entry
		if s!= "":
			my_dict += [s + entry[0]]
		s = entry



	#result += str(my_dict.index(P) + 1)
	return(result)




