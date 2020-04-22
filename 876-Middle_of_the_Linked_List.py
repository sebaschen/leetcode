#876-Middle_of_the_Linked_List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:# if head is empty then return
            return head
        pointer_fast, pointer_slow = head, head # if head is empty then return
        while pointer_fast and pointer_fast.next: #check each time the faster one is empty or not(if we                                                   #encounter odd)
            pointer_fast = pointer_fast.next.next
            pointer_slow = pointer_slow.next
        return pointer_slow
            
        
