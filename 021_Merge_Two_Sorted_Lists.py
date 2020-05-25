# 21. Merge Two Sorted Lists
# 21_Merge_Two_Sorted_Lists.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = []
        dummy = ListNode(0) #use dummy as the pointer
        p = dummy #use p as the initial pointer that can directly traverse through the linkedlist
        
        #1. always consider the boundary case
        if not l1 and not l2:
            return None
        
        #Main:        
        """
        1. Append 2 linkelist to one list
        2. sort the list
        3. put the list to a linkedlist
        """
        while l1 or l2:
            if l1:
                result.append(l1.val)
                l1 =l1.next
            if l2:
                result.append(l2.val)
                l2 = l2.next
        result = sorted(result)
        for i in result:
            p.next = ListNode(int(i))
            p = p.next
        return dummy.next
