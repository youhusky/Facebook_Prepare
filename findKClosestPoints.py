import heapq
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

def findKClosestPoints(points, k):
	pq = []
	for point in points:
		heapq.heappush(pq,(-point.x*point.x-point.y*point.y, point))
		if len(pq) > k:
			heapq.heappop(pq)
	res = []
	while pq:
		res.append(heapq.heappop(pq)[1])
	print res[0].x, res[0].y
	return res

a = Point(1,1)
b = Point(2,2)
print findKClosestPoints([a,b],1)