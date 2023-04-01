"""
   +---+    +---+    +---+    +---+    +---+
   | H | -> | A | -> | B | -> | C | -> | D |
   +---+    +---+    +---+    +---+    +---+
                          ^               |
                          |               |
                          +---------------+

In this example, the linked list has a cycle between nodes C and D.


"""

from main import Node


def delete_cycle(head_pointer):
    if not head_pointer:
        return False

    slow, fast = head_pointer, head_pointer.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow, fast = slow.next, fast.next.next

    return False


if __name__ == '__main__':
    # Create nodes
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Connect nodes
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Create a cycle between nodes 3 and 4
    node5.next = node3
    result = delete_cycle(head)
    print(f"Cycle Status {result}")
