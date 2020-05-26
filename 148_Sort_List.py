#148_Sort_List
#148. Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = fast = head  
        while fast and fast.next:
            pre = slow
            slow = slow.next   #慢指针走一步
            fast = fast.next.next  # 快指针走两步
        pre.next = None   # 将左右两半截断
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self , left,right):
        res = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
            if left :
                cur.next = left
            if right:
                cur.next = right
        return res.next
