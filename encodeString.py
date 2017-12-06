def encodeString(s):
	# O(n)
	if not s:
		return ""
	res = ""
	count = 1
	i = 0
	while i < len(s):
		while i < len(s) -1 and s[i]==s[i+1]:
			count += 1
			i += 1
		res += s[i] + str(count)
		count = 1
		i += 1
	print res

encodeString("wwwwaaadexxxxxx")