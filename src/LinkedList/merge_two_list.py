"""
List 1: 1 -> 4 -> 6
List 2: 2 -> 3 -> 5

   +----+     +----+     +----+
   |  1 | --> |  4 | --> |  6 |
   +----+     +----+     +----+
                  |         |
                  |         v
   +----+     +----+     +----+
   |  2 | --> |  3 | --> |  5 |
   +----+     +----+     +----+
                  |         |
                  v         |
                 None   +----+
                        |None|
                        +----+

Merged list: 1 -> 2 -> 3 -> 4 -> 5 -> 6

"""

from main import LinkedList, Node


def merge_lists(head1, head2):
    # check if any of the linked lists is empty
    if not head1:
        return head2
    elif not head2:
        return head1

    # find the head of the merged linked list
    if head1.data < head2.data:
        head = head1
        cur_node_1 = head1.next
        cur_node_2 = head2
    else:
        head = head2
        cur_node_1 = head1
        cur_node_2 = head2.next

    # merge the linked lists
    cur_node_merged = head
    while cur_node_1 and cur_node_2:
        if cur_node_1.data < cur_node_2.data:
            cur_node_merged.next = cur_node_1
            cur_node_1 = cur_node_1.next
        else:
            cur_node_merged.next = cur_node_2
            cur_node_2 = cur_node_2.next
        cur_node_merged = cur_node_merged.next

    # attach the remaining nodes, if any
    if cur_node_1:
        cur_node_merged.next = cur_node_1
    elif cur_node_2:
        cur_node_merged.next = cur_node_2

    return head


if __name__ == '__main__':
    first_list = LinkedList()
    second_list = LinkedList()

    for i in [1, 4, 6]:
        first_list.add_to_end_of_list(i)

    for i in [2, 3, 5]:
        second_list.add_to_end_of_list(i)

    head = merge_lists(first_list.head, second_list.head)
    second_list.show_list(head)
