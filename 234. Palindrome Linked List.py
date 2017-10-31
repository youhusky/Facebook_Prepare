# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # find mid
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        newHead = slow
        prev = None
        # reverse linkedlist
        while newHead:
            temp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp
        
        # prev - newhead for the second part
        
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        
        
        