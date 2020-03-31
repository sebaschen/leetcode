# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("-inf")) #給定初始值，create一個新node,不影響他的值, 才用float("-inf")
        while head: #只要有head存在
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next 



