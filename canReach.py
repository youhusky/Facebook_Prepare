
def canReach(x,y):
	while x>= 1 and y>=1:
		if x > y:
			x -= y
		else:
			y -=x
		if x==1 and y==1:
			return True
	return False

