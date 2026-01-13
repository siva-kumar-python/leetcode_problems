#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.hed = None

    def appendend(self,val):
        if self.hed is None:
            node = ListNode(val,None)
            self.hed = node
            return
        ptr = self.hed
        while ptr.next!=None:
            ptr = ptr.next
        ptr.next = ListNode(val,None)

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # res = []
        # ptr = head
        # while ptr!=None:
        #     if ptr.val not in res:
        #         res.append(ptr.val)
        #         self.appendend(ptr.val)
        #     ptr = ptr.next
        # return self.hed
        if head is None or head.next is None:
            return head
        ptr=head.next
        while   ptr and head.val==ptr.val:
            head=ptr
            ptr=ptr.next
        prev=head
        ptr=head.next
        while ptr:
            if prev.val==ptr.val:
                prev.next=ptr.next
                ptr=ptr.next
            else:
                prev=ptr
                ptr=ptr.next
        return head

        