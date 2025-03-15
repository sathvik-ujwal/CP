class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) ->ListNode:
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


head = ListNode(1, ListNode(2))
reversed_head = reverse_list(head)
print(reversed_head.val)
print(reversed_head.next.val)  