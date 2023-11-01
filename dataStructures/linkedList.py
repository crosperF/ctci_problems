class Node:
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_new_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, val):
        new_node = Node(val)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete_node(self, n):

        dummy = Node(0)
        dummy.next = self.head
        node = dummy

        while n > 0:
            node = node.next
            n -= 1
        
        node.next = node.next.next

        self.head = dummy.next
        if node.next == None: #if the last node is removed - change tail
            self.tail = node.next
            
    def traverse(self):
        node = self.head
        s = ""

        while node:
            s += f"{str(node.val)} -> " 
            node = node.next

        print(s)

ll = LinkedList()
ll.add_to_tail(20)
ll.add_to_tail(24)
ll.add_new_head(10)
ll.add_new_head(7)
ll.add_new_head(9)
ll.traverse()
# ll.delete_node(3)
# ll.delete_node(1)
# ll.delete_node(0)
ll.delete_node(0)
ll.delete_node(0)
ll.delete_node(0)
ll.delete_node(0)
# ll.delete_node(0)
# print(ll.tail.val)
ll.traverse()
