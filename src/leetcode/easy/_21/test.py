from solution import Solution
from solution import ListNode

s = Solution()
INPUT = [
    ([1, 2, 4], [1, 3, 4]), 
    ([], []),
    ([], [0])
]

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged = s.mergeTwoLists(list1, list2)
while merged != None:
    print(merged.val)
    merged = merged.next