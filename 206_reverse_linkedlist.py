# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        
        prev = None 
        curr = head        
        while curr:
            next = curr.next #先存後面
            curr.next = prev#斷掉第一個和後面的
            prev = curr#將斷的第一個存到答案
            curr= next #迭代第一個
        return prev
        
