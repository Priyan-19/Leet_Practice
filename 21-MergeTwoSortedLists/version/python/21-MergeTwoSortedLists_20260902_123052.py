# Last updated: 9/2/2026, 12:30:52 PM
1class Solution:
2    def mergeTwoLists(
3        self,
4        list1: Optional[ListNode],
5        list2: Optional[ListNode]
6    ) -> Optional[ListNode]:
7
8        dummy = ListNode()
9        current = dummy
10
11        while list1 and list2:
12            if list1.val <= list2.val:
13                current.next = list1
14                list1 = list1.next
15            else:
16                current.next = list2
17                list2 = list2.next
18
19            current = current.next
20
21        if list1:
22            current.next = list1
23        else:
24            current.next = list2
25
26        return dummy.next