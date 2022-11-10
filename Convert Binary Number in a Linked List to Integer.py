# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head):
        res =0
        while head:
           # ans=ans*2 +head.val
            res = res<<1 | head.val
            head=head.next
        return res
