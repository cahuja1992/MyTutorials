# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
      s = l1
      f = l1
      while f and f.next:
        s = s.next
        f = f.next.next
      
      temp = s.next
      s.next = None
      
      while temp:
        next = temp.next
        temp.next = s
        s = temp
        temp = next
      
      while s and l1:
        if s.val!=l1.val:
          return False
        s=s.next
        l1=l1.next
      return True
      
    
