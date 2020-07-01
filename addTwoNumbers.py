# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
  def __init__(self, val=None):
    self.head = ListNode(val)

  def add(self, val=0):
    if self.head.val is None:
      self.head = ListNode(val)
    else:
      node = self.head
      while node.next is not None:
        node = node.next
      node.next = ListNode(val)

  def display(self):
    node = self.head
    while node:
      print(node.val)
      node = node.next


class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    firstNumber = ""
    while l1:
      firstNumber += str(l1.val)
      l1 = l1.next

    secondNumber = ""
    while l2:
      secondNumber += str(l2.val)
      l2 = l2.next

    answer = str(int(firstNumber[::-1]) + int(secondNumber[::-1]))[::-1]
    nodeHead = ListNode(val=int(answer[0]))
    node = nodeHead
    for i in answer[1:]:
      node.next = ListNode(val=int(i))
      node = node.next

    return nodeHead


firstInput = [2, 4, 3]
SecondInput = [5, 6, 4]

firstList = LinkedList()
SecondList = LinkedList()

for i in firstInput:
  firstList.add(i)

for i in SecondInput:
  SecondList.add(i)

Solution.addTwoNumbers(Solution, firstList.head, SecondList.head)
