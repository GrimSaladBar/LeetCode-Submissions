# Python Solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        #temp = 0
        """

        traversal_1 = headA
        traversal_2 = headB

        #Loops through until they intersect at the same node
        while (traversal_1 != traversal_2):
            traversal_1 = headB if traversal_1 is None else traversal_1.next
            traversal_2 = headA if traversal_2 is None else traversal_2.next

        return traversal_1
