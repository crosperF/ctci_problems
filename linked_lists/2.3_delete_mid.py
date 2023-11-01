from test_list import ll

# renaming all the nodes from the given node
# def delete(node):
#     pre = cur = node

#     while cur.next:
#         cur.val = cur.next.val
#         pre = cur
#         cur = cur.next
    
#     pre.next = None

# copying value from next node and delete next node 
def delete(node):
    if not node or not node.next:
        return False

    node.val = node.next.val
    node.next = node.next.next

delete(ll.head.next.next.next)
ll.traverse()