# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        O(V+E)
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        zero_indegree = []
        indegree = {}
        outdegree = {}
        
        # save the indegree and outdegree
        for i, j in prerequisites:
            if i not in indegree:
                indegree[i] = set()
            if j not in outdegree:
                outdegree[j] = set()
            indegree[i].add(j)
            outdegree[j].add(i)
            
        # find zero indegree in the graph
        for i in range(numCourses):
            if i not in indegree:
                zero_indegree.append(i)
        
        while zero_indegree:
            prerequest = zero_indegree.pop(0)
            if prerequest in outdegree:
                for course in outdegree[prerequest]:
                    indegree[course].remove(prerequest)
                    # empty
                    if not indegree[course]:
                        zero_indegree.append(course)
                del (outdegree[prerequest])
            
                        
        # check out degree
        if outdegree:
            return False
        return True

    def canFinish(self, n, pres):
        
        oud = [[] for _ in range(n)]  # indegree
        ind = [0] * n  # outdegree
        for succ,pre in pres:
            ind[succ] += 1
            oud[pre].append(succ)
        dq = []
        for i in range(n):
            if ind[i] == 0:
                dq.append(i)
        count = 0
        while dq:
            pre_course = dq.pop(0)
            count += 1
            for succ in oud[pre_course]:
                ind[succ] -= 1
                if ind[succ] == 0:
                    dq.append(succ)
        return count == n
            
