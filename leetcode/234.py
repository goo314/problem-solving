"""LeetCode

Algorithm : 
    Linked List
Level :
    Easy
Status :
    Accepted

Sat Mar  1 23:14:10 KST 2025
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        if arr == arr[::-1]:
            return True
        return False