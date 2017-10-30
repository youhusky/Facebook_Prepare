def stringcompression(s):
	res_list = []
	count = 0
	for i in range(len(s)):
		count += 1
		if i+1 >= len(s) or s[i] != s[i+1]:
			res_list.append(str(count))
			res_list.append(s[i])
			count = 0
	return "".join(res_list) if len(res_list) < len(s) else s
	
print stringcompression("aasss")