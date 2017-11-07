# Given a nested list of integers, implement an iterator to flatten it.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Given the list [1,[4,[6]]],

# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self,nestedList):
        self.queue = collections.deque([])
        
        for elem in nestedList:
            if elem.isInteger():
                self.queue.append(elem.getInteger())
            else:
                newList = NestedIterator(elem.getList())
                
                while newList.hasNext():
                    self.queue.append(newList.next())
    def hasNext(self):
        if self.queue:
            return True
        return False
    def next(self):
        return self.queue.popleft()

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())