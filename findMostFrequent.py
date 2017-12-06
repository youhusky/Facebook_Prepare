from collections import defaultdict
def findMostFrequent(s):
	# O(n)
	dic = defaultdict(int)
	count = 0
	res = ""
	if not s:
		return res

	for char in s:
		char = char.lower()
		if not char.isalpha():
			continue
		if char == " ":
			continue
		dic[char] += 1
		if dic[char] > count:
			count = dic[char]
			res = char
	print res, count

def findMostFrequent2(s):
	# O(n)
	dic = defaultdict(int)
	count1 = 0
	count2 = 0
	c1 = ""
	c2 = ""
	if not s:
		return res

	for char in s:
		char = char.lower()
		if not char.isalpha():
			continue
		if char == " ":
			continue
		dic[char] += 1
		if dic[char] > count1:
			if char == c1:
				count1 += 1
			else:
				count2 = count1
				c2 = c1
				count1 = dic[char]
				c1 = char
		elif dic[char] > count2:
			count2 = dic[char]
			c2 = char
		if count1 - count2 >= len(s) - s.index(char):
			break
	print c1, c2, count1, count2

s = "addassxvwrcvssd"
findMostFrequent(s)
findMostFrequent2(s)