# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        #ans is an unchanging reference that points to res -> the prev node of res
        ans = res  
        #iterate through two lists
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
 
        #if one of the lists hit end, append the additional nodes of that list to the ans
        while l1:
            res.next = l1
            l1 = l1.next
            res = res.next
            
        while l2:
            res.next = l2
            l2 = l2.next
            res = res.next
           
        return ans.next
