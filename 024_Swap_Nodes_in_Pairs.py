#24. Swap Nodes in Pairs
#24_Swap_Nodes_in_Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            n1,n2 = head.next, head.next.next #2,1,3,4
            n1.next = n2.next   
            n2.next = n1
            head.next = n2      
            head = n1
        return dummy.next
    
    #recursive way
    # def swapPairs(self, head):
    #     if not head or not head.next: return head
    #     new_start = head.next.next
    #     head, head.next = head.next, head
    #     head.next.next = self.swapPairs(new_start)
    #     return head