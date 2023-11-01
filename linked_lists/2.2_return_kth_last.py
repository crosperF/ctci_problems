from test_list import ll


def kth_last(head, k):
    p1 = p2 = head

    for i in range(k):
        p2 = p2.next
    
    while p2:
        p2 = p2.next
        p1 = p1.next
    
    return p1.val

print(kth_last(ll.head, 1)) 

