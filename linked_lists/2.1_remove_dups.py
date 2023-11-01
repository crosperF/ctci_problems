from test_list import ll

# remove duplicates
# O(N) - time
# O(N) - space
def remove_dups(node):
    hash_set = set()

    pre = None
    cur = node 

    while cur:
        if cur.val in hash_set:
            pre.next = cur.next
            cur = pre.next
        else:
            hash_set.add(cur.val)
            pre = cur
            cur = cur.next
    
# remove_dups(ll.head)
# ll.traverse()