import heapq
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __repr__(self):
		return repr((self.x,self.y))

# O (nlgk)
# O(k)
def findKClosestPoints(points, k):
	# corner case
	if not points:
		return []
	if len(points) <= k:
		return points
	pq = []
	for point in points:
		heapq.heappush(pq,(-point.x*point.x-point.y*point.y, point))
		if len(pq) > k:
			heapq.heappop(pq)
	res = []
	while pq:
		res.append(heapq.heappop(pq)[1])

	return res

a = Point(1,1)
b = Point(2,2)
c = Point(3,3)
print findKClosestPoints([a,b],2)