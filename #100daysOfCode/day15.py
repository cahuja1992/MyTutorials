# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      if l1.val < l2.val:
        ptr1 = l1
        ptr2 = l2
      else:
        ptr1 = l2
        ptr2 = l1
      prev = ptr1
      ptr1 = ptr1.next
      while ptr1 and ptr2:
        # print(ptr1.val, ptr2.val)
        if ptr1.val<ptr2.val:
          prev = ptr1
          ptr1 = ptr1.next
        else:
          temp = ptr2
          ptr2 = ptr2.next
          prev.next = temp
          temp.next = ptr1
          prev = temp
      while ptr2:
        prev.next = ptr2
        prev = prev.next
        ptr2 = ptr2.next
      return l1
