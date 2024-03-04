# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        carry = 0
        head = ListNode(-1)
        tail = head

        while l1 and l2:

            temp = l1.val + l2.val + carry
            l1=l1.next
            l2=l2.next

            tail.next = ListNode(temp%10)
            tail = tail.next

            carry = temp//10

        while l1:

            temp = l1.val + carry
            l1=l1.next

            tail.next = ListNode(temp%10)
            tail = tail.next

            carry = temp//10

        while l2:

            temp =  l2.val + carry
            l2=l2.next

            tail.next = ListNode(temp%10)
            tail = tail.next

            carry = temp//10

        while carry:

            temp =  carry

            tail.next = ListNode(temp%10)
            tail = tail.next

            carry = 0

        return head.next