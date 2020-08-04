# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def recursive_reverse(self, node, k):
      if node == None or node.next == None:
        return node
      prev = node
      ptr = node.next
      i=1
      while i<k and ptr:
          nex = ptr.next
          ptr.next = prev
          prev = ptr
          ptr = nex
          i+=1
      node.next = self.recursive_reverse(ptr, k)
      return prev
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
      return self.recursive_reverse(l1, key)
