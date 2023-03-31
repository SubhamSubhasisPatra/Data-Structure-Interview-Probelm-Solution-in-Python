"""
To delete a node from a linked list, we need to adjust the next pointers of the preceding node and the node to be deleted.

Let's assume we have a singly linked list with three nodes: A -> B -> C. If we want to delete the node B, we would need to do the following steps:

Traverse the list to find the node B and its preceding node A.
Set the next pointer of node A to point to the node C (i.e., bypassing node B).
Free the memory allocated to node B.
Here's an arrow diagram that illustrates the initial and final state of the linked list:

Initial state:           Final state:

   A -> B -> C            A -> C
       ^                    ^
       |                    |
    current              current

"""

from main import LinkedList


def delete_node(head, index):
    counter = 0

    if index == counter:
        # here a special case will be applied
        return None

    cur_node = head
    prev = None
    while cur_node:
        if counter == index:
            prev.next = cur_node.next
        counter += 1
        prev = cur_node
        cur_node = cur_node.next
    return head


if __name__ == '__main__':
    # add the delete node tests case
    cur_list = LinkedList()

    arr = [1, 2, 3, 4, 5]
    for element in arr:
        cur_list.add_to_end_of_list(element)

    cur_list.show_list(cur_list.head)
    print()
    new_head = delete_node(cur_list.head, 2)
    cur_list.show_list(new_head)
