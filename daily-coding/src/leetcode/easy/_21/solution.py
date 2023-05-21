from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
            list2: Optional[ListNode]) -> Optional[ListNode]:
        # initalize
        # None placeholder, we'll advance this away when we return
        # doing it this way is easier???
        curr = ListNode(None) 
        head = curr
        while True:
            if list1 == None and list2 == None:
                break
            elif list1 != None and list2 != None:
                if list1.val <= list2.val:
                    curr, list1 = Solution.advance(curr, list1)
                elif list2.val <= list1.val:
                    curr, list2 = Solution.advance(curr, list2)
            elif list2 == None:
                curr, list1 = Solution.advance(curr, list1)
            elif list1 == None:
                curr, list2 = Solution.advance(curr, list2)
        return head.next

    # python passes args by assignment
    # mutable objects into a method get a reference to same object
    # outer scope knows nothing about object if we rebind
    # best practice is to return and reassign
    @staticmethod
    def advance(curr: ListNode, ln: ListNode):
        curr.next = ListNode(ln.val)
        curr = curr.next
        ln = ln.next
        return curr, ln

# smelly code
"""
class Solution:
    # static
    def mergeTwoLists(self, list1: Optional[ListNode], 
            list2: Optional[ListNode]) -> Optional[ListNode]:
        # initalize
        # None placeholder, we'll advance this away when we return
        # doing it this way is easier???
        curr = ListNode(None) 
        head = curr
        while True:
            if list1 == None and list2 == None:
                break
            elif list1 != None and list2 != None:
                if list1.val <= list2.val:
                    curr.next = ListNode(list1.val)
                    curr = curr.next
                    list1 = list1.next
                elif list2.val <= list1.val:
                    curr.next = ListNode(list2.val)
                    curr = curr.next
                    list2 = list2.next
            elif list2 == None:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            elif list1 == None:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        return head.next
"""