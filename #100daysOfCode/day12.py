# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_num(head):
    ptr = head
    i=1
    res = 0
    while ptr:
        res = res*10+ptr.val
        ptr = ptr.next
    return res
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      res = list_to_num(l1)+list_to_num(l2)
        
      head = ListNode(0)
      if res == 0: return head
      while res:
          e, res = res%10, res//10
          head.next, head.next.next = ListNode(e), head.next
          
      return head.next
