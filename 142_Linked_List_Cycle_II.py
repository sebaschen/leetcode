# 142. Linked List Cycle II
# 142_Linked_List_Cycle_II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1. set moethod
        if not head: return None
        visited = set()
        while head:
            if head in visited:                
                return head
            visited.add(head)
            head = head.next
        return None
            
#         2. two pointer method
#           slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 break
#         slow = head
#         if not fast or not fast.next:
#             return None
#         while slow != fast:
#             slow = slow.next
#             fast = fast.next
#         return fast
            