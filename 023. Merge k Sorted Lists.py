# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        # O(nlgk)
        # n node in list and the size of heap is k
        # O(k)
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        dummy = ListNode(0)
        head = dummy
        for node in lists:
            # imp !
            # O(k)
            if node:
                heapq.heappush(pq, (node.val, node))
        while pq:
            #O(n)
            head.next = heapq.heappop(pq)[1]
            head = head.next
            if head.next:
                # O(logk)
                heapq.heappush(pq,(head.next.val, head.next))
        return dummy.next
