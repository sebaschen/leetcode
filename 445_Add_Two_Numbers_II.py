#445. Add Two Numbers II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        1. put two numbers sum together
        2. traverse through the sum, put integer to LinkedList
        """
        
        num1 =''
        num2 =''
        
        while l1:
            num1+=str(int(l1.val))
            l1 = l1.next
        while l2:
            num2+=str(int(l2.val))
            l2 = l2.next
        add = str(int(num1)+int(num2))
        head = ListNode(add[0])
        answer = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next =  node
            head = head.next
        return answer 
    
        