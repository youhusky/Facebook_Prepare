def stringrotation(s1,s2):
	# check
	if not s1 or not s2:
		return False
	if len(s1) != len(s2):
		return False
	return True if s2 in s1+s1 else False
print stringrotation("waterbottle","erbottlewat")
