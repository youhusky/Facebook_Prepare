# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	# Iterative
	# last Node prev -> curr == None
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        prev = None
        curr = head
        while curr:
        	nextNode = curr.next
        	curr.next = prev
        	prev = curr
        	curr = nextNode
        return prev

    # Recursive
    def reverseList(self, head):
	    """
	    :type head: ListNode
	    :rtype: ListNode
	    """
	    if not head or not head.next:
	    	return head
	    second = head.next # save nextNode
	    head.next = None # forward cut
	    newNode = self.reverseList(second)
	    second.next = head # backward connect
	    return newNode
