class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val: int):
    dummy = ListNode()
    dummy.next = head

    tmp = dummy
    while tmp and tmp.next:
        if tmp.next.val == val:
            tmp.next = tmp.next.next

        tmp = tmp.next

    return dummy.next

head  = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))

res = removeElements(head, 7)