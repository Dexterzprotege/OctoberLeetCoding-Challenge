'''Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
4->2->1->3 to 1->2->3->4
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
-1->5->3->4->0 to -1->0->3->4->5
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 !=None and list2!=None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        if list1!=None:
            tail.next = list1
        if list2!=None:
            tail.next = list2
        return dummy.next
        
    def getMid(self, node):
        mid = None
        while node!=None and node.next!=None:
            if mid == None:
                mid = node
            else:
                mid = mid.next
            node = node.next.next
        m = mid.next
        mid.next = None
        return m
        
