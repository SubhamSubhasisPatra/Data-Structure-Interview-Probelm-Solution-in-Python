"""
Original Linked List: 1 -> 2 -> 3 -> 4 -> 5

Step 1:      _________
            |         V
            1 -> 2 -> 3 -> 4 -> 5
            |___^    |___^

Step 2:      _________________
            |                 V
            2 -> 1 -> 4 -> 3 -> 5
            |___^    |___^    |

Step 3:      ________________________
            |                        V
            2 -> 1 -> 4 -> 3 -> 5 -> NULL
            |___^    |___^    |___^

Final Linked List: 2 -> 1 -> 4 -> 3 -> 5

"""

from main import LinkedList


def swap_pairs(head):
    if not head or not head.next:
        return head

    prev = None
    cur = head
    while cur and cur.next:
        temp = cur.next
        cur.next = temp.next
        temp.next = cur

        if prev:
            prev.next = temp
        else:
            head = temp
        prev = cur
        cur = cur.next
    return head


if __name__ == '__main__':
    node_elements = [1, 2, 3, 4, 5]
    l = LinkedList()
    for element in node_elements:
        l.add_to_end_of_list(element)

    head = l.head
    l.show_list(head)
    print()
    head = swap_pairs(head)
    l.show_list(head)
