import heapq
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

# O (nlgk)
# O(k)
def findKClosestPoints(points, k):
	pq = []
	for point in points:
		heapq.heappush(pq,(-point.x*point.x-point.y*point.y, point))
		if len(pq) > k:
			heapq.heappop(pq)
	for i in pq:
		print i[1].x, i[1].y
	res = []
	while pq:
		res.append(heapq.heappop(pq)[1])
	# for i in res:
	# 	print i.x, i.y
	return res

a = Point(1,1)
b = Point(2,2)
c = Point(3,3)
print findKClosestPoints([a,b],2)