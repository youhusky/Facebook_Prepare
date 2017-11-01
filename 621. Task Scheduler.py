# Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

# However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

# You need to return the least number of intervals the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].



tasks = ["A","A","A","B","B","B"]
n = 2
from collections import defaultdict
def leastInterval(tasks, n):
    """
    # no -order
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    dic = defaultdict(int)
    for task in tasks:
        dic[task] += 1
    maxvalue = max(dic.values())
    count = 0
    for key in dic:
        if dic[key] == maxvalue:
            count += 1
    partcnt = maxvalue -1
    partlen = n + 1 - count
    
    remain_plot = partcnt * partlen
    remain_item = len(tasks) - maxvalue * count
    remainappend = max(0, remain_plot- remain_item)
    return len(tasks) + remainappend

def leastInterval2(tasks, n):
	# with order
	if not tasks:
		return 0
	dic = {}
	slot = 0
	for each in tasks:
		if each in dic and dic[each] > slot:
			# update
			slot = dic[each]
		dic[each] = slot + 1 + n
		slot += 1
	return slot

def leastInterval3(tasks, n):
	# many tasks and little slot-n
	if not tasks:
		return 0
	dic = {}
	slot = 0
	# init queue -with size n
	queue = []
	for each in tasks:
		if each in dic and dic[each] > slot:
			# update
			slot = dic[each]
		
	# del irrelevent task only save recent task
		if len(queue) == n+1:
			irrelevent = queue.pop(0)
			del(dic[irrelevent])
		queue.append(each)
		dic[each] = slot + 1 + n
		slot += 1
	return slot

print leastInterval3([1,2,3,4,5,6,1,2],2)

def leastInterval4(tasks, n):
	# with order print
	if not tasks:
		return 0
	dic = {}
	slot = 0
	res = ""
	for each in tasks:
		if each in dic and dic[each] > slot:
			# update
			waittime = dic[each] - slot
			res += "_" * waittime
			slot = dic[each]
		dic[each] = slot + 1 + n
		res += str(each)
		slot += 1
	return res
test = [1,2,1,1,3,4]
print leastInterval2(test,2)
print leastInterval3(test,2)
print leastInterval(tasks,2)
        
                
            
