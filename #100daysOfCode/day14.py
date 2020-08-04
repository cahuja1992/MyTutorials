#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      ptr = head
      m = 0
      while ptr:
        ptr=ptr.next
        m+=1
      
      if m==n:
        return head.next
      ptr = head 
      for _ in range(0, m-n-1):
        ptr = ptr.next
      
      if ptr.next.next:
        ptr.next = ptr.next.next
      else:
        ptr.next = None
      return head
      
