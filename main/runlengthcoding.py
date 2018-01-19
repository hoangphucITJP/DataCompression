#Run lenght coding

def runlengthcoding_func(Str):
	Str = ' '.join([i.strip() for i in Str.split(' ') if i != ''])

	tmp = ""
	length = 0
	result = ""


	for i in Str:
		if i != tmp:
			if length != 0:
				result += str(length) + tmp	+ " "
			tmp = i
			length = 1
		else:
			length += 1
	result += str(length) + tmp

	result += "!~!"
	return result




