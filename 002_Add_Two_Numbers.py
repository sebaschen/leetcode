# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0 #deal with the carrier number, e.g. 6+7 =13, 1 is its carrier number.
        dummy = ListNode(0) #use it as the initial pointer that can directly use for pointer
        p = dummy  #use P as the pointer
        
        #正常兩邊都有element的時候
        while l1 and l2:
            p.next = ListNode((l1.val +l2.val+carry)%10)
            carry = (l1.val +l2.val+carry)//10
            l1 = l1.next
            l2 = l2.next
            p = p.next
            
        #只有l2有element的時候
        while l2:
            p.next = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)//10            
            l2 = l2.next
            p = p.next
                
        #只有l1有element的時候   
        while l1:
            p.next = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)//10            
            l1 = l1.next
            p = p.next
        #如果最後一位相加 >10
        if carry ==1:
            p.next=ListNode(1)
            
        return dummy.next

