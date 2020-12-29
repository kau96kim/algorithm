# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def push(self, new_data):
        node = ListNode(new_data[0])
        head = node
        for i in new_data[1:]:
            node.next = ListNode(i)
            node = node.next

        return head

    def printList(self, head):
        while head:
            print(f"{head.val}, ", end=""),
            head = head.next


class Solution:
    def getListLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        length = self.getListLength(self, head)
        targetIndex = length - n - 1

        if length == 1:
            head = head.next
            return head

        if targetIndex == -1:
            return head.next

        for i in range(targetIndex + 1):
            if i == targetIndex:
                head.next = head.next.next
            else:
                head = head.next

        return node

head = ListNode.push(ListNode, [1, 2])
ans = Solution.removeNthFromEnd(Solution, head, 2)
ListNode.printList(ListNode, ans)