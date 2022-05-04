def ConvertLine(curr_string):
	curr_string = curr_string.lower()
	#print(curr_string)
	curr_string = [
	#Если текущий символ имеет сходство с другим в строке, то записываем ")"
	')' 
	if (curr_string[index] in (curr_string[:index]+curr_string[index+1:])) 
	#Иначе записываем "("
	else 
	'(' 
	# В цикле назначем текущий индекс
	for index in range(len(curr_string))
	]
	return ''.join(curr_string)



if __name__ == '__main__':
	list_of_strings=[]
	with open('input.txt', 'r') as f_re:
		for read_string in f_re.readlines():
			if (read_string[-1]=='\n'):

				read_string = read_string[:-1]
			list_of_strings.append(read_string)
	with open('output.txt', 'w') as f_wr:
		for curr_string in list_of_strings:
			result_string = ConvertLine(curr_string)
			print('"'+curr_string+'"'+' => '+'"'+result_string+'"')
			f_wr.write(result_string+'\n')